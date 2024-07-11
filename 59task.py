### create 10 employee who works on different department
###Print all employee who are in IT department

###option :
# display all department along with their names.
name = [
    # name , department
    ("Pradip", "web development"),
    ("Manish", "mobile application"),
    ("sujan", "date scienc"),
    ("Kiran", "Programming"),
    ("Ankit", "Ui/Ux design"),
    ("deepak", "cyber security"),
    ("sandip", "web development"),
    ("bishal", "Programming"),
    ("suman", "mobile application"),
    ("palden", "HR"),

]

### Find all from Web development
web_development = [name for name in name if name[1] == "web development"]

print(web_development)