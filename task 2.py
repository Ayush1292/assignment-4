# Write and Append Data to a File

# Write data in file
user_input = input("Enter text to write to the file: ")
file = open("output.txt", "w")  
file.write(user_input + "\n")
print("Data successfully written to output.txt.\n")
file.close()

#appending data in file
user_input1 = input("Enter additional text to append: ")
file = open("output.txt", "a")
appending_file = file.write(user_input1)
print("Data successfully appended.\n")
file.close()

# Reading data from the file
print("Final content of output.txt:")
file = open("output.txt", "r")
reading_file = file.read()
print(reading_file)
file.close()


