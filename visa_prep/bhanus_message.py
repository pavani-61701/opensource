s=input()
if len(s)==10 and s.isdigit():
    digits=s
elif len(s)>4 and s[0]=="+" and s[1:3].isdigit() and s[3]==" " and len(s[4:])==10 and s[4:].isdigit():
    digits=s[4:]
else:
    print("Incorrect")
    exit()
if sum(int(digit) for digit in digits)>0:
    print("Correct")
else:
    print("Incorrect")

            
        
