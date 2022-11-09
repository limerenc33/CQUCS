import struct
import json

# 需要传输的值
value = ['2018993', 'Andy Hu', 26, 'male', True, 175.3, 78, [12, 99, 77]]
print(value)
# 配合json将数据打包，同时保留其数据结构
strings = json.dumps(value)

# 将json的str兑现转换成bytes，以方便struct压缩
bytesarray = bytes(strings, encoding='utf8')
# 获取bytesarray的长度
bytes_len = len(bytesarray)

# 打包
packed_data = struct.pack('{0}s'.format(bytes_len), bytesarray)
#解包
unpacked_data = struct.unpack('{0}s'.format(bytes_len), packed_data)

# 读出数据
unpacked_data_x = unpacked_data[0]
# json读取数据结构
unpacked_data = json.loads(unpacked_data_x)
print(unpacked_data)