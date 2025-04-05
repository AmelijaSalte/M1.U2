import random
import string 

print('___________Passwords generator_____________')

lenght = int(input("какой длины пароль вы хотите?"))
password = ""

for i in range(0, lenght, 1):
    password += random.choice(string.printable)

print("Password: ", password)