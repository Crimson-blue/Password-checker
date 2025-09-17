# 🔐 Password Strength Checker

A simple yet educational **Password Strength Checker** written in Python.  

This tool evaluates the strength of a password based on:
- ✅ Length  
- ✅ Character variety (uppercase, lowercase, digits, symbols)  
- ✅ Presence of common dictionary words  
- ✅ Estimated entropy bits (inspired by [zxcvbn](https://github.com/dropbox/zxcvbn))  

It’s a fun little project to learn about **regex**, **pattern matching**, and **security hygiene**.

---

## 🚀 Features
- Checks if a password includes:
  - Uppercase letters
  - Lowercase letters
  - Digits
  - Symbols
- Warns if it contains common weak words (like `password123`, `12345678`, etc.)
- Estimates password entropy (bits of randomness).
- Rates passwords as **Weak** / **Moderate** / **Strong** / **Very Strong**.
- Interactive prompt: test as many passwords as you want in one run.

---

## 📦 Requirements
This project uses built-in Python libraries only:

- `math`
- `re`

No external dependencies required!

---

## 🛠️ Installation & Usage

1. Clone or download this repository.
2. Save the script as `passchecker.py`.
3. Run it with Python:
