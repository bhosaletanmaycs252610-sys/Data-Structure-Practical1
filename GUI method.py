from tkinter import *
from tkinter import messagebox

employees = []

def create_employee():
    emp_id = entry_id.get()
    name = entry_name.get()
    salary = entry_salary.get()

    employees.append([emp_id, name, salary])
    messagebox.showinfo("Success", "Employee Added Successfully")
    display_employees()

def update_employee():
    emp_id = entry_id.get()

    for emp in employees:
        if emp[0] == emp_id:
            emp[1] = entry_name.get()
            emp[2] = entry_salary.get()
            messagebox.showinfo("Success", "Employee Updated Successfully")
            display_employees()
            return

    messagebox.showerror("Error", "Employee Not Found")

def delete_employee():
    emp_id = entry_id.get()

    for emp in employees:
        if emp[0] == emp_id:
            employees.remove(emp)
            messagebox.showinfo("Success", "Employee Deleted Successfully")
            display_employees()
            return

    messagebox.showerror("Error", "Employee Not Found")

def display_employees():
    listbox.delete(0, END)

    for emp in employees:
        listbox.insert(
            END,
            f"ID:{emp[0]}  Name:{emp[1]}  Salary:{emp[2]}"
        )

root = Tk()
root.title("Employee Management System")
root.geometry("500x450")

Label(root, text="Employee ID").pack()
entry_id = Entry(root)
entry_id.pack()

Label(root, text="Employee Name").pack()
entry_name = Entry(root)
entry_name.pack()

Label(root, text="Salary").pack()
entry_salary = Entry(root)
entry_salary.pack()

Button(root, text="Create", command=create_employee).pack(pady=5)
Button(root, text="Update", command=update_employee).pack(pady=5)
Button(root, text="Delete", command=delete_employee).pack(pady=5)
Button(root, text="Display", command=display_employees).pack(pady=5)

listbox = Listbox(root, width=60)
listbox.pack(pady=10)

root.mainloop()
