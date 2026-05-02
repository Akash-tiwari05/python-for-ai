import string

class Tokenization:

    def __init__(self):
        # Create mapping for A-Z (0-25)
        self.tokens = {letter: index for index, letter in enumerate(string.ascii_uppercase)}

        # Add mapping for a-z (26-51)
        self.tokens.update({letter: index + 26 for index, letter in enumerate(string.ascii_lowercase)})

        self.reverse_tokens = {index: letter for letter, index in self.tokens.items()}

    def encoder(self, key):
        if key and key[0] in self.tokens:
            return self.tokens[key[0]]
        else:
            raise ValueError("Invalid Key...")
    
    def decoder(self, value):
        if value in self.reverse_tokens:
            return self.reverse_tokens.get(value)
        else:
            raise ValueError("Value is Invalid! Please re-check your input.")
    

tokens = Tokenization()
result = tokens.encoder("a")
print(result)

getKey = tokens.decoder(28)
print(getKey)