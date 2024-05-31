import random
#Generate a random password of the given length.
def generate_password(length):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = lowercase.upper()
    digits = '0123456789'
    special_chars = '!@#$%^&*()_+-=[]{}|;:\',<.>/?`~'
    all_chars = lowercase + uppercase + digits + special_chars

    min_uppercase = 2
    min_lowercase = 2
    min_digits = 2
    min_special = 2

    password = (random.sample(uppercase, min_uppercase) +
                random.sample(lowercase, min_lowercase) +
                random.sample(digits, min_digits) +
                random.sample(special_chars, min_special) +
                random.sample(all_chars, length - (min_uppercase + min_lowercase + min_digits + min_special)))
    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    length = int(input("Enter password length(Better password_length > 15): "))
    num_passwords = int(input("Enter number of passwords to generate: "))

    for _ in range(num_passwords):
        password = generate_password(length)
        print(password)
