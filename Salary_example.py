import pandas as pd

# Sample data with Indian names for salary analysis
data = {
    'Name': ['Amit', 'Priya', 'Ravi', 'Sneha', 'Vikas', 'Kiran', 'Rahul', 'Meena'],
    'Age': [25, 45, 35, 28, 42, 50, 33, 40],
    'Department': ['HR', 'Finance', 'IT', 'HR', 'IT', 'Finance', 'IT', 'HR'],
    'Position': ['Manager', 'Analyst', 'Developer', 'Recruiter', 'Developer', 'Manager', 'Developer', 'Manager'],
    'Years_of_Experience': [2, 15, 7, 3, 12, 20, 5, 10],
    'Salary': [50000, 80000, 75000, 52000, 95000, 120000, 70000, 85000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display basic information about the dataset
print("Dataset Information:")
print(df.info())
print("\nBasic Statistics:")
print(df.describe())

# Calculate the average salary
average_salary = df['Salary'].mean()
print(f"\nAverage Salary: ₹{average_salary:.2f}")

# Group by department and calculate average salary per department
avg_salary_department = df.groupby('Department')['Salary'].mean()
print("\nAverage Salary by Department:")
print(avg_salary_department)

# Find the highest and lowest salary
highest_salary = df['Salary'].max()
lowest_salary = df['Salary'].min()
print(f"\nHighest Salary: ₹{highest_salary}")
print(f"Lowest Salary: ₹{lowest_salary}")

# Calculate the average salary by position
avg_salary_position = df.groupby('Position')['Salary'].mean()
print("\nAverage Salary by Position:")
print(avg_salary_position)

# Analyze salary by years of experience
experience_salary_corr = df['Years_of_Experience'].corr(df['Salary'])
print(f"\nCorrelation between Years of Experience and Salary: {experience_salary_corr:.2f}")

# Filter employees with salaries above the average
high_salary_employees = df[df['Salary'] > average_salary]
print("\nEmployees with Salary Above Average:")
print(high_salary_employees)

# Identify departments with employees having more than 10 years of experience
experienced_employees = df[df['Years_of_Experience'] > 10]
print("\nDepartments with Employees having more than 10 years of experience:")
print(experienced_employees['Department'].unique())
