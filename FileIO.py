f = open('a.txt', 'r') # it will show FILENOTFOUNDERROR, if there is no a.txt in the file, r is read mode access
# w is write mode. r is default mode
f2 = open('a2.txt', 'w')
f3 = open('a2.txt', 'at')
f3.write("Im adding this at the end of the file")
f2.write(". I am writing this from python script") # i can write in the file when im in write mode
# f2.read() # cant read in write mode and vice versa
print(f) # print file wrapper object in read mode
text = f.read() # extract the data and print to the console
print(text) # print to the console
with open('myfile3.txt', 'w+') as fw:
    fw.write("Using withopen will allow us not to write close again and again")
f.close() # close the access of the file
f2.close()
f3.close()