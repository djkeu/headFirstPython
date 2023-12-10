try:
    with open('myfile.txt') as f:
        file_data = f.read()
    print(file_data)
except FileNotFoundError:
    print("The data file is missing.")
except PermissionError:
    print("This is not allowed.")
