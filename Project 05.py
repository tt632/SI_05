import datetime

attendance_records = {}


def check_in(employee_id):
    current_time = datetime.datetime.now()
    if employee_id in attendance_records:
        print(f"Employee {employee_id} already checked in at {attendance_records[employee_id]['check_in']}!")
    else:
        attendance_records[employee_id] = {'check_in': current_time, 'check_out': None}
        print(f"Employee {employee_id} checked in at {current_time.strftime('%Y-%m-%d %H:%M:%S')}.")


def check_out(employee_id):
    current_time = datetime.datetime.now()
    if employee_id in attendance_records and attendance_records[employee_id]['check_out'] is None:
        attendance_records[employee_id]['check_out'] = current_time
        print(f"Employee {employee_id} checked out at {current_time.strftime('%Y-%m-%d %H:%M:%S')}.")
    elif employee_id not in attendance_records:
        print(f"Employee {employee_id} has not checked in yet!")
    else:
        print(f"Employee {employee_id} has already checked out!")


def generate_report():
    print("\n--- Attendance Report ---")
    if attendance_records:
        for employee_id, times in attendance_records.items():
            check_in_time = times['check_in'].strftime('%Y-%m-%d %H:%M:%S') if times['check_in'] else 'N/A'
            check_out_time = times['check_out'].strftime('%Y-%m-%d %H:%M:%S') if times['check_out'] else 'Not checked out'
            print(f"Employee ID: {employee_id}, Check-In: {check_in_time}, Check-Out: {check_out_time}")
    else:
        print("No attendance records found!")


if __name__ == "__main__":
    while True:
        print("\n--- Employee Attendance System ---")
        print("1. Check-In")
        print("2. Check-Out")
        print("3. Generate Attendance Report")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            employee_id = input("Enter employee ID to check-in: ")
            check_in(employee_id)

        elif choice == '2':
            employee_id = input("Enter employee ID to check-out: ")
            check_out(employee_id)

        elif choice == '3':
            generate_report()

        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")
