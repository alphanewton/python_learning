
print("This program analyzes if the given string is a valid Email")

email = input("Enter your Email: ")#g@g.in
k,d=0,0

if len(email)>=6:
    if email[0].isalpha():
        if email.count("@")==1:
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        continue
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d = 1

                if k == 1 or d==1:
                    print("wrong Email 5")
                else:
                    print(" Email is formatted correctly")

            else:
                print("wrong Email 4")
        else:
            print("wrong Email 3")
    else:
        print("wrong Email 2")
else:
    print("wrong Email 1")


