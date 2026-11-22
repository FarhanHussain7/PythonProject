email=input("Enter your email: ")
if email=="":
    print("Email cannot be empty")
elif len(email)<5:
    print("Email is too short")
elif len(email)>50:
    print("Email is too long")
elif " " in email:
    print("Email cannot contain spaces")
elif email[0].isdigit():
    print("Email cannot start with a digit")
elif email[-1].isdigit():
    print("Email cannot end with a digit")
elif email.count("@")==0:
    print("Email must contain @ symbol")
elif email.count(".")==0:
    print("Email must contain . symbol")
elif email.count(".")>1:
    print("Email cannot contain more than one . symbol")
elif email.count("@")>1:
    print("Email cannot contain more than one @ symbol")
elif email.startswith("@") or email.endswith("@"):
    print("Email cannot start or end with @ symbol")
elif "@" in email and "." in email:
    print("Valid email")
else:    
    print("Invalid email")
