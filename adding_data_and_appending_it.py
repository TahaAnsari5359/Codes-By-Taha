
write1 = input("Enter text to write to the file: ")
with open("output.txt", "a") as f:
    f.write(write1 + " " )
    print("Data Successfully Written to output.txt \n ")


write2 = input('Enter additional text to append: ')
with open("output.txt", "a") as f:
    f.write(write2 + "\n")
    print("Data Successfully appended \n ")

write3 = print('Final Content of output.txt: ')
print(write1)
print(write2)