import random

def generate_random_password():
    length = int(input("Enter password length: "))
    alphabets_count = int(input("Enter alphabets count in password: "))
    digits_count = int(input("Enter digits count in password: "))
    special_characters_count = int(input("Enter special characters count in password: "))
    characters_count = alphabets_count + digits_count + special_characters_count
    if characters_count > length:
        print("Characters total count is greater than the password length")
        return
    password = []
def alphabets(alphabets):
    for i in range(alphabets_count):
        password.append(random.choice(alphabets))
        return password
def digits():
    for i in range(digits_count):
        password.append(random.choice(digits))
        return password
def special():
    for i in range(special_characters_count):
        password.append(random.choice(special_characters))
        return special
def character():
    if characters_count < length:
        random.shuffle(characters)
        for i in range(length - characters_count):
            password.append(random.choice(characters))
            return character
    password = []
    random.shuffle(password)
    print("".join(password))