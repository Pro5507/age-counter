a= int(input("Please enter your age: "))
if a<12:
    print("You are a kid or tween")
elif a<20 and a>11:
    print("You are teenager")
elif a==20 and a==21:
    print("You are adult")
elif a>21 and a<41:
    print("You are in middil age")
elif a>40 and a<61:
    print("You are in higher age")
else:
    print("You are old")