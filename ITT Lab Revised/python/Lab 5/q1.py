def calculator(x,y,op):
    # Use a breakpoint in the code line below to debug your script.
    if op=="+":
        c=x+y
        print(c)

    elif op== "-":
        c=x-y
        print(c)

    elif op== "*":
        c=x*y
        print(c)

    elif op== "/":
        c=x/y
        print(c)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x=float(input("Enter 1st number: "))
    y=float(input("Enter 2nd number: "))
    op=input("Enter operator: ")
    calculator(x,y,op)