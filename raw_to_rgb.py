import time
from demos import *

# 灰度世界白平衡
def gray_world_white_balance(img):
    # 分离图像的 R、G、B 通道
    B, G, R = cv2.split(img)

    # 计算各通道的平均值
    mu_R = np.mean(R)
    mu_G = np.mean(G)
    mu_B = np.mean(B)

    # 计算调整因子
    k_R = mu_G / mu_R
    k_B = mu_G / mu_B

    # 打印增益值
    print(f"Red channel gain (r_gain): {k_R}")
    print(f"Blue channel gain (b_gain): {k_B}")

    # 调整各通道的值
    R = R * k_R
    B = B * k_B
    G = G.astype(np.float64)

    # 合并通道
    balanced_img = cv2.merge([R, G, B])

    # 确保像素值在 [0, 65535] 范围内
    balanced_img = np.clip(balanced_img, 0, 65535).astype(np.uint16)

    return balanced_img

# 完美反射白平衡
def perfect_reflector_white_balance(image, top_ratio=0.1):
    # 将图像转换为浮点数，以避免在计算过程中溢出
    image = image.astype(np.float32)

    # 计算亮度，选取每个像素点三个通道的最大值作为亮度值
    brightness = np.max(image, axis=2)

    # 选择亮度大于阈值的像素作为候选白色像素
    threshold = np.percentile(brightness, 1 - top_ratio)
    mask = brightness > threshold

    # 分别计算候选白色像素中三个通道的平均值
    avgR = np.mean(image[:, :, 0][mask])
    avgG = np.mean(image[:, :, 1][mask])
    avgB = np.mean(image[:, :, 2][mask])

    # 计算平均亮度
    avg = (avgR + avgG + avgB) / 3.0
    scaleR = avg / avgR
    scaleG = avg / avgG
    scaleB = avg / avgB

    # 打印增益值
    print(f'R_gain: {scaleR}')
    print(f'B_gain: {scaleB}')

    # 创建一个与输入图像形状相同的全零数组
    balanced_image = np.zeros_like(image)

    # 对每个通道进行增益调整并裁剪到合法范围
    balanced_image[:, :, 0] = np.clip(image[:, :, 0] * scaleR, 0, 65535)
    balanced_image[:, :, 1] = np.clip(image[:, :, 1] * scaleG, 0, 65535)
    balanced_image[:, :, 2] = np.clip(image[:, :, 2] * scaleB, 0, 65535)

    # 将处理后的图像转换回无符号16为整数类型
    balanced_image = balanced_image.astype(np.uint16)

    return balanced_image

# 创建gamma校正查找表
def create_gamma_table(gamma, max_value=65535):
    invGamma = 1.0 / gamma
    table = np.array([(i / max_value) ** invGamma * max_value for i in np.arange(0, max_value + 1)]).astype("uint16")
    return table

# 调整图像伽马值
def adjust_gamma(image, gamma=1.0):
    table = create_gamma_table(gamma)
    # 手动应用查找表
    adjusted_image = np.zeros_like(image)
    adjusted_image[:, :, 0] = table[image[:, :, 0]]
    adjusted_image[:, :, 1] = table[image[:, :, 1]]
    adjusted_image[:, :, 2] = table[image[:, :, 2]]

    return adjusted_image

# 原始图像类
class RawImage:
    def __init__(self, file_path, parameters):
        self.file_path = file_path
        self.height = parameters['height']
        self.width = parameters['width']
        self.bit_depth = parameters['bit_depth']
        self.big_endian = parameters['big_endian']
        self.compression = parameters['compression']
        self.parameters = parameters
        self.data = None

    # 数据读取方法
    def read_data(self):
        start_time = time.time()  # 记录开始时间

        # 根据白平衡算法选择函数
        def wb_choose(white_balance, ready_data):
            print(white_balance)
            if white_balance == 'GrayworldWB':
                # 使用灰度世界白平衡算法
                new_data = gray_world_white_balance(ready_data)
            else:
                # 使用完美反射白平衡算法
                new_data = perfect_reflector_white_balance(ready_data)
            return new_data

        # 根据位深度选择数据类型
        dtype = np.uint16 if self.bit_depth > 8 else np.uint8
        data = np.fromfile(self.file_path, dtype=dtype)

        # 如果图像是压缩的，则进行解压缩
        if self.compression:
            data = self.decompress(data)

        # 如果是大端模式，则交换字节顺序
        if self.big_endian:
            data.byteswap(inplace=True)

        # 检查数据大小是否正确
        expected_size = self.height * self.width

        # 如果数据大小不正确，则抛出异常
        if data.size!= expected_size:
            print(f"Expected size: {expected_size}, but got {data.size}")
            raise ValueError("size not match")

        # 将读取到的数据重塑为指定的图像尺寸
        self.data = data.reshape((self.height, self.width))

        # 归一化
        normalized_data = cv2.normalize(self.data, None, 0, 65535, cv2.NORM_MINMAX)
        normalized_data = np.uint16(normalized_data)
        view_mode = self.parameters.get('view_mode', 'Demosica')  # 默认使用 Demosica
        bayer_pattern = self.parameters.get('bayer_pattern', 'RGGB')  # 默认使用 RGGB
        if view_mode == 'Demosica':
            self.data = demosaic_image(normalized_data, bayer_pattern)
        elif view_mode == 'Bayer':
            self.data = vng_demosaic(normalized_data, bayer_pattern)

        # 如果需要调整白平衡和伽马校正
        if self.parameters['adjust']:
            # 根据参数中指定的白平衡算法对图像进行处理
            data = wb_choose(self.parameters['wb'], self.data)

            # 将参数中的gamma值转化为浮点数类型
            gamma = float(self.parameters['gamma'])

            # 对图像进行伽马校正
            data = np.power(data / 65535.0, gamma) * 65535.0
            data = data.astype(np.uint16)

            # 如果需要应用色彩校正矩阵
            if self.parameters['ccm_checked']:
                print(self.parameters['ccm'])
                data = cv2.transform(data, self.parameters['ccm'])

            self.data = data.astype(np.uint16)

        end_time = time.time()  # 记录结束时间
        elapsed_time = end_time - start_time  # 计算运行时间
        print(f"read_data 方法的运行时间: {elapsed_time} 秒")

    def decompress(self, data):
        # 将输入的数据重塑为无符号8位整数类型
        data = data.reshape(np.uint8)

        # 根据位深度调用对应的解压缩方法并返回结果
        if self.bit_depth == 10:
            return self.decepressed_raw10(data)
        elif self.bit_depth == 12:
            return self.decepressed_raw12(data)
        elif self.bit_depth == 14:
            return self.decepressed_raw14(data)
        else:
            # 如果位深度不是以上几种情况，抛出异常
            raise NotImplementedError(f'Decompression for {self.bit_depth}-bit')

    # 位深度位10的解压缩函数
    def decepressed_raw10(self, date):
        # 创建一个形状位（self.height, self.width）的零数组，用于存储解压缩后的数据
        decepressed_data = np.zeros((self.height, self.width), dtype=np.uint16)

        # 设置索引变量，用于在解压缩数据数组中定位位置
        index = 0

        # 遍历输入的压缩数据数组，每次处理5个字节
        for i in range(0, len(date), 5):
            # 通过位操作将输入的数据组合成10位数据，并存储到解压缩数据数组中
            decepressed_data[index] = ((date[i] << 2) | ((date[i + 4] & 0b11000000) >> 6))
            decepressed_data[index + 1] = ((date[i + 1] << 2) | ((date[i + 4] & 0b00110000) >> 4))
            decepressed_data[index + 2] = ((date[i + 2] << 2) | ((date[i + 4] & 0b00001100) >> 2))
            decepressed_data[index + 3] = ((date[i + 3] << 2) | (date[i + 4] & 0b00000011))

            # 更新索引变量，每次处理4个解压缩后的数据
            index += 4

        return decepressed_data

    # 位深度位12的解压缩函数
    def decepressed_raw12(self, date):
        # 创建一个形状位（self.height, self.width）的零数组，用于存储解压缩后的数据
        decepressed_data = np.zeros((self.height, self.width), dtype=np.uint16)

        # 设置索引变量，用于在解压缩数据数组中定位位置
        index = 0

        # 遍历输入的压缩数据数组，每次处理3个字节
        for i in range(0, len(date), 3):
            # 通过位操作将输入的数据组合成12位数据，并存储到解压缩数据数组中
            decepressed_data[index] = ((date[i] << 4) | (date[i + 2] & 0x0f))
            decepressed_data[index + 1] = ((date[i + 1] << 4) | ((date[i + 2] & 0xf0) >> 4))

            # 更新索引变量，每次处理2个解压缩后的数据
            index += 2

        return decepressed_data

    # 位深度位14的解压缩函数
    def decepressed_raw14(self, date):
        # 创建一个形状位（self.height, self.width）的零数组，用于存储解压缩后的数据
        decepressed_data = np.zeros((self.height, self.width), dtype=np.uint16)

        # 设置索引变量，用于在解压缩数据数组中定位位置
        index = 0

        # 遍历输入的压缩数据数组，每次处理7个字节
        for i in range(0, len(date), 7):
            # 通过位操作将输入的数据组合成14位数据，并存储到解压缩数据数组中
            decepressed_data[index] = ((date[i] << 6) | ((date[i + 4] & 0b11111100) >> 2))
            decepressed_data[index + 1] = ((date[i + 1] << 6) | ((date[i + 4] & 0b00000011) << 4) | ((date[i + 5] & 0b11110000) >> 4))
            decepressed_data[index + 2] = ((date[i + 2] << 6) | ((date[i + 5] & 0b00001111) << 2) | ((date[i + 6] & 0b11000000) >> 6))
            decepressed_data[index + 3] = ((date[i + 3] << 6) | (date[i + 6] & 0b00111111))

            # 更新索引变量，每次处理4个解压缩后的数据
            index += 4

        return decepressed_data

# 根据bayer_pattern获取bayer转换代码
def get_bayer_conversion_code(bayer_pattern):
    return {
        'RG': 'RGGB',
        'BG': 'BGGR',
        'GB': 'GBRG',
        'GR': 'GRBG'
    }.get(bayer_pattern, 'RGGB')

# 对10位数据进行压缩
def compressed_raw10(data):
    byte = bytearray()

    # 遍历输入数据，每次处理4个数据点
    for i in range(0, len(data), 4):
        # 提取并处理每个数据点的高8位
        byte1 = (data[i] >> 2) & 0xFF
        byte2 = (data[i + 1] >> 2) & 0xFF
        byte3 = (data[i + 2] >> 2) & 0xFF
        byte4 = (data[i + 3] >> 2) & 0xFF

        # 提取并组合每个数据点的低2位
        byte5 = ((data[i] & 0x03) << 6) | ((data[i + 1] & 0x03) << 4) | ((data[i + 2] & 0x03) << 2) | (
                data[i + 3] & 0x03)

        # 将处理后的字节添加到字节数组中
        byte.extend([byte1, byte2, byte3, byte4, byte5])

    return byte

# 对12位数据进行压缩
def compressed_raw12(data):
    byte = bytearray()

    # 遍历输入数据，每次处理2个数据点
    for i in range(0, len(data), 2):
        # 提取每个数据点的低12位
        pixel0 = data[i] & 0xFFF
        pixel1 = data[i+1] & 0xFFF

        # 提取并处理第一个数据点的高8位
        byte0 = ((pixel0 >> 4) & 0xFF)

        # 提取并处理第一个数据点的低 4 位和第二个数据点的低 4 位
        byte2 = ((pixel1 >> 4) & 0xFF)

        # 提取并处理第二个数据点的高 8 位
        byte1 = ((pixel0 & 0x0F) << 4) | (pixel1 & 0x0F)

        # 将处理后的字节添加到字节数组中
        byte.extend([byte0, byte1, byte2])

    return byte

# 对14位数据进行压缩
def compressed_raw14(data):
    byte = bytearray()

    # 遍历输入数据，每次处理4个数据点
    for i in range(0, len(data), 4):
        # 提取每个数据点的低 14 位
        pixel0 = data[i] & 0x3FFF
        pixel1 = data[i] & 0x3FFF
        pixel2 = data[i] & 0x3FFF
        pixel3 = data[i] & 0x3FFF

        # 提取并处理第一个数据点的高 8 位
        byte0 = (pixel0 >> 6) & 0xFF
        byte1 = (pixel1 >> 6) & 0xFF
        byte2 = (pixel2 >> 6) & 0xFF
        byte3 = (pixel3 >> 6) & 0xFF

        # 提取并处理第一个数据点的低 6 位和第二个数据点的高 2 位
        byte4 = ((pixel0 & 0x3F) << 2) | ((pixel1 >> 2) & 0x03)

        # 提取并处理第二个数据点的低 4 位和第三个数据点的高 4 位
        byte5 = ((pixel1 & 0x0F) << 4) | ((pixel2 >> 10) & 0x0F)

        # 提取并处理第三个数据点的低 6 位和第四个数据点的高 6 位
        byte6 = ((pixel2 & 0x03) << 6) | (pixel3 & 0x3F)

        # 将处理后的字节添加到字节数组中
        byte.extend([byte0, byte1, byte2, byte3, byte4, byte5, byte6])

    return byte

# 根据输入数据的位深度进行压缩
def compress(data, bit_depth):
    data = data.flatten()
    if bit_depth == 10:
        return compressed_raw10(data)
    elif bit_depth == 12:
        return compressed_raw12(data)
    elif bit_depth == 14:
        return compressed_raw14(data)
    else:
        raise NotImplementedError(f'Decompression for {bit_depth}-bit')

# 将RGB数据转换位Bayer模式的原始数据
def rgb2raw(data, bit_depth, pattern, is_compress=False):
    print(data.shape)
    h, w, _ = data.shape

    # 创建一个形状为(h, w)的数据类型为根据位深度确定的无符号整数的零数组，用于存储拜耳模式数据
    bayer_array = np.zeros((h, w), dtype=np.uint16 if bit_depth > 8 else np.uint8)

    # 根据拜耳模式填充数据
    if pattern == "RGGB":
        bayer_array[0::2, 0::2] = data[0::2, 0::2, 0]
        bayer_array[0::2, 1::2] = data[0::2, 1::2, 1]
        bayer_array[1::2, 0::2] = data[1::2, 0::2, 1]
        bayer_array[1::2, 1::2] = data[1::2, 1::2, 2]
    elif pattern == "BGGR":
        bayer_array[0::2, 0::2] = data[0::2, 0::2, 2]
        bayer_array[0::2, 1::2] = data[0::2, 1::2, 1]
        bayer_array[1::2, 0::2] = data[1::2, 0::2, 1]
        bayer_array[1::2, 1::2] = data[1::2, 1::2, 0]
    elif pattern == "GRBG":
        bayer_array[0::2, 0::2] = data[0::2, 0::2, 1]
        bayer_array[0::2, 1::2] = data[0::2, 1::2, 0]
        bayer_array[1::2, 0::2] = data[1::2, 0::2, 2]
        bayer_array[1::2, 1::2] = data[1::2, 1::2, 1]
    elif pattern == "GBRG":
        bayer_array[0::2, 0::2] = data[0::2, 0::2, 1]
        bayer_array[0::2, 1::2] = data[0::2, 1::2, 2]
        bayer_array[1::2, 0::2] = data[1::2, 0::2, 0]
        bayer_array[1::2, 1::2] = data[1::2, 1::2, 1]
    else:
        # 如果输入的拜尔模式不被支持，则抛出异常
        raise ValueError("Unknown Bayer pattern: {}".format(pattern))
    if is_compress:
        # 如果要进行压缩，则调用compress函数进行压缩
        bayer_array = compress(bayer_array, bit_depth)

    return bayer_array