a = int(input("enter the first number  = "))
b = int(input("enter the second number = "))

print(" a = +   (Addition) \n b = -   (subtraction) \n c = *   (multiplication) \n d = **  (Exponential) \n e = /   (Division) \n f = %   (Modulus) \n g = //  (Floor Divistion) ")

c = input(" enter the your celqulastion key ")

if c == "a":
    d = a + b
    print("your ansuar is = ",d)
elif c == "b":
    d = a - b
    print("your ansuar is = ",d)
elif c == "c":
    d = a * b
    print("your ansuar is = ",d)
elif c == "d":
    d = a ** b
    print("your ansuar is = ",d)
elif c == "e":
    d = a / b
    print("your ansuar is = ",d)
elif c == "f":
    d = a % b
    print("your ansuar is = ",d)
elif c == "g":
    d = a // b
    print("your ansuar is = ",d)

else:
    print("pls right key")
