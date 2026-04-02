import re


def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("- Too short (minimum 8 characters).")

    # 2. Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("- Missing uppercase letters.")

    # 3. Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("- Missing lowercase letters.")

    # 4. Check for numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("- Missing numbers.")

    # 5. Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("- Missing special characters (e.g., !@#$%).")

    # Determine final strength
    print(f"\nAnalyzing Password: {'*' * len(password)}")
    if score == 5:
        print("Status: [STRONG] ✅")
        print("Your password meets all security criteria.")
    elif score >= 3:
        print("Status: [MODERATE] ⚠️")
        print("Feedback to improve:")
        for f in feedback: print(f)
    else:
        print("Status: [WEAK] ❌")
        print("Feedback to improve:")
        for f in feedback: print(f)
    print("-" * 30)


if __name__ == "__main__":
    print("=== Security Solution: Password Strength Analyzer ===")
    test_weak = input("Enter a WEAK password to test: ")
    check_password_strength(test_weak)

    test_strong = input("Enter a STRONG password to test: ")
    check_password_strength(test_strong)