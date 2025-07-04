import re

def check_password_strength(password):
    score = 0
    feedback = []
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔸 Use at least 8 characters.")
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔸 Include lowercase letters.")
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("🔸 Add some uppercase letters.")
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔸 Add numbers for extra strength.")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("🔸 Try using symbols like !, @, #, etc.")
    if score == 5:
        strength = "💪 Strong"
    elif 3 <= score < 5:
        strength = "🙂 Medium"
    else:
        strength = "😬 Weak"
    return strength, feedback
password = input("Enter a password to check: ")
strength, suggestions = check_password_strength(password)
print(f"\nPassword Strength: {strength}")
if suggestions:
    print("Suggestions:")
    for tip in suggestions:
        print(tip)