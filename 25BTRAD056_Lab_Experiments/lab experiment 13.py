import csv

file = open("employees.csv", "r")

reader = csv.DictReader(file)

total = 0

print("Payroll Report")

for row in reader:
    name = row["Name"]
    salary = float(row["Salary"])
    hra = salary * 0.10
    deduction = salary * 0.05
    gross = salary + hra
    net = gross - deduction
    total += net

    print("\nEmployee:", name)
    print("Gross Salary:", gross)
    print("Deduction:", deduction)
    print("Net Salary:", net)

print("\nTotal Payroll:", total)

file.close()
