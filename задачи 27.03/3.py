password = input()
def check_password(password):
    if len(password) >= 8 and password.lower() != password:
        return True
    else:
        return False
print(input(check_password(password)))