
# employee_file = open("employees.txt", "a")
employee_file = open("employees-a.txt", "w")  # overwrites the file
employee_file.write("Kelly - Customer Service\n")
employee_file.write("Toby - Human Resources\n")
employee_file.close()
