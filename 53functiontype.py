##WAP to print even number betweeen start and end using function
def display_even(first,last):
    for i in range(first,last+1):
        if i%2 ==0:
            print(i)
start = 100
end = 150
display_even(start,end)

## Types of Function
#system Define
#User Define

# 1. No parameter No Return Type

def display_name():
    print("Pradip Chaudhary")
display_name()
# 2. Parameter and No Return Type
def add(n1,n2): #parameter
    total = n1 + n2
    print(f"Total is {total}")

add(20,30) #argument giving value
# 3. Parameter and Return Type
def find_cube(num):
    cube = num * num * num
    return cube
myvalue = find_cube(2)
print(myvalue)
# 4. No parameter & Return Type
def voter_age():
    return 18

ram_age = 2
if ram_age >= voter_age():
    print("Ram is ready to vote")
else:
    print("Not a voter")





