# Read a File and Handle Errors

try:
    file = open("sample.txt", "r")
    print('Reading file content: ')
    file_content = file.read()
    print(file_content)
    file.close()


except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

