a = int(input("Enter the First Number: "))
b = int(input("Enter the second Number: "))
c = int(input("Enter the Third Number: "))
d = int(input("Enter the fourth Number: "))

if a > b and a > c and a > d:
    print(f"{a} A is greater")
elif b > a and b > c and b > d:
    print(f"{b} B is greater")
elif c > a and c > b and c > d:
    print(f"{c} C is greater")
elif d > a and d > b and d > c:
    print(f"{d} D is greater")
else:
    print("Invalid Text")

print("Program End")
