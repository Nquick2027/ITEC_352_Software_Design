#!/usr/bin/env python3
# Nathan Quick
# 02/17/2025

def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    

def list(movie_catalog):
    if len(movie_catalog) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        for name in movie_catalog:
            movie = movie_catalog[name]
            print("Name     " + name)
            print("Year:    " + movie["year"])

def add(movie_catalog):
    name = input("Name: ")
    year = input("Year: ")
    movie = {"year": year}
    movie_catalog[name] = movie
    print(name + " was added.\n")
    
def delete(movie_catalog):
    name = input('Name: ')
    if name in movie_catalog:
        del movie_catalog[name]
        print(name + ' was deleted.\n')
    else:
        print(name + " doesn't exist in this catalog")
        
def main():
    movie_catalog = {
        "Monty Python and the Holy Grail":
            {"year": "1975"},
        "On the Waterfront":
            {"year": "1954"},
        "Cat on a Hot Tin Roof":
            {"year": "1958"}
    }
    
    display_menu()
    while True:        
        command = input("Command: ")
        if command == "list":
            list(movie_catalog)
        elif command == "add":
            add(movie_catalog)
        elif command == "del":
            delete(movie_catalog)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
