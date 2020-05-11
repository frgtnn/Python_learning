    #OPENING A FILE AS A READER
# import csv
# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     next(csv_reader) (line[2]) -> the line which we want to print
#     for line in csv_reader:
#         print(line)       #how we are gonna to print them,

#OPENING A FILE AS A WRITER, AND CREATING A NEW ONE FILE
# import csv
#
# with open('names.csv', 'r') as csv_file: - opening a original file to be read
#     csv_reader = csv.reader(csv_file) - creating a csv reader variable, using csv reader, to read method to read the file
#
#     with open('new_names.csv', 'w') as new_file: we opening a new file
#         csv_writer = csv.writer(new_file, delimiter='-'), we are creating a csv writer by a csv writer method
#
#         for line in csv_reader: / for each line in csv data
#             csv_writer.writerow(line) / we are writing to a new file from original file each line
                #delimiter='\t') - makes tabs between words
                    #if we won't give a delimiter, we will see only one variable, cause python expected e.g. comas

#DICTIONARY READER
# import csv
#
# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#
#     for line in csv_reader:
#         print(line),  we see variables like this in this .csv, {'first_name, last_name, email: ....'}
#             print(line['email'])  #we will see only e-mails
import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)


    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)