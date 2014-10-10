# http://labs.bewd.co/putting-it-together/

import csv


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


def main():
    

if __name__=="__main__":
    main() 