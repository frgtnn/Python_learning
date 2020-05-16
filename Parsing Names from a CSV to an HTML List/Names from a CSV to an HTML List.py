# import csv
#
# html_output = ''
# names = []
#
# with open('patrons.csv.txt', 'r') as data_file:
#     csv_data = csv.reader(data_file)
#
#     for line in csv_data:
#         print(line)       #it prints the whole file line by line, it is printed in good way to read
#   next(csv_data)
#   next(csv_data) #gives us next two lines without first ones
# names.append(f"{line[0]} {line[1]}")
#
# for name in names:
#     print(name) #gives us only first values (two first first and second name in this situation)
# for line in csv_data
# if line[0] == 'No Reward':
    # break         #it shows us a person with "No Reward" on the last place

#ADDING THIS CSV ON HTML LIST:


import csv

html_output = ''
names = []

with open('patrons.csv.txt', 'r') as data_file:
    csv_data = csv.DictReader(data_file)        #DictReader turns each line into a dictionary instead of list


    # We don't want headers or first line of bad data
    next(csv_data)

    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'           #\n new line \t a tab, <li> list item

html_output += '\n</ul>'

print(html_output)