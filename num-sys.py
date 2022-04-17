"""A number of three digits when divided
by 2, 5, 9, 11 leaves remainder 1 in each case.
The number is (a) 981 (b)983 (c)991 (d)997"""

a = int(input("Enter a three digit no."))
b = str(a)
c = len(b)

if c==3:
    print("Entered Number is of 3 digits")
    if a % (2 and  5 and 9 and 11) == 1:
        print(f"{a} passed")
    
    else:
        print("does not retuns zero after devided by 2 and 5 and 9 and 11")

else:
    print(f"'{a}' is not 3 digits")