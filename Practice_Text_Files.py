def main():
    # outfile = open("test.txt", "w")
    # outfile.write("Test")
    # outfile.close()

    # "with" automatically opens and close the file removing the mistake of forgetting to close a file
    with open('test.txt', 'w') as outfile:
        outfile.write('Test\n')
        outfile.write('Test2')
    
    # with open('test.txt', 'r') as infile:
    #     print(infile.readline())

    with open('test.txt') as file:
        for line in file:
            print(line, end="")
        print()

    with open('test.txt') as file:
        contents = file.read()
        print(contents)

if __name__ == "__main__":
    main()