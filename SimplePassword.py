# SimplePassword.py

def is_valid_password(password, min_length=8):
    if len(password) >= min_length:
        return True
    else:
        return False

# Get input from user
user_password = input("Enter your password: ")

# Validate password
if is_valid_password(user_password):
    print("✅ Password is valid.")
else:
    print("❌ Password is too short. It must be at least 8 characters long.")
