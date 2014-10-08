import csv

neighborhoods = []
days = []

monday = 0
tuesday = 0
wednesday = 0
thursday = 0
friday = 0
saturday = 0
sunday = 0

# my_street = []

# with open('sweep.csv') as f:

#     reader = csv.reader(f)

#     for row in reader:
        # # Negative means count from the right, which is easier here
        # neighborhood = row[-2]

        # if neighborhood not in neighborhoods:
        #     # Append it to the list!
        #     neighborhoods.append(neighborhood)

        # if row[1] == "Mon":
        #     monday +=1
        # if row[1] == "Tues":
        #     tuesday +=1
        # if row[1] == "Wed":
        #     wednesday +=1
        # if row[1] == "Thu":
        #     thursday +=1
        # if row[1] == "Fri":
        #     friday +=1
        # if row[1] == "Sat":
        #     saturday +=1
        # if row[1] == "Sun":
        #     sunday +=1

# function to print out which week(s) of the month there is sweeping
def which_weeks(weeks_of_month):
    print_numbers = []
    if weeks_of_month[0] == 'True':
        # print "1"
        print_numbers.append(1)
    if weeks_of_month[1] == 'True':
        # print "2"
        print_numbers.append(2)
    if weeks_of_month[2] == 'True':
        # print "3"
        print_numbers.append(3)
    if weeks_of_month[3] == 'True':
        # print "4"
        print_numbers.append(4)
    if weeks_of_month[4] == 'True':
        # print "5"
        print_numbers.append(5)
    return print_numbers

# for functions, move to outermost indentation level        
def sweep_times():
    with open('sweep.csv') as f:
        reader = csv.reader(f)

        for row in reader:
            street_name = row[5]
            weekday = row[1]
            blockside = row[2]

            if street_name == "Broderick St":
                street_odd_from = int(row[14])
                street_odd_to = int(row[15])

                if street_odd_from > 2000 and street_odd_to < 2100 and blockside == "West":
                    my_street = row
                    weeks_of_month = my_street[9:14]
        print "My street is swept on", my_street[1], "from", my_street[6], "to", my_street[7], "on week(s)", which_weeks(weeks_of_month)

# call the function
sweep_times()

# you are returning the things you care about
    # return my_street, weeks_of_month

# you are calling the function, which returns the things you care about
# my_street, weeks_of_month = sweep_times()

# print my_street
# print weeks_of_month

# def which_weeks(weeks_of_month):
#     print_numbers = []
#     if weeks_of_month[0] == 'True':
#         # print "1"
#         print_numbers.append(1)
#     if weeks_of_month[1] == 'True':
#         # print "2"
#         print_numbers.append(2)
#     if weeks_of_month[2] == 'True':
#         # print "3"
#         print_numbers.append(3)
#     if weeks_of_month[3] == 'True':
#         # print "4"
#         print_numbers.append(4)
#     if weeks_of_month[4] == 'True':
#         # print "5"
#         print_numbers.append(5)
#     return print_numbers

# # print "My street is swept on", my_street[1], "from", my_street[6], "to", my_street[7], "on week(s)", which_weeks(my_street[9:14]) #weeks_of_month

# print "My street is swept on", my_street[1], "from", my_street[6], "to", my_street[7], "on week(s)", which_weeks(weeks_of_month) #weeks_of_month

# print "Found {} neighborhoods".format(len(neighborhoods))
# print sorted(neighborhoods)

# print "monday =", monday
# print "tuesday =", tuesday
# print "wednesday =", wednesday
# print "thursday =", thursday
# print "friday =", friday
# print "saturday =", saturday
# print "sunday =", sunday


# print my_street
