def calculator(a,operator,b):
    if  operator == "+" :
        print(a+b)
    elif operator == "-" :
        print(a-b)
    elif operator == "*" :
        print(a*b)
    elif operator == "/" :
        print(a/b)
    else:
        print("invalid operator")
while True:
     a=int(input())
     operator=input(("+,-,*,/"))
     b=int(input())
     print("result:",calculator(a,b,operator))

     again = input(" you calculate again? (yes/no): ").lower()
     if again != "yes":
        print("Exiting calculator.")
        break