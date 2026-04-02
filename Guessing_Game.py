num="5"
guess=""
count=0
limit=3
out=False

while guess!=num and not out:
    if count < limit:
        guess= input("enter your guess : ")
        count+=1
    else:
        out=True
if out:
    print("you lose")   
else:
    print(" you win")    