import csv
from objects_week8 import Homework, HomeworkList

def get_homeworklist():
    filename = "Homework_list.csv"
    homeworklist = HomeworkList("Software Design")
    with open(filename, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            # convert row to Homework object
            homework = Homework(row[0])
            if row[1] == "True":
                homework.completed = True
            homeworklist.addHomework(homework)
        return homeworklist

def list_homeworklist(homeworklist):
    if homeworklist.getCount() == 0:
        print("There is no homework in this list.\n")
    else:
        i = 1
        for homework in homeworklist:
            print(str(i) + ". " + str(homework))
            i += 1
        print()

def add_homework(homeworklist):
    description = input("Description of homework: ")
    homework = Homework(description)
    homeworklist.addHomework(homework)
    print()

def complete_homework(homeworklist):
    number = int(input("Number: "))
    homework = homeworklist.getHomework(number)
    homework.completed = True
    print()

def write_homeworklist(name, homeworklist):
    # convert the HomeworkList object to a list of lists
    rows = []
    for homework in homeworklist:
        row = []
        row.append(homework.description)
        row.append(homework.completed)
        rows.append(row)
    
    # write the list of lists to CSV file
    filename = "homework_list.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def delete_homework(homeworklist):
    number = int(input("Number: "))
    homework = homeworklist.getHomework(number)
    homeworklist.removeHomework(homework)
    print()

def displayMenu():
    print("The Homework List Program")
    print()
    print("Command Menu")
    print("list             - List all homework")
    print("add              - Add homework")
    print("complete         - Mark homework complete")
    print("delete           - Delete homework item")
    print("exit             - Exit program")
    print()

def main():
    displayMenu()

    homeworklist = get_homeworklist()
    print("Software Design Homework List")

    while True:
        command = input("Command:   ")
        if command.lower() == "list":
            list_homeworklist(homeworklist)
        elif command.lower() == "add":
            add_homework(homeworklist)
        elif command.lower() == "complete":
            complete_homework(homeworklist)
        elif command.lower() == "delete":
            delete_homework(homeworklist)
        elif command.lower() == "exit":
            write_homeworklist("Software Design", homeworklist)
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")

if __name__ == "__main__":
    main()