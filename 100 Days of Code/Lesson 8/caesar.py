# TODO-1: Import and print the logo from art.py when the program starts.
# import art
# print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    output_text = ""

    if direction not in ('encode', 'decode'):
        print('Enter a valid direction')
        return 
    else:

        if direction == "decode":
                shift *= -1
        
        for letter in text:
            

            shifted_position = alphabet.index(letter) + shift
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        print(f"Here is the {direction}d result: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?


# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
caesar()



