### Ask user to enter todo and print all todo 
total_todo = int(input("Enter total todo: "))
todos = []

# ASK
for i in range(total_todo):
    todo = input(f"Enter todo {i + 1}: ")
    todos.append(todo)

# Display
for todo in todos:
    print(todo)

## Ask user to enter n number of people names
## And print all names strat with B
## if there is no name, it should say " No Name Found"
## If there is /are 