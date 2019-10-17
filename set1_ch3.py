from cryptopals_modules import *

buff = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
buff = bytes.fromhex(buff)

score, decrypted, key = single_xor_decrypt(buff)

print("Score : {}\nDecrypted msg: {}\nChar key: {}".format(score, decrypted, key))










