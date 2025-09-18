# import ???

# def to_celsius():
#     return

# def to_fahrenheit():
#     return

def convert_temp():
    option = int(input('Enter a menu option: '))
    if option == 1:
        try:
            f = int(input('Enter degrees Fahrenheit: '))
            c = temp.to_celsius(f)
            c = round(c, 2)
            print('Degrees Celsius:', c)
        except:
            print('You must enter a valid integer!')
    elif option == 2:
        try:
            c = int(input('Enter degrees Celsius: '))
            f = temp.to_fahrenheit(c)
            f = round(f, 2)
            print("Degrees Fahrenheit:", f)
        except:
            print('You must enter a valid integer!')
    else:
        print('Enter a valid menu option!')

# def main():
#     return

if __name__ == "__main__":
    main()
