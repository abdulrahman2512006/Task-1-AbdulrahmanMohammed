import re

def check_password_strength(password):
    length = len(password)

    if length < 8:
        return "WEAK   - Password must be at least 8 characters."

    has_upper  = any(c.isupper() for c in password)
    has_lower  = any(c.islower() for c in password)
    has_digit  = any(c.isdigit() for c in password)
    has_symbol = any(c in "!@#$%^&*()_+-=[]{}|;':\",./<>?" for c in password)

    score = 0
    if length >= 8:  score += 1
    if length >= 12: score += 1
    if has_upper:    score += 1
    if has_lower:    score += 1
    if has_digit:    score += 1
    if has_symbol:   score += 1

    if score <= 3: return "WEAK   - Add uppercase, numbers, and symbols."
    if score <= 5: return "MEDIUM - Good, but try adding more variety."
    return                "STRONG - Excellent password!"

def analyze_password(password):
    print("\nResult  :", check_password_strength(password))
    print("\n--- Analysis ---")
    print(f"Length    : {len(password)} chars")
    print(f"Uppercase : {'YES' if any(c.isupper() for c in password) else 'NO'}")
    print(f"Lowercase : {'YES' if any(c.islower() for c in password) else 'NO'}")
    print(f"Digit     : {'YES' if any(c.isdigit() for c in password) else 'NO'}")
    print(f"Symbol    : {'YES' if any(c in '!@#$%^&*()_+-=[]{}|;\':\",./<>?' for c in password) else 'NO'}")

def main():
    print("========================================")
    print("  DecodeLabs - Password Strength Checker")
    print("========================================")

    while True:
        password = input("\nEnter password (or 'quit' to exit): ")

        if password.lower() == "quit":
            break

        analyze_password(password)

    print("\nGoodbye! Stay secure. - DecodeLabs")

if __name__ == "__main__":
    main()
