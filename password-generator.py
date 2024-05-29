import random

def generate_password():
    cap_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', '?', '£', '^', '_', '-', '=', '{', '}', '[', ']', '|', '~', '<', '>', ',', '.', ':', "'", '"', '/', '\\']

    print("Welcome to the PyPassword Generator!")
    nr_characters = int(input("How many characters would you like in your password?\n"))

    if nr_characters < 4:
        print("Password length should be at least 4 to include one of each type of character.")
    else:
        # Ensure at least one of each type
        char_left = nr_characters - 4
        nr_cap_letters = 1 + random.randint(0, char_left)
        char_left -= (nr_cap_letters - 1)
        nr_small_letters = 1 + random.randint(0, char_left)
        char_left -= (nr_small_letters - 1)
        nr_numbers = 1 + random.randint(0, char_left)
        char_left -= (nr_numbers - 1)
        nr_symbols = char_left + 1

        # Generate the password
        password_list = []
        for _ in range(nr_cap_letters):
            password_list.append(random.choice(cap_letters))

        for _ in range(nr_small_letters):
            password_list.append(random.choice(small_letters))

        for _ in range(nr_symbols):
            password_list.append(random.choice(symbols))

        for _ in range(nr_numbers):
            password_list.append(random.choice(numbers))

        # Shuffle the password list to ensure randomness
        random.shuffle(password_list)

        # Convert the list to a string
        password = "".join(password_list)

        print(f"Your generated password is: {password}")

while True:
    generate_password()
    rerun = input("Do you want to generate another password? (yes/no, default yes): ").strip().lower()
    if rerun == '' or rerun == 'yes':
        continue
    else:
        break

print("Thank you for using the Password Generator!")
