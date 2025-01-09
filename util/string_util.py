from random import choice

# function definition for generating a random string of length (n) containing only the provided characters
def generate_random_string(allowable_chars, length):
    return ''.join(choice(allowable_chars) for i in range(length))
# end of generate_random_string