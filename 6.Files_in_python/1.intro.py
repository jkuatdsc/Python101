"""
 Intro into  files in python
 # Open()....Read() | Write()....Close()  -->Remember to CLOSE the file
"""
# Reading data from text files --> (I've created a new text file and called it data.txt) this is the file i'll read from
my_file = open('data.txt', 'r')
file_contents = my_file.read()
my_file.close()
print(file_contents)

# Writing data to files --> (All the data in the file will be overwritten)
data_to_write = input('Enter some text here: ')  # The input method should be called before opening the file
my_writable_file = open('data.txt', 'w')
my_writable_file.write(data_to_write)
my_writable_file.close()
