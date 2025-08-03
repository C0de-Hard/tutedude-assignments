# print("Hello World")

employees = {}

def add_employee():
    empId = int(input("Enter Employee ID : "))
    temp = {}
    temp["name"] = input("Enter name : ")
    temp["age"] = int(input("Enter age : "))
    temp["department"] = input("Enter Dept : ")
    temp["salary"] = float(input("Enter Salary : "))
    if len(temp) != 4:
        return None
    else:
        employees[empId] = temp

def view_employees():
    if not employees:
        print("Employee not found.")
    else:
        print()
        print(f"{'ID':<8}{'Name':<15}{'Age':<6}{'Department':<15}{'Salary':<10}")
        print("-" * 54)
        for emp_id, info in employees.items():
            print(f"{emp_id:<8}{info['name']:<15}{info['age']:<6}{info['department']:<15}{info['salary']:<10.2f}")
        print()

def search_employee(empId):
    if empId in employees:
        return employees[empId]
    else:
        return None

def main_menu():
    print('''
    1. Add Employee
    2. View All Employees
    3. Search for Employee
    4. Exit''')
    return

while True:
    main_menu()
    choice = int(input("Enter your query: "))
    
    if choice == 1:
        add_employee()
    elif choice == 2:
        view_employees()
    elif choice == 3:
        empId = int(input("Enter Employee ID to search: "))
        result = search_employee(empId)
        if result:
            print(f"Employee ID: {empId}, Details: {result}")
        else:
            print("Employee not found.")
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

