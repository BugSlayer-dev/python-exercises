def plus(x,y):
    print(x+y)

def times(x,y):
    print(x*y)

def minus(x,y):
    print(x-y)

def divided(x,y):
    print(x/y)

while True:
    print("\n number 1 = +\n number 2 = *\n number 3 = -\n number 4 = /\n")
    r = int(input("Choose a sign :"))
    # r=int(r)
    if r == 1:
        n1=float(input("number one = "))
        n2=float(input("number two = "))
        plus(n1,n2)
    elif r == 2:
        n1=float(input("number one = "))
        n2=float(input("number two = "))
        times(n1,n2)
    elif r == 3:
        n1=float(input("number one = "))
        n2=float(input("number two = "))
        minus(n1,n2)
    elif r == 4:
        n1=float(input("number one = "))
        n2=float(input("number two = "))
        divided(n1,n2)
    else :
        print("Enter the correct number.")
        continue

