def check_password(password):
    string ='''@#$%^&*(){}:";<>/?'''
    if(len(password)<10 or len(password)>15):
        return "password is valid"
    elif not any (char.islower() for char in password):
        return "password contains lowercase"
    elif not any (char.isupper() for char in password):
        return "password contains upperrcase"
    elif not any (char.isdigit() for char in password):
        return "password contains digit"
    elif not any (char in string for char in password):
        return "password not containspecial characters"
    elif " " in password:
        return "password must not contain spaces"
    elif password[-1] not in ['.', '@']:
        return "password must end with '.' or '@'"
    else:
        return "password valid"
password=input("enter password")
print(check_password(password))