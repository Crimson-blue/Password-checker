import math
import re

COMMON_WORDS = {"password", "123456789", "password123", "12345678", "iloveyou"}

def password_strength(password: str):
    """Evaluate the strength of a password and return a report dict."""

    report = {
        "length": len(password),
        "has_upper": bool(re.search(r"[A-Z]", password)),
        "has_lower": bool(re.search(r"[a-z]", password)),
        "has_digit": bool(re.search(r"[0-9]", password)),
        "has_symbol": bool(re.search(r"[^A-Za-z0-9]", password)),
        "contains_common_word": any(word in password.lower() for word in COMMON_WORDS)
    }

    # Rule-based scoring
    score = 0
    if report["length"] >= 8: score += 1
    if report["length"] >= 12: score += 1
    if report["has_upper"]: score += 1
    if report["has_lower"]: score += 1
    if report["has_digit"]: score += 1
    if report["has_symbol"]: score += 1
    if report["contains_common_word"]: score -= 2  # big penalty

    # Entropy estimation
    charset_size = 0
    if report["has_lower"]: charset_size += 26
    if report["has_upper"]: charset_size += 26
    if report["has_digit"]: charset_size += 10
    if report["has_symbol"]: charset_size += 32  # estimated printable symbols

    entropy_bits = 0
    if charset_size > 0:
        entropy_bits = round(math.log2(charset_size) * report["length"], 2)

    # Strength classification
    if score <= 2 or entropy_bits < 28:
        strength = "Weak"
    elif score <= 4 or entropy_bits < 36:
        strength = "Moderate"
    elif score <= 6 or entropy_bits < 60:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return {
        "report": report,
        "score": score,
        "entropy_bits": entropy_bits,
        "strength": strength
    }

if __name__ == "__main__":
    print("\n--- Password Strength Checker ---")
    while True:
        user_pwd = input("Enter a password to check (or press Enter to quit): ")
        if not user_pwd:
            print("Exiting")
            break
        result = password_strength(user_pwd)
        print("\nReport:", result["report"])
        print("Score:", result["score"])
        print("Entropy (bits):", result["entropy_bits"])
        print("Strength:", result["strength"])
        print("-" * 50)