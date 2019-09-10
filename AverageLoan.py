import csv
# csv module makes things much easier; could do it from scratch with string split method on each line
totMortgage, numMortgage, totOwn, numOwn, totRent, numRent, avgMortgage, avgOwn, avgRent = 0, 0, 0, 0, 0, 0, 0, 0, 0
# variables that define the total of each sum of loans, the number of people with each kind of loan, and their averages
with open('loan_data.csv', 'r') as csv_file, open('home_ownership_data.csv', 'r') as csv_file2:
    csv_reader = csv.reader(csv_file)
    csv_reader2 = csv.reader(csv_file2)
    myList = list(csv_reader2)
    # need to create a list to iterate multiple times over this list
    for line in csv_reader:
        for line2 in myList:
            if line[0] == line2[0]:
                if line2[1] == "MORTGAGE":
                    totMortgage += int(line[1], 10)
                    numMortgage += 1
                if line2[1] == "OWN":
                    totOwn += int(line[1], 10)
                    numOwn += 1
                if line2[1] == "RENT":
                    totRent += int(line[1], 10)
                    numRent += 1
    # nested for loop allows for checking if member id's match; pretty slow, but only 40,000 checks so not that bad
    avgMortgage = totMortgage/numMortgage
    avgOwn = totOwn/numOwn
    avgRent = totRent/numRent

    print("The average mortgage loan is ", avgMortgage)
    print("The average loan to rent is ", avgOwn)
    print("The average rent loan is ", avgRent)











