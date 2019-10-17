import struct

def xor_buffers(buffer1, buffer2):
	
	if len(buffer1) != len(buffer2):
		print("Supplied buffers are not equal")
		return false

	result = b''

	for count in range(len(buffer1)):
		result += bytes([buffer1[count] ^ buffer2[count]])

	return result

def scorer(buff):
	
	"""
	let x = character

	x is letter (lower/upper character) => 3 points
	x is number => 1 point
	x is special char => -2 points
	
	"""

	score = 0

	for item in buff:
		if bytes([item]).isalpha():
			score += 3
		elif item > 31 and item < 128:
			score += 1
		else:
			score -= 2

	return score

def single_xor_decrypt(buff, start_range = 32, end_range = 127):

	score = 0
	ret_buff = b''
	ret_key = None

	for count in range(start_range, end_range+1):
		key = bytes([count])*len(buff)
		
		xor_buff = xor_buffers(buff, key)

		new_score = scorer(xor_buff)

		if score < new_score:
			score = new_score
			ret_buff = xor_buff
			ret_key = bytes([count])

	return score, ret_buff, ret_key










