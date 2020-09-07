from validator import Validator

username = "Starfire"
validator = Validator()


if validator.valid_username(username):
    print("This username is valid!")
else:
    print("This username is invalid!")


username = "Ann"
validator = Validator()


if validator.valid_username(username):
    print("This username is valid!")
else:
    print("This username is invalid!")
