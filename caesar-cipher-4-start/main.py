import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    cipher_text = ""
    if direction=="decode":
        shift*= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)  
            cipher_text+=alphabet[position+shift]
        else:
            cipher_text+=char
    print(f"Here's the {direction}d result: {cipher_text}")
    

print(art.logo)
gamestatus=True

while gamestatus==True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    caesar(text, shift, direction)
    result=input("Would you like to go again? Type yes or no")
    if result=="no":
        gamestatus=False
print("Goodbye")