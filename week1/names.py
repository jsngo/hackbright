import random 

# first and last names block
with open('names.txt') as f:
    data = f.readlines()

# define empty array for the subsequent appending
stripped = []
for name in data:
    stripped.append(name.strip())

data = sorted(stripped)

# put it outside the for loop so we don't overwrite it
first_names = []
last_names = []

for name in data:
    # returns a list, the first element is first name, etc.
    name_pieces = name.split(" ")

    # access first name from index 0 of name_pieces
    first_name = name_pieces[0]

    # append it to empty list first_names
    first_names.append(first_name)

    # same as above
    last_name = name_pieces[1]

    last_names.append(last_name)

# villians adjectives block
with open('villains.txt') as f:
    vdata = f.readlines()

# define empty arrays for subsequent appending
villain_adjs = []
cool_names = []

for adj in vdata:
    adj = adj.strip().title()
    villain_adjs.append(adj)

# creates a list of random names that takes in three lists, the length of the list is determined by the length of the second list (also adds line breaks)
def villain_name_generator(x, y, z):
    for i in range(len(y)):
        villain_adj = random.choice(x)
        first_name = random.choice(y)
        last_name = random.choice(z)
        cool_name = villain_adj + " " + first_name + " " + last_name + "\n"
        cool_names.append(cool_name)
    return cool_names

# use the above function to create a list of villain names called final_list
final_list = villain_name_generator(villain_adjs, first_names, last_names)

# write the contents of final_list to output.txt
with open('output.txt', 'w') as f:
    f.writelines(final_list)