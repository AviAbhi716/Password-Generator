import random
print("Welcome to the Password Generator")
num=int(input("Enter the number of numbers you want"))
alp=int(input("Enter the number of alphabets you want"))
sym=int(input("Enter the number of symbols you want"))
Letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Symbols=[
    ".", ",", "?", "!", ";", ":", "(", ")", "[", "]", "{", "}",
    "+", "-", "*", "/", "=", "%", "&", "^", "$", "#", "@", "~", "`","$", "^", "~","<",">","|"]
password=[]
for i in range(0,num):
    char=random.randint(0,9)
    password+=str(char)
for i in range(0,alp):
    char=random.choice(Letters)
    password+=char
for i in range(0,sym):
    char=random.choice(Symbols)
    password+=char
random.shuffle(password)
passwords=""
for i in password:
    passwords+=i
print(passwords)
