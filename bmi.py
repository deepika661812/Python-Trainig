print("bmi")
name=str(input("enter your name:"))
age=int(input("enter your age:"))
height=float(input("enter your height(cm):"))
weight=float(input("enter your weight(kg):"))
height= height/100
bmi=weight/(height**2)
print(f"your bmi is: {bmi:.2f}")
if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 24.9:
    print("normal weight")
elif 25 <= bmi < 29.9:
     print("overweight")
else:
    print("obesity")





