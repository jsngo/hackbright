import csv
import sys

# row[1] : day of the week
# row[4] : right or left
# row[5] : street name
# row[6] : start time
# row[7] : end time
# row[9] : week 1 of month
# row[10] : week 2 of month
# row[11] : week 3 of month
# row[12] : week 4 of month
# row[13] : week 5 of month
# row[14] : left side from address (house number)
# row[15] : left side to address (house number)
# row[16] : right side from address (house number)
# row[17] : right side to address (house number)
# row[18] : full street name
# row[19] : zipcode

def sweep_times(street_name):
    with open('sweep.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
        # street name (corridor) is item 5 in the list
      
        # TODO: Check lowercase versions of both,
        # in case of accidental or inconsistent capitalization.
            if row[5] == street_name:
                street_odd_from = int(row[14])
                street_odd_to = int(row[15])

                if row[4] == "R":
                    print "No. {}-{} swept on {} at {}-{}".format(row[16],row[17],row[1], row[6], row[7])
                else:
                    print "No. {}-{} swept on {} at {}-{}".format(row[14],row[15],row[1], row[6], row[7])

                # for just my block
                # if street_odd_from > 2000 and street_odd_to < 2100:
                #     if row[4] == "R":
                #         print "No. {}-{} swept on {} at {}-{}".format(row[16],row[17],row[1], row[6], row[7])
                #     else:
                #         print "No. {}-{} swept on {} at {}-{}".format(row[14],row[15],row[1], row[6], row[7])

# call the function
# sweep_times(sys.argv[1])

def day_counter():
    with open('sweep.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print row['WEEKDAY']


day_counter()
