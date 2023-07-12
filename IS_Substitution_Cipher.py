pip install caesarcipher

from caesarcipher import CaesarCipher

text = input("Enter the text: ")
offset = int(input("Enter the offset: "))

cipher = CaesarCipher(text, offset=offset)
encoded_text = cipher.encoded
decoded_text = cipher.decoded

print("Encoded text:", encoded_text)
print("Decoded text:",decoded_text)
