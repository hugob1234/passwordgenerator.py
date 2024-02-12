import random
import string
x = int(input("Enter length of password: "))
def password(length=x):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(x))

gen = password(x)
print(f"Your new password is : {gen}")
    
