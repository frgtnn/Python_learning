#File Objects
#Less recomended, 'w' #writing, 'a' #appending, 'r' #reading, 'r+..' two things
#print(f.open), print(f.mode)
#without context manager
# f = open('test.txt', 'r')
# print(f.mode)
# f.close()
#with context manager (easier one)
# with open('test.txt', 'r') as f:
#     pass
# print(f.closed)
#print exactly the hole file which we want to read
#with open('test.txt', 'r') as f:
 #   f_contents = f.read() /readlines(), we've got printed all of the lines, of our file
     #readline() prints out, the first line  of our file, if we are going to do it in the next lines, one more time
        #its going to print us the next line of our file, etc.
            #if we add to print(f_contents, end='') it won't print the next lines
                #f.read(100) gives us first 100 characters in our file
                    #size_to_read = 100, f_contents = f.read(size_to_read) gives us the same as, f.read(100)
#print(f_contents)

# with open('test.txt', 'r') as f:
#    for line in f:
#        print(line, end='') / another way to read lines

# size_to_read = 10
#    f_contents = f.read(size_to_read)
#    while len(f_contents) > 0:
#        print(f_contents, end = '')
#           f_contents = f.read(size_to_read)      gives us a "stop" after next 10 characters
#                print(f.tell()) tells us how many characters the string we gonna see
                     #f.seek(0) starts a reading of the file
# while len(f_contents) > 0:
#     print(f_contents, end = '')
#     f_contents = f.read(size_to_read)

# with open('test2.txt', 'w') as f:
    #or pass  - it creates a new file
    # f.write('Test') it write 'test' in our file

# with open('test2.txt', 'w') as f:
#     f.write('Test')
#     f.seek(0)
#     f.write('R') rewrites first character, from T to R

#original file open reading
#file that is copy, and doesn't exist yet and we write
#we are saying 'for each line' in our original file, for wf
# with open('test.txt', 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

# with open('harnas.jpg', 'rb') as rf:
#     with open('harnas_copy.jpg', 'wb') as wf:
#         for line in rf:
#             wf.write(line)

with open('harnas.jpg', 'rb') as rf:
    with open('harnas_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)



