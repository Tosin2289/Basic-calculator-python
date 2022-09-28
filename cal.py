print("=============== This is a basic Calculator ===============")
print("1-Addition\n2-Subtraction\n3-Multiplication\n4-Division")

ope=input()


if ope == "1":
    fst=int(input("Enter first number  :"))
    snd=int(input("enter second number  :"))
    add=fst + snd
    print(add)


if ope =="2":
    fst=int(input("Enter first number  :"))
    snd=int(input("enter second number  :"))
    sub=fst - snd
    print(sub)

if ope =="3":
    fst=int(input("Enter first number  :"))
    snd=int(input("enter second number  :"))
    multipy=fst*snd
    print(multipy)


if ope =="4":
    fst=float(input("Enter first number  :"))
    snd=float(input("enter second number  :"))
    div=fst/snd
    print(div)