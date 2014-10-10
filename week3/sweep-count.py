# http://labs.bewd.co/putting-it-together/

import csv

days_counts = {
    "Mon": 0,
    "Tues": 0,
    "Wed": 0,
    "Thu": 0,
    "Fri": 0,
    "Sat": 0,
    "Sun": 0,
    "Holiday": 0
}

ordered_days = [
    "Mon",
    "Tues",
    "Wed",
    "Thu",
    "Fri",
    "Sat",
    "Sun",
    "Holiday"
]

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
    day_counter()
    print "\n"
    swept_most()

if __name__=="__main__":
    main() 