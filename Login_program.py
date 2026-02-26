print("Welcome to Our Page")

username_db="Bilal"
password_db="1234"

username=input("Enter username :")
password=input("password :")

if username_db==username and password_db==password:
    print("Login Suceessful")
elif username_db!=username:
    print("invalid Username")
elif password_db!=password:
    print("incorrect password")
else:
    print("invalid")