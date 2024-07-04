s= "A man, a plan, a canal: Panama"
ns = ""

for i in s:
    if i.isalnum() is True:
        ns+=i.lower()

print(ns)