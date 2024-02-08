# hrm.py
class Employee:
    def __init__(self, employee_id, name, designation, department, contact_info, appointment_date, leave_details):
        self.employee_id = employee_id
        self.name = name
        self.designation = designation
        self.department = department
        self.contact_info = contact_info
        self.appointment_date = appointment_date
        self.leave_details = leave_details


# Initialize a list to store employee records
employee_records = [
    Employee("E001", "Mr. Kiten", "Chairman", "All", "xxxxxxxxxxxxx", "2020.01.01",
             ["2020.03.02", "2020.05.03", "2020.05.04"]),
    Employee("E002", "Mr. K. Josaph", "Head of the Finance Department", "Finance Department", "xxxxxxxxxxxxx",
             "2021.01.01", ["2021.03.05", "2023.02.02", "2021.10.20"]),
    Employee("E003", "Mr. John", "Software Developer", "Department of Development", "xxxxxxxxxxxxx", "2019.01.01",
             ["2019.06.05", "2019.02.03", "2019.03.01"]),
]


def view_personal_information(employee_id):
    # Display personal information of the specified employee
    for employee in employee_records:
        if employee.employee_id == employee_id:
            print(f"Employee ID: {employee.employee_id}")
            print(f"Employee Name: {employee.name}")
            print(f"Designation: {employee.designation}")
            print(f"Department: {employee.department}")
            print(f"Contact Information: {employee.contact_info}")
            print(f"Appointment Date: {employee.appointment_date}")
            print(f"Leave Details: {', '.join(employee.leave_details)}")
            break
    else:
        print("Employee not found.")


def update_personal_information(employee_id, new_contact_info, new_position, new_department):
    # Update personal information of the specified employee
    for employee in employee_records:
        if employee.employee_id == employee_id:
            employee.contact_info = new_contact_info
            employee.designation = new_position
            employee.department = new_department
            print("Personal information updated successfully.")
            break
    else:
        print("Employee not found.")


def submit_leave_request(employee_id, leave_type, duration, details):
    # Submit leave request for the specified employee
    for employee in employee_records:
        if employee.employee_id == employee_id:
            employee.leave_details.append(f"{duration}: {leave_type} - {details}")
            print("Leave request submitted successfully.")
            break
    else:
        print("Employee not found.")


def view_company_policies():
    # Display company policies and guidelines
    print("Company Policies:")
    # Add your company policies here


def access_work_schedules(employee_id):
    # Display work schedules of the specified employee
    for employee in employee_records:
        if employee.employee_id == employee_id:
            print(f"Work Schedule for {employee.name}:")
            # Add work schedule information here
            break
    else:
        print("Employee not found.")
