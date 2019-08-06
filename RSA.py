# Ben Ryan
# RSA Encryption

import random
import math

def main():
	#using small sample numbers 
	p = 17
	q = 11
	
	n = p * q

	t = (p-1) * (q-1)
		
	e = getCoprime(t)

	d = getPrivateKey(e, t)
	
	public = (n, e)
	private = (n, d)

	ciphertext = applyKey(public, input("Enter text to be encrypted\n"))
	plaintext = applyKey(private, ciphertext)
	
	print("\n Public Key:", public, 
			"\n Private Key:", private, 
			"\n Ciphertext:", ciphertext, 
			"\n Plaintext (after decryption):", ''.join(plaintext))

#gets random value for e that is coprime with t
def getCoprime(t):
	e = random.randrange(1, t)

	while math.gcd(e, t) != 1:
		e = random.randrange(1, t)
	
	return e
	
#gets first possible d
def getPrivateKey(e, n):
	for d in range(0, n):
		if (e*d) % n == 1 and e != d:
			return d

#applies key to plain or cipher text
def applyKey(key, text):
	n, ed = key

	convertedText = []
	for element in text:
		numVal = ord(element)
		convertedEl = chr((numVal ** ed) % n)
		convertedText.append(convertedEl)

	return convertedText

if __name__ == '__main__':
	main()
	