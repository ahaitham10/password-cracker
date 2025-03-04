import itertools
import string

def dictionary_attack(username, password, dictionary):
    print(f"Attempting dictionary attack for user: {username}")
    for word in dictionary:
        if word.strip() == password:
            print(f"Success! Password found: {word}")
            return True
    print("Dictionary attack failed.")
    return False

def brute_force_attack(password):
    print("Starting brute force attack...")
    chars = string.ascii_letters  # A-Z, a-z
    for attempt in itertools.product(chars, repeat=5):
        attempt = ''.join(attempt)
        if attempt == password:
            print(f"Success! Password cracked: {attempt}")
            return True
    print("Brute force attack failed.")
    return False

def main():
    username = input("Enter username: ")
    password = "abcDE"  # Hardcoded correct password
    
    dictionary = ["password", "12345", "admin", "letmein", "qwerty", "abcde"]  # Example dictionary
    
    if not dictionary_attack(username, password, dictionary):
        brute_force_attack(password)

if __name__ == "__main__":
    main()
