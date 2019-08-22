input_file = open("notes.txt")
files = input_file.readlines()
input_file.close()

files = [file.strip() for file in files]
print(files)

first_year_subjects = [file for file in files if file[2] == "1"]

print(first_year_subjects)

