from cryptopals_modules import xor_buffers

buff1 = bytes.fromhex('1c0111001f010100061a024b53535009181c')
buff2 = bytes.fromhex('686974207468652062756c6c277320657965')

result = xor_buffers(buff1, buff2)
print("Byte result: {}".format(result))
print("Hex result: {}".format(result.hex()))
