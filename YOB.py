print("Welcome to Calculate your Year at the Age of 100")
age=input("Enter your Age or Year of Birth\n")
if len(age)==2 or len(age)==3:
    if int(age)>120:
        print("You seem to be the most oldest person alive")
    elif int(age)<0:
        print("You are not yet born")
    elif len(age)==2:
        print(f"You will turn 100 years old in {2023+100-int(age)}")
    else:
        print("You are already 100 or more than 100 years old")
elif len(age)==4:
    if int(age)>2022:
        print("You are not yet born")
    elif int(age)<1900:
        print(f"You seem to be the most oldest person alive and you turned 100 in {int(age)+100}")
    elif int(age)<1923:
        print(f"You already turned 100 in {int(age)+100}")
    else:
        print(f"You will turn 100 years old in {int(age)+100}")
else:
    print("It's a wrong input")

print("Do you want to check your Age at certain year, press 'y' for Yes and press 'n' for No")
a=input()
if a=="y":
    b=int(input("Enter your Year Of Birth\t"))
    c=int(input("On which year you want to check your Age\t"))
    print("Your age will be ",c-b)
elif a=="n":
    print("Thank You for sparing your Valuable Time")
else:
    print("You pressed Wrong Key")