import cv2
import numpy as np

BT601_TV = np.array([[1.164, 0.000, 1.596],
                     [1.164, -0.392, -0.813],
                     [1.164, 2.017, 0.000]])

BT709_TV = np.array([[1.164, 0.000, 1.793],
                     [1.164, -0.213, -0.533],
                     [1.164, 2.112, 0.000]])

BT2020_TV = np.array([[1.164, 0.000, 1.679],
                      [1.164, -0.187, -0.650],
                      [1.164, 2.148, 0.000]])

BT601 = np.array([[1.000, 0.000, 1.402],
                  [1.000, -0.344, -0.714],
                  [1.000, 1.772, 0.000]])

BT709 = np.array([[1.000, 0.000, 1.574],
                  [1.000, -0.187, -0.468],
                  [1.000, 1.855, 0.000]])

BT2020 = np.array([[1.000, 0.000, 1.474],
                   [1.000, -0.164, -0.571],
                   [1.000, 1.881, 0.000]])


RGB601_TV = np.array([[0.2568, 0.5041, 0.0979],
                      [-0.1482, -0.2910, 0.4392],
                      [0.4392, -0.3678, -0.0714]])

RGB709_TV = np.array([[0.1826, 0.6142, 0.0620],
                      [-0.1006, -0.3386, 0.4392],
                      [0.4392, -0.3989, -0.0403]])

RGB2020_TV = np.array([[0.2257, 0.5828, 0.0501],
                       [-0.1225, -0.3166, 0.4392],
                       [0.4392, -0.4027, -0.0366]])

RGB601 = np.array([[0.299, 0.587, 0.114],
                   [-0.14713, -0.28886, 0.436],
                   [0.615, -0.51499, -0.10001]])

RGB709 = np.array([[0.1826, 0.6142, 0.0620],
                   [-0.1006, -0.3386, 0.4392],
                   [0.4392, -0.3989, -0.0403]])

RGB2020 = np.array([[0.2627, 0.6780, 0.0593],
                    [-0.13963, -0.36037, 0.5],
                    [0.5, -0.45979, -0.04021]])

# 函数 I444：将输入数据解析为 Y、U、V 三个平面
def I444(data, width, height):
    # 计算 Y 平面的大小
    y_plane_size = width * height
    # 计算 U 平面的大小，与 Y 平面相同
    u_plane_size = width * height

    # 从数据中提取 Y 平面，转换为 uint8 类型并重塑为(height, width)的形状
    Y = np.frombuffer(data[:y_plane_size], dtype=np.uint8).reshape((height, width))
    # 从数据中提取 U 平面，转换为 uint8 类型并重塑为(height, width)的形状
    U = np.frombuffer(data[y_plane_size:y_plane_size + u_plane_size], dtype=np.uint8).reshape((height, width))
    # 从数据中提取 V 平面，转换为 uint8 类型并重塑为(height, width)的形状
    V = np.frombuffer(data[y_plane_size + u_plane_size:], dtype=np.uint8).reshape((height, width))

    return Y, U, V

# 函数 NV24：将输入数据解析为 Y、U、V 三个平面
def NV24(data, width, height):
    # 计算一帧图像的大小
    frame_size = width * height
    # 提取 Y 数据
    y_data = data[:frame_size]
    # 提取 UV 数据
    uv_data = data[frame_size:]

    # 从 Y 数据中创建 Y 平面，转换为 uint8 类型并重塑为(height, width)的形状
    Y = np.frombuffer(y_data, dtype=np.uint8).reshape((height, width))
    # 从 UV 数据中隔一个元素提取 U 平面，转换为 uint8 类型并重塑为(height, width)的形状
    U = np.frombuffer(uv_data[0::2], dtype=np.uint8).reshape((height, width))
    # 从 UV 数据中隔一个元素提取 V 平面，转换为 uint8 类型并重塑为(height, width)的形状
    V = np.frombuffer(uv_data[1::2], dtype=np.uint8).reshape((height, width))

    return Y, U, V

# 函数 NV42：将输入数据解析为 Y、U、V 三个平面
def NV42(data, width, height):
    # 计算一帧图像的大小
    frame_size = width * height
    # 提取 Y 数据
    y_data = data[:frame_size]
    # 提取 UV 数据
    uv_data = data[frame_size:]

    # 从 Y 数据中创建 Y 平面，转换为 uint8 类型并重塑为(height, width)的形状
    Y = np.frombuffer(y_data, dtype=np.uint8).reshape((height, width))
    # 从 UV 数据中隔一个元素提取 V 平面，转换为 uint8 类型并重塑为(height, width)的形状
    V = np.frombuffer(uv_data[0::2], dtype=np.uint8).reshape((height, width))
    # 从 UV 数据中隔一个元素提取 U 平面，转换为 uint8 类型并重塑为(height, width)的形状
    U = np.frombuffer(uv_data[1::2], dtype=np.uint8).reshape((height, width))

    return Y, U, V

# 函数 AYUV：将输入数据解析为 Y、U、V 三个平面
def AYUV(data, width, height):
    # 将输入数据转换为 uint8 类型并重塑为(height, width, 4)的形状
    data = np.frombuffer(data, dtype=np.uint8).reshape(height, width, 4)
    # 提取 Y 平面
    Y = data[:, :, 1]
    # 提取 U 平面
    U = data[:, :, 2]
    # 提取 V 平面
    V = data[:, :, 3]

    return Y, U, V

# 函数 I422：将输入数据解析为 Y、U、V 三个平面
def I422(data, width, height):
    # 计算 Y 平面的大小
    y_plane_size = width * height
    # 计算 U 平面的大小，为 Y 平面的一半
    u_plane_size = width * height // 2

    # 从数据中提取 Y 平面，转换为 uint8 类型并重塑为(height, width)的形状
    Y = np.frombuffer(data[:y_plane_size], dtype=np.uint8).reshape((height, width))
    # 从数据中提取 U 平面，转换为 uint8 类型并重塑为(height, width)的形状
    U = np.frombuffer(data[y_plane_size:y_plane_size + u_plane_size], dtype=np.uint8).reshape((height, width))
    # 从数据中提取 V 平面，转换为 uint8 类型并重塑为(height, width)的形状
    V = np.frombuffer(data[y_plane_size + u_plane_size:], dtype=np.uint8).reshape((height, width))

    return Y, U, V

# 函数 NV16：将输入数据解析为 Y、U、V 三个平面
def NV16(data, width, height):
    # 计算一帧图像的大小
    frame_size = width * height
    # 提取 Y 数据
    y_data = data[:frame_size]
    # 提取 UV 数据
    uv_data = data[frame_size:]

    # 从 Y 数据中创建 Y 平面，转换为 uint8 类型并重塑为(height, width)的形状
    Y = np.frombuffer(y_data, dtype=np.uint8).reshape((height, width))
    # 从 UV 数据中隔一个元素提取 U 平面，重塑为(height, width//2)的形状
    U = np.frombuffer(uv_data[0::2], dtype=np.uint8).reshape((height, width // 2))
    # 从 UV 数据中隔一个元素提取 V 平面，重塑为(height, width//2)的形状
    V = np.frombuffer(uv_data[1::2], dtype=np.uint8).reshape((height, width // 2))

    return Y, U, V

# 函数 NV61：将输入数据解析为 Y、U、V 三个平面
def NV61(data, width, height):
    # 计算一帧图像的大小
    frame_size = width * height
    # 提取 Y 数据
    y_data = data[:frame_size]
    # 提取 UV 数据
    uv_data = data[frame_size:]

    # 从 Y 数据中创建 Y 平面，转换为 uint8 类型并重塑为(height, width)的形状
    Y = np.frombuffer(y_data, dtype=np.uint8).reshape((height, width))
    # 从 UV 数据中隔一个元素提取 V 平面，重塑为(height, width//2)的形状
    V = np.frombuffer(uv_data[0::2], dtype=np.uint8).reshape((height, width // 2))
    # 从 UV 数据中隔一个元素提取 U 平面，重塑为(height, width//2)的形状
    U = np.frombuffer(uv_data[1::2], dtype=np.uint8).reshape((height, width // 2))

    return Y, U, V

# 函数 YUYV：将输入数据解析为 Y、U、V 三个平面
def YUYV(data, width, height):
    # 从数据中隔一个元素提取 Y 平面，转换为 uint8 类型并重塑为(height, width)的形状
    Y = np.frombuffer(data[0::2], dtype=np.uint8).reshape((height, width))
    # 从数据中隔四个元素提取 V 平面，转换为 uint8 类型并重塑为(height, width//2)的形状
    V = np.frombuffer(data[3::4], dtype=np.uint8).reshape((height, width // 2))
    # 从数据中隔四个元素提取 U 平面，转换为 uint8 类型并重塑为(height, width//2)的形状
    U = np.frombuffer(data[1::4], dtype=np.uint8).reshape((height, width // 2))

    return Y, U, V

# 函数 UYVY：将输入数据解析为 Y、U、V 三个平面
def UYVY(data, width, height):
    # 从数据中隔一个元素提取 Y 平面，转换为 uint8 类型并重塑为(height, width)的形状
    Y = np.frombuffer(data[1::2], dtype=np.uint8).reshape((height, width))
    # 从数据中隔四个元素提取 V 平面，转换为 uint8 类型并重塑为(height, width//2)的形状
    V = np.frombuffer(data[2::4], dtype=np.uint8).reshape((height, width // 2))
    # 从数据中隔四个元素提取 U 平面，转换为 uint8 类型并重塑为(height, width//2)的形状
    U = np.frombuffer(data[0::4], dtype=np.uint8).reshape((height, width // 2))

    return Y, U, V

# 函数 I420：将输入数据解析为 Y、U、V 三个平面
def I420(data, width, height):
    # 计算一帧图像的大小
    frame_size = width * height
    # 计算 U、V 平面的大小，为 Y 平面的四分之一
    quarter_size = width * height // 4

    # 从数据中提取 Y 平面，转换为 uint8 类型并重塑为(height, width)的形状
    Y = np.frombuffer(data[0:frame_size], dtype=np.uint8).reshape((height, width))
    # 从数据中提取 U 平面，转换为 uint8 类型并重塑为(height//2, width//2)的形状
    U = np.frombuffer(data[frame_size:frame_size + quarter_size], dtype=np.uint8).reshape((height // 2, width // 2))
    # 从数据中提取 V 平面，转换为 uint8 类型并重塑为(height//2, width//2)的形状
    V = np.frombuffer(data[frame_size + quarter_size:], dtype=np.uint8).reshape((height // 2, width // 2))

    return Y, U, V

# 函数 YV12：将输入数据解析为 Y、U、V 三个平面
def YV12(data, width, height):
    # 计算一帧图像的大小
    frame_size = width * height
    # 计算 U、V 平面的大小，为 Y 平面的四分之一
    quarter_size = width * height // 4

    # 从数据中提取 Y 平面，转换为 uint8 类型并重塑为(height, width)的形状
    Y = np.frombuffer(data[0:frame_size], dtype=np.uint8).reshape((height, width))
    # 从数据中提取 V 平面，转换为 uint8 类型并重塑为(height//2, width//2)的形状
    V = np.frombuffer(data[frame_size:frame_size + quarter_size], dtype=np.uint8).reshape((height // 2, width // 2))
    # 从数据中提取 U 平面，转换为 uint8 类型并重塑为(height//2, width//2)的形状
    U = np.frombuffer(data[frame_size + quarter_size:], dtype=np.uint8).reshape((height // 2, width // 2))

    return Y, U, V

# 函数 I010：将输入数据解析为 Y、U、V 三个平面
def I010(data, width, height):
    # 计算一帧图像的大小
    frame_size = width * height
    # 计算 U、V 平面的大小，为 Y 平面的四分之一
    quarter_size = width * height // 4

    # 将数据转换为 uint16 类型
    data = np.frombuffer(data, dtype=np.uint16)

    # 从数据中提取 Y 平面，转换为 uint16 类型并重塑为(height, width)的形状
    Y = np.frombuffer(data[0:frame_size], dtype=np.uint16).reshape((height, width))
    # 从数据中提取 U 平面，转换为 uint16 类型并重塑为(height//2, width//2)的形状
    U = np.frombuffer(data[frame_size:frame_size + quarter_size], dtype=np.uint16).reshape((height // 2, width // 2))
    # 从数据中提取 V 平面，转换为 uint16 类型并重塑为(height//2, width//2)的形状
    V = np.frombuffer(data[frame_size + quarter_size:], dtype=np.uint16).reshape((height // 2, width // 2))

    return Y, U, V

# 函数 NV12：将输入数据解析为 Y、U、V 三个平面
def NV12(data, width, height):
    # 计算一帧图像的大小
    frame_size = width * height
    # 提取 Y 数据
    y_data = data[:frame_size]
    # 提取 UV 数据
    uv_data = data[frame_size:]

    # 从 Y 数据中创建 Y 平面，转换为 uint8 类型并重塑为(height, width)的形状
    Y = np.frombuffer(y_data, dtype=np.uint8).reshape((height, width))
    # 从 UV 数据中隔一个元素提取 U 平面，重塑为(height//2, width//2)的形状
    U = np.frombuffer(uv_data[0::2], dtype=np.uint8).reshape((height // 2, width // 2))
    # 从 UV 数据中隔一个元素提取 V 平面，重塑为(height//2, width//2)的形状
    V = np.frombuffer(uv_data[1::2], dtype=np.uint8).reshape((height // 2, width // 2))

    return Y, U, V

# 函数 NV21：将输入数据解析为 Y、U、V 三个平面
def NV21(data, width, height):
    # 计算一帧图像的大小
    frame_size = width * height
    # 提取 Y 数据
    y_data = data[:frame_size]
    # 提取 UV 数据
    uv_data = data[frame_size:]

    # 从 Y 数据中创建 Y 平面，转换为 uint8 类型并重塑为(height, width)的形状
    Y = np.frombuffer(y_data, dtype=np.uint8).reshape((height, width))
    # 从 UV 数据中隔一个元素提取 V 平面，重塑为(height//2, width//2)的形状
    V = np.frombuffer(uv_data[0::2], dtype=np.uint8).reshape((height // 2, width // 2))
    # 从 UV 数据中隔一个元素提取 U 平面，重塑为(height//2, width//2)的形状
    U = np.frombuffer(uv_data[1::2], dtype=np.uint8).reshape((height // 2, width // 2))

    return Y, U, V

# 函数 P101：将输入数据解析为 Y、U、V 三个平面
def P101(data, width, height):
    # 计算一帧图像的大小
    frame_size = width * height

    # 将数据转换为 uint16 类型
    data = np.frombuffer(data, dtype=np.uint16)
    # 提取 Y 数据
    y_data = data[:frame_size]
    # 提取 UV 数据
    uv_data = data[frame_size:]

    # 从 Y 数据中创建 Y 平面，转换为 uint16 类型并重塑为(height, width)的形状
    Y = np.frombuffer(y_data, dtype=np.uint16).reshape((height, width))
    # 从 UV 数据中隔一个元素提取 U 平面，转换为 uint16 类型并重塑为(height, width//2)的形状
    U = np.frombuffer(uv_data[0::2], dtype=np.uint16).reshape((height, width // 2))
    # 从 UV 数据中隔一个元素提取 V 平面，转换为 uint16 类型并重塑为(height, width//2)的形状
    V = np.frombuffer(uv_data[1::2], dtype=np.uint16).reshape((height, width // 2))

    return Y, U, V

#字典存储不同格式的解析函数
format_parsers = {
    'I444': I444,'NV24': NV24,'NV42': NV42,'AYUV': AYUV,'I422': I422,'NV16': NV16,
    'NV61': NV61,'YUYV': YUYV,'UYVY': UYVY,'I420': I420,'YV12': YV12,'I010': I010,'NV12': NV12,'NV21': NV21
}

# 根据文件路径、图像宽度、高度和格式获取 Y、U、V 三个平面
def get_Y_U_V(filepath, width, height, format):
    # 以二进制只读模式打开文件
    with open(filepath, 'rb') as f:

        # 读取文件内容
        data = f.read()

    # 根据格式调用相应的函数解析数据
    return format_parsers[format](data, width, height)

# 将 YUV 转换为 RGB
def matrix_rgb(y, u, v, standard, TV_type=False, inter=None):
    print(f"Applying interpolation method: {inter}")  # 调试信息

    # 根据 TV_type 的值进行不同的预处理
    if TV_type:
        y = y.astype(np.float32) - 16.0
        if standard == 'BT.601':
            m = BT601_TV
        elif standard == 'BT.709':
            m = BT709_TV
        else:
            m = BT2020_TV
    else:
        y = y.astype(np.float32)
        if standard == 'BT.601':
            m = BT601
        elif standard == 'BT.709':
            m = BT709
        else:
            m = BT2020

    u = u.astype(np.float32) - 128.0
    v = v.astype(np.float32) - 128.0

    if u.shape != y.shape:
        print(f"Resizing U and V planes using {inter}")  # 调试信息
        u = cv2.resize(u, (y.shape[1], y.shape[0]), interpolation=get_interpolation(inter))
        v = cv2.resize(v, (y.shape[1], y.shape[0]), interpolation=get_interpolation(inter))

    yuv = np.stack((y, u, v), axis=-1)
    rgb = np.dot(yuv, m.T)

    if TV_type:
        rgb[..., 0] = np.clip(rgb[..., 0], 16, 235)
        rgb[..., 1] = np.clip(rgb[..., 1], 16, 240)
        rgb[..., 2] = np.clip(rgb[..., 2], 16, 240)
    else:
        rgb = np.clip(rgb, 0, 255)

    rgb = rgb.astype(np.uint8)
    return rgb

# 根据传入的参数获取对应的 OpenCV 插值方法
def get_interpolation(inter):
    return {
        'nearest': cv2.INTER_NEAREST,  # 最近邻插值
        'linear': cv2.INTER_LINEAR,    # 双线性插值
        'cubic': cv2.INTER_CUBIC,  # 三次插值
        'area': cv2.INTER_AREA,  # 区域插值
        'linear_exact': cv2.INTER_LINEAR_EXACT,  # 精确双线性插值
        'nearest_exact': cv2.INTER_NEAREST_EXACT  # 精确最近邻插值
    }.get(inter, cv2.INTER_NEAREST)

# 获取 YUV 图像并转换为 RGB
def get_yuv_rgb(filepath, parameters):
    # 从参数中获取图像宽度
    width = parameters['width']

    # 从参数中获取图像高度
    height = parameters['height']

    # 从参数中获取 YUV 格式
    format = parameters['yuv_pattern']

    # 从参数中获取标准
    standard = parameters['standard']

    # 从参数中获取是否为 TV 范围标志
    TV_type = parameters['TV_range']

    # 从参数中获取插值方法
    interpolation_key = parameters.get('interpolation', 'nearest')  # 提供默认值

    # 检查插值方法键是否为字符串，并且是否在 get_interpolation 中定义
    if not isinstance(interpolation_key, str):
        raise ValueError("Interpolation key must be a string.")

    interpolation_methods = {
        'nearest': cv2.INTER_NEAREST,  # 最近邻插值
        'linear': cv2.INTER_LINEAR,    # 双线性插值
        'cubic': cv2.INTER_CUBIC,  # 三次插值
        'area': cv2.INTER_AREA,  # 区域插值
        'linear_exact': cv2.INTER_LINEAR_EXACT,  # 精确双线性插值
        'nearest_exact': cv2.INTER_NEAREST_EXACT  # 精确最近邻插值
    }

    if interpolation_key not in interpolation_methods:
        raise ValueError(f"Interpolation key '{interpolation_key}' is not recognized. Choose from {list(interpolation_methods.keys())}.")

    # 获取 Y、U、V 三个平面
    y, u, v = get_Y_U_V(filepath, width, height, format)

    # 如果参数中不包含 Y，将 Y 平面填充为 128
    if not parameters.get('Y', False):
        y = np.full(y.shape, 128)

    # 如果参数中不包含 Cb（U），将 U 平面填充为 128
    if not parameters.get('Cb', False):
        u = np.full(u.shape, 128)

    # 如果参数中不包含 Cr（V），将 V 平面填充为 128
    if not parameters.get('Cr', False):
        v = np.full(v.shape, 128)

    # 打印插值方法以进行调试
    print(f"Using interpolation method: {interpolation_key}")

    # 将 YUV 转换为 RGB
    return matrix_rgb(y, u, v, standard, TV_type, interpolation_key)

# 将 RGB 转换为 NV24 格式
def RGB2NV24(y, u, v):
    # 获取 Y 平面的高度和宽度
    h, w = y.shape

    # 将 Y 平面展平为一维数组
    y = y.flatten()

    # 创建一个二维数组用于存储 UV 平面
    uv = np.zeros((h, w * 2))

    # 将 U 平面存储在 uv 的偶数位置
    uv[:, ::2] = u

    # 将 V 平面存储在 uv 的奇数位置
    uv[:, 1::2] = v

    # 将 uv 展平为一维数组
    uv = uv.flatten()

    # 将 Y 平面和 UV 平面连接起来
    return np.concatenate((y, uv))

# 将 RGB 转换为 NV42 格式
def RGB2NV42(y, u, v):
    # 获取 Y 平面的高度和宽度
    h, w = y.shape

    # 将 Y 平面展平为一维数组
    y = y.flatten()

    # 创建一个二维数组用于存储 UV 平面
    uv = np.zeros((h, w * 2))

    # 将 V 平面存储在 uv 的偶数位置
    uv[:, ::2] = v

    # 将 U 平面存储在 uv 的奇数位置
    uv[:, 1::2] = u

    # 将 uv 展平为一维数组
    uv = uv.flatten()

    # 将 Y 平面和 UV 平面连接起来
    return np.concatenate((y, uv))

# 将 RGB 转换为 I422 格式
def RGB2I422(y, u, v):
    # 将 Y 平面展平为一维数组
    y = y.flatten()

    # 将 U 平面展平为一维数组
    u = u.flatten()

    # 将 V 平面展平为一维数组
    v = v.flatten()

    # 将 Y 平面、U 平面和 V 平面连接起来
    return np.concatenate((y, u, v))

# 将 RGB 转换为 NV16 格式
def RGB2NV16(y, u, v):
    # 获取 Y 平面的高度和宽度
    h, w = y.shape

    # 将 Y 平面展平为一维数组
    y = y.flatten()

    # 创建一个二维数组用于存储 UV 平面
    uv = np.zeros((h, w))

    # 将 U 平面存储在 uv 的偶数位置
    uv[:, ::2] = u

    # 将 V 平面存储在 uv 的奇数位置
    uv[:, 1::2] = v

    # 将 uv 展平为一维数组
    uv = uv.flatten()

    # 将 Y 平面和 UV 平面连接起来
    return np.concatenate((y, uv))

# 将 RGB 转换为 NV61 格式
def RGB2NV61(y, u, v):
    # 获取 Y 平面的高度和宽度
    h, w = y.shape

    # 将 Y 平面展平为一维数组
    y = y.flatten()

    # 创建一个二维数组用于存储 UV 平面
    uv = np.zeros((h, w))

    # 将 V 平面存储在 uv 的偶数位置
    uv[:, ::2] = v

    # 将 U 平面存储在 uv 的奇数位置
    uv[:, 1::2] = u

    # 将 uv 展平为一维数组
    uv = uv.flatten()

    # 将 Y 平面和 UV 平面连接起来
    return np.concatenate((y, uv))

# 将 RGB 转换为 YUYV 格式
def RGB2YUYV(y, u, v):
    # 获取 Y 平面的高度和宽度
    h, w = y.shape

    # 创建一个二维数组用于存储 YUV 平面
    yuv = np.zeros((h, w * 2))

    # 将 Y 平面的偶数行存储在 yuv 的 0、4、8...位置
    yuv[:, 0::4] = y[:, ::2]

    # 将 U 平面存储在 yuv 的 1、5、9...位置
    yuv[:, 1::4] = u

    # 将 Y 平面的奇数行存储在 yuv 的 2、6、10...位置
    yuv[:, 2::4] = y[:, 1::2]

    # 将 V 平面存储在 yuv 的 3、7、11...位置
    yuv[:, 3::4] = v

    # 将 yuv 展平为一维数组
    return yuv.flatten()

# 将 RGB 转换为 UYVY 格式
def RGB2UYVY(y, u, v):
    # 获取 Y 平面的高度和宽度
    h, w = y.shape

    # 创建一个二维数组用于存储 YUV 平面
    yuv = np.zeros((h, w * 2))

    # 将 U 平面存储在 yuv 的 0、4、8...位置
    yuv[:, 0::4] = u

    # 将 Y 平面的偶数行存储在 yuv 的 1、5、9...位置
    yuv[:, 1::4] = y[:, ::2]

    # 将 V 平面存储在 yuv 的 2、6、10...位置
    yuv[:, 2::4] = v

    # 将 Y 平面的奇数行存储在 yuv 的 3、7、11...位置
    yuv[:, 3::4] = y[:, 1::2]

    # 将 yuv 展平为一维数组
    return yuv.flatten()

# 将 RGB 转换为 YV12 格式
def RGB2YV12(y, u, v):
    # 将 Y 平面展平为一维数组
    y = y.flatten()

    # 将 U 平面展平为一维数组
    u = u.flatten()

    # 将 V 平面展平为一维数组
    v = v.flatten()

    # 将 Y 平面、V 平面和 U 平面连接起来
    return np.concatenate((y, v, u))

# 将 RGB 转换为 NV12 格式
def RGB2NV12(y, u, v):
    # 获取 U 平面的高度和宽度
    h, w = u.shape

    # 将 Y 平面展平为一维数组
    y = y.flatten()

    # 创建一个二维数组用于存储 UV 平面
    uv = np.zeros((h, w * 2))

    # 将 U 平面存储在 uv 的偶数位置
    uv[:, ::2] = u

    # 将 V 平面存储在 uv 的奇数位置
    uv[:, 1::2] = v

    # 将 uv 展平为一维数组
    uv = uv.flatten()

    # 将 Y 平面和 UV 平面连接起来
    return np.concatenate((y, uv))

# 将 RGB 转换为 NV21 格式
def RGB2NV21(y, u, v):
    # 获取 U 平面的高度和宽度
    h, w = u.shape

    # 将 Y 平面展平为一维数组
    y = y.flatten()

    # 创建一个二维数组用于存储 UV 平面
    uv = np.zeros((h * 2, w))

    # 将 V 平面存储在 uv 的偶数位置
    uv[:, ::2] = v

    # 将 U 平面存储在 uv 的奇数位置
    uv[:, 1::2] = u

    # 将 uv 展平为一维数组
    uv = uv.flatten()

    # 将 Y 平面和 UV 平面连接起来
    return np.concatenate((y, uv))

# 将 RGB 转换为 I420 格式
def RGB2I420(y, u, v):
    # 将 Y 平面展平为一维数组
    y = y.flatten()

    # 将 U 平面展平为一维数组
    u = u.flatten()

    # 将 V 平面展平为一维数组
    v = v.flatten()

    # 将 Y 平面、U 平面和 V 平面连接起来
    return np.concatenate((y, u, v))

# 将RGB转换为yuv格式
def rgb2yuv(data, head, style, standard, TV_type):
    # 如果是TV类型
    if TV_type:
        #设置偏移量
        offset = np.array([16.0, 128.0, 128.0])
        # 根据不同的标准选择不同的转换矩阵
        if standard == 'BT.601':
            m = RGB601_TV
        elif standard == 'BT.709':
            m = RGB709_TV
        else:
            m = RGB2020_TV
    else:
        # 如果不是TV类型，设置不同的偏移量
        offset = np.array([0.0, 128.0, 128.0])
        # 根据不同的标准选择不同的转换矩阵
        if standard == 'BT.601':
            m = RGB601
        elif standard == 'BT.709':
            m = RGB709
        else:
            m = RGB2020
    # height, width, channels = data.shape
    # data = data.reshape(-1, channels)

    # 如果数据类型是 uint16，则将其归一化到 0-255 范围内
    if data.dtype == np.uint16:
        cv2.normalize(data, None, 0, 255, cv2.NORM_MINMAX)

    # 将RGB数据转换位YUV数据
    yuv = np.dot(data, m) + offset

    # 将YUV数据重新调整为原来的形状
    yuv = yuv.reshape(data.shape)

    # 获取Y、U、V三个平面
    print(yuv.shape)
    y = yuv[..., 0]
    u = yuv[..., 1]
    v = yuv[..., 2]

    # 根据不同的格式进行不同的处理
    if head == '4:4:4':
        if style == 'I444':
            return np.concatenate((y, u, v))
        elif style == 'NV24':
            return RGB2NV24(y, u, v)
        elif style == 'NV42':
            return RGB2NV42(y, u, v)

    elif head == '4:2:2':
        # 对U、V平面进行采样
        u = (u[:, ::2] + u[:, 1::2]) // 2
        v = (v[:, ::2] + v[:, 1::2]) // 2
        height, width = y.shape
        # 断言下采样后的形状正确
        assert u.shape == (height, width // 2)
        assert v.shape == (height, width // 2)
        # 转换格式
        if style == 'I422':
            return RGB2I422(y, u, v)
        elif style == 'NV16':
            return RGB2NV16(y, u, v)
        elif style == 'NV61':
            return RGB2NV61(y, u, v)
        elif style == 'YUYV':
            return RGB2YUYV(y, u, v)
        elif style == 'UYVY':
            return RGB2UYVY(y, u, v)

    elif head == '4:2:0':
        # 对U、V平面进行采样
        u = (u[::2, ::2] + u[::2, 1::2] + u[1::2, ::2] + u[1::2, 1::2]) // 4
        v = (v[::2, ::2] + v[::2, 1::2] + v[1::2, ::2] + v[1::2, 1::2]) // 4
        height, width = y.shape
        # 断言下采样后的形状正确
        assert u.shape == (height // 2, width // 2)
        assert v.shape == (height // 2, width // 2)
        # 转换格式
        if style == 'I420':
            return RGB2I420(y, u, v)
        elif style == 'YV12':
            return RGB2YV12(y, u, v)
        elif style == 'NV12':
            return RGB2NV12(y, u, v)
        elif style == 'NV21':
            return RGB2NV21(y, u, v)

    else:
        raise ValueError("error")
