
#1. bit_length
n = -37
print("bit_length:",n.bit_lengh())  # 6

#2. bit_count
n = 19
print("bit_count:",n.bit_count())  # 3

#3. to_bytes
x = 1024
print("to_bytes (big):",x.to_bytes(2, byteorder='big')) 

x = 1000
min_bytes = (x.bit_length()+7)//8
print("to_bytes (little:)", x.to_bytes(min_bytes, byteorder='little'))

#4. from_bytes
print("from_bytes (big):", int.from_bytes(b'\x00\x10', byteorder='big'))
print("from_bytes (signed):", int.from_bytes(b'\x00\x10', byteorder='big', signed=True))

#5. as_integer_ratio
print("as_integer_ratio:", (5).as_integer_ratio())

#6. is_integer
print("is_integer:", (5).is_integer())