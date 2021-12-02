# 10/21/21
# To Do program: Organizes a to do list based on time and importance. Sends updates on due dates to a phone.

class Task:
    def __init__(self, name, importance, date):
        self.name = name
        self.importance = importance
        self.date = date

container = ""
exampleTask = Task("Clean", 10, "10/24/21")

with open("to-do-list.txt", "a+") as file:
    container = str(exampleTask.name) + " " + str(exampleTask.importance) + " " + str(exampleTask.date)
    file.write(container)
    file.write("\n")

with open('to-do-list.txt', 'r+') as file:
    print(file.read())

do "blah blah blah"
