# Perfect Match Dating App
A Python practice project for a dating app registration and intelligent matching system.

## 🌟 Core Features
1. **User Registration System**
   Collects comprehensive user profile information with strict input validation:
   - String validation (minimum length for nickname: 2 characters)
   - Numeric validation (age: 18-80, valid number format for height/income)
   - Option validation (predefined choices for gender, occupation, and email consent)

2. **Secure Login Authentication**
   Verifies user credentials after registration. Passwords are stored in lowercase and verified case-insensitively.

3. **Ideal Match Recommendation**
   Filters matches based on the user's specific preferences (gender, height/age/income range, occupation):
   - **Tier 1**: Annual income ≤ $100,000 → 3 ideal matches recommended
   - **Tier 2**: Annual income > $100,000 → 5 ideal matches + exclusive tailored services

4. **Similar Match Fallback**
   If no exact matches are found, users can trigger a "similar match" search via the `more` option, which recommends profiles close to the user's own attributes.

## 📋 Prerequisites
- Python 3.6 or higher
- No external libraries required (uses only Python built-in functions)

## 🚀 How to Run
1. Open the `dating_app` folder in your IDE (VS Code / PyCharm)
2. Open the terminal (Shortcut: `Ctrl + ` )
3. Run the main script with the following command:
   ```bash
   python 20260220datingapp.py

## Project Structure