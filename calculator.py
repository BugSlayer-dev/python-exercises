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
        # r=int(r)
        if r == 1:
            n1=float(input("number one = "))
            n2=float(input("number two = "))
            print(f"{n1} + {n2} = {plus(n1,n2)}")
        elif r == 2:
            n1=float(input("number one = "))
            n2=float(input("number two = "))
            print(f"{n1} * {n2} = {times(n1,n2)}")
        elif r == 3:
            n1=float(input("number one = "))
            n2=float(input("number two = "))
            print(f"{n1} - {n2} = {minus(n1,n2)}")
        elif r == 4:
            n1=float(input("number one = "))
            n2=float(input("number two = "))
            print(f"{n1} / {n2} = {divided(n1,n2)}")  
        else :
            print("Enter the correct number.")
            continue
    except ValueError :
        print("Please enter a number.")
    except ZeroDivisionError :
        print("The number shouldn't be 0.")
    finally:
        j=input("Are you planning to continue? y/n\t")
        if j=="n":
            break
        else:
            continue


