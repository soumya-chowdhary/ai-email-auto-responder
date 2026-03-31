def validate_password(password):
    if len(password) < 8:
        return "Invalid Password"
    if not any(ch.isupper() for ch in password):
        return "Invalid Password"
    if not any(ch.islower() for ch in password):
        return "Invalid Password"
    if not any(ch.isdigit() for ch in password):
        return "Invalid Password"
    if not any(ch in "@#$%&*" for ch in password):
        return "Invalid Password"
    return "Valid Password"

password = input("Enter password: ")
print(validate_password(password))
