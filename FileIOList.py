def main():
   
    years = [1975, 1979, 1983]
    with open("years.txt", 'w') as years_file:
        for year in years:
            years_file.write(str(year) + '\n')
    
    years = []
    with open('years.txt', 'r') as file:
        for line in file:
            line = line.replace('\n', '')
            years.append(int(line))
    print(years)

if __name__ == "__main__":
    main()