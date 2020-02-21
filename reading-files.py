
# open("employees.txt", "w") "write" can write to file only
# open("employees.txt", "a") "append" can only add text at the end of file
# open("employees.txt", "r+") "read and write"

employee_file = open("employees.txt", "r")

# print(employee_file.readable())  returns a boolean if a file is readable or not
# print(employee_file.read())  # print whole file
# print(employee_file.readline())  # print one line at a time
# print(employee_file.readlines())  # take each line of a file into an array
# print(employee_file.readlines()[2])  # take one line of a file into an array

for employee in employee_file.readlines():
    print(employee)

employee_file.close()
