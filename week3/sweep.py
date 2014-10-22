# http://labs.bewd.co/putting-it-together/

import csv

# 87 Coral Rd is swept on Mondays only.
# 60 Fanning Way is swept on Tuesdays only.
# 50 Delmar St is swept on Wednesdays and Fridays.
# 33 Vesta St is swept on Tuesdays and Thursdays.
# 77 Dukes Ct is swept on Fridays only.

# write a function that takes a street name and tells you if it is going to be swept tomorrow.

def day_counter():
    with open('sweep.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            day = row['WEEKDAY']
            count = days_counts[day]
            days_counts[day] += 1
    for d in ordered_days:
        print "{} blocks swept on {}".format(days_counts[d], d)

def swept_most():
    max_sweeps = 0
    max_day = ""
    for d in days_counts:
        if days_counts[d] > max_sweeps:
            max_sweeps = days_counts[d]
            max_day = d
    print "{} is the day with the most street sweeping: {}".format(max_day, max_sweeps)


def swept_tomorrow(street_name, house_number):
   if this_part_of_street_will_be_swept_tomorrow:
       return True
   else:
       return False

result = swept_tomorrow("Dukes Ct", 77)
print "If tomorrow is Friday, this should be True: {}".format(result)

def main():
    

if __name__=="__main__":
    main() 