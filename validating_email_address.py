def validate_email(email):
    if email.count('@') != 1:
        return "Invalid Email Address"
    username, domain = email.split('@')
    if len(username) == 0 or len(domain) == 0:
        return "Invalid Email Address"
    if '.' not in domain:
        return "Invalid Email Address"
    if domain.startswith('.') or domain.endswith('.'):
        return "Invalid Email Address"
    return "Valid Email Address"

email = input("Enter email address: ")
print(validate_email(email))
