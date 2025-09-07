from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1#for backword movement while running in decode function

    for letter in original_text:
        if letter not in alphabet:
            output_text+=letter
        else:

            shifted_position = alphabet.index(letter) + shift_amount   #ex:letter=z,shift_amount=9,shifted position will be 34
            shifted_position %= len(alphabet)    #to maintain the range b/w 0-25 ex:34%25=9,so the crt shift is also maintained for these error type.
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    result=input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()
    if result=="no":
       should_continue=False
       print("GoodBye")


