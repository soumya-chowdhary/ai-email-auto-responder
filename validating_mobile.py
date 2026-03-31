def validate_mobile(number):
    if len(number) != 10:
        return "Invalid Mobile Number"
    if not number.isdigit():
        return "Invalid Mobile Number"
    if number[0] not in ['6', '7', '8', '9']:
        return "Invalid Mobile Number"
    return "Valid Mobile Number"

number = input("Enter mobile number: ")
print(validate_mobile(number))
