def plus(x,y):
    return(x+y)

def times(x,y):
    return(x*y)

def minus(x,y):
    return(x-y)

def divided(x,y):
    return(x/y)

while True:
    try:
        print("\n number 1 = +\n number 2 = *\n number 3 = -\n number 4 = /\n")
        r = int(input("Choose a sign :"))
        if r >= 1 and r <= 4 :
            n1=float(input("number one = "))
            n2=float(input("number two = "))
            if n1 % 2 == 0 :
                n1 = int(n1)
            if n2 % 2 == 0 :
                n2 = int(n2)
            if r == 1:
                print(f"{n1} + {n2} = {plus(n1,n2)}")
            elif r == 2:
                print(f"{n1} * {n2} = {times(n1,n2)}")
            elif r == 3:
                print(f"{n1} - {n2} = {minus(n1,n2)}")
            elif r == 4:
                print(f"{n1} / {n2} = {divided(n1,n2)}")  
        else:
            print("Enter the correct number.")
    except ValueError :
        print("Please enter a number.")
    except ZeroDivisionError :
        print("Cannot divide by zero.")
    j=input("Continue? y/n:\t").strip().lower()
    if j=="n":
        break


