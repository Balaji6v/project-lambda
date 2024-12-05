import re

# a) Validate email address
def is_valid_email(email):
    return bool(re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email))

# b) Validate Bangladeshi mobile number
def is_valid_bd_mobile(number):
    return bool(re.fullmatch(r"(\+8801|01)[3-9]\d{8}", number))

# c) Validate USA telephone number
def is_valid_usa_phone(number):
    return bool(re.fullmatch(r"(\+1\s?)?(\d{3}[-.\s]?)?\d{3}[-.\s]?\d{4}", number))

# d) Validate 16-character alphanumeric password
def is_valid_password(password):
    return bool(re.fullmatch(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}", password))

# Test examples
print(is_valid_email("test@example.com"))        # True
print(is_valid_bd_mobile("+8801712345678"))      # True
print(is_valid_usa_phone("123-456-7890"))        # True
print(is_valid_password("A1b2C3d4E5f6G7h8!"))    # True

