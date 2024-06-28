resultsset = {
    '001456G': '4',
    '002454R': '3.56',
    '002455S': '3.56',
    '002456T': '3.56'
}

symbol_number = input("Enter your symbol number:  ")

for i in resultsset.keys():
    if symbol_number ==i:
        result = resultsset[i]
        break
    else:
        result = ''
if result != "":
    print(f"your result is {result}")
else:
    print(f"Your symbol number not found.")


