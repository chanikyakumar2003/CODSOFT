import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    try:
        desired_length = int(input("Enter the desired password length: "))
        if desired_length <= 0:
            print("Please enter a positive integer.")
            return

        generated_password = generate_password(desired_length)
        print(f"Generated password: {generated_password}")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")
if __name__ == "__main__":
    main()
