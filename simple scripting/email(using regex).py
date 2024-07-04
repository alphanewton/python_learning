# a-z
# 0-9
# . - time 1 before @
# @ time 1
# . 2,3 from end
import re

email = input("Enter Email: ")

email_condition = "^[a-z][A-Za-z0-9._]{2,}@[A-Za-z]{3,10}.{1}[A-Za-z.]{2,6}"

if re.search(email_condition,email):
    print("The email format is correct")
else:
    print("Wrong email")