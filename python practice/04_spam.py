p1 = "Make a lot of money"
p2 = "buy now"
p3 = "Subscribe this"
p4 = "click this"

message = input("Enter yourcomment: ")

if (p1 in message or p2 in message or p3 in message or p4 in message):
    print("Spam comment")
else:
    print("not a spam comment")