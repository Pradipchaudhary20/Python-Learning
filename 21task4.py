## Add your Electricity Bill From Jan dec In Dec in Dictonary and find total and average .


Bill = {

    'Jan': 200,
    'feb': 300,
    'Mar': 100,
    'Apr': 250,
    'jun': 270,
    'Jul': 210,
    'Aug': 220,
    'Sep': 250,
    'Oct': 270,
    'Nov': 280,
    'Dec': 290,
}
total = sum(Bill.values())
print(f"The total Bill is {total}")
print(f"The Average Bill is {total/7}")
