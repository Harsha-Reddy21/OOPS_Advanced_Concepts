from datetime import datetime, timedelta
import re 


class Employee:
    company_name='Global Tech Solutions'
    total_employees=0
    departments={"Engineering":0, "Sales":0, "HR":0, "Marketing":0}
    tax_rates={"USA":0.22, "India":0.18, "UK":0.25}
    next_employee_id=1


    def __init__(self,name, department, base_salary, country,email):
        if not Employee.is_valid_department(department):
            raise ValueError("Invalid department")
        
        if not Employee.valid_email(email):
            raise ValueError("Invalid email")
        
        self.name=name
        self.department=department
        self.base_salary=base_salary
        self.country=country
        self.email=email
        self.hire_date=datetime.now()
        self.performance_ratings=[]

        self.employee_id=self.generate_employee_id()
        Employee.total_employees+=1
        Employee.departments[department]+=1

    @staticmethod
    def is_valid_department(department):
        print("department",department)
        print("Employee.departments",Employee.departments)
        print("department in Employee.departments",department in Employee.departments)
        return department in Employee.departments
    
    @staticmethod
    def valid_email(email):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return bool(re.match(pattern, email))
    
    @staticmethod
    def calculate_tax(salary,country):
        rate=Employee.tax_rates.get(country,0)
        return round(salary*rate,2)
    
    @staticmethod
    def generate_employee_id():
        year=datetime.now().year
        eid=f"EMP-{year}-{Employee.next_employee_id:04d}"
        Employee.next_employee_id+=1
        return eid
    
    

    
    @classmethod
    def from_csv_data(cls,csv_line):
        parts=csv_line
        print("parts",parts)
        print("len(parts)",len(parts))
        if len(parts)!=5:
            raise ValueError("Invalid CSV data")
        
        name,department,base_salary,country,email=parts
        return cls(name,department,base_salary,country,email)
    
    
    @classmethod
    def department_stats(cls):
        return {dept:count for dept,count in cls.departments.items()}
    
    @classmethod
    def set_tax_rate(cls,country,rate):
        if country not in cls.tax_rates:
            raise ValueError("Invalid country")
        cls.tax_rates[country]=rate
    
    @classmethod
    def hire_bulk_employees(cls,employee_lines):
        print("employee_lines",employee_lines)
        for line in employee_lines:
            print("line",line)
            cls.from_csv_data(line)


    
    def add_performance_rating(self,rating):
        if rating<1 or rating>5:
            raise ValueError("Invalid rating")
        self.performance_ratings.append(rating)
    
    def get_average_performance(self):
        if not self.performance_ratings:
            return 0
        return sum(self.performance_ratings)/len(self.performance_ratings)
    
    def calculate_net_salary(self):
        tax=Employee.calculate_tax(self.base_salary,self.country)
        return round(self.base_salary-tax,2)
    

    def get_years_of_service(self):
        delta=datetime.now()-self.hire_date
        return delta.days//365
    

    def is_eligible_for_bonus(self):
        return self.get_average_performance()>=3.5 and self.get_years_of_service()>=1
    


emp1=Employee("John Doe","Engineering",50000,"USA","john.doe@example.com")
assert emp1.employee_id.startswith("EMP-2025-")
assert Employee.total_employees==1
assert Employee.departments["Engineering"]==1


print(Employee.valid_email("test@company.com"))
assert Employee.valid_email("test@company.com")==True
assert Employee.valid_email("invalid-email")==False
assert Employee.is_valid_department("Engineering")==True
assert Employee.is_valid_department("Invalid")==False
assert abs(Employee.calculate_tax(100000,"USA")-22000)<0.01



emp2=Employee.from_csv_data("Sarah Johnson,HR,45000,India,sarah.johnson@example.com")
assert emp2.name=="Sarah Johnson"
assert emp2.department=="HR"
assert Employee.departments["HR"]==1


bulk_data=[
    ["Milk Wilson", "Engineering", 65000, "India", "mike.w@globaltech.com"],
    ["Lisa Chen", "HR", 70000, "USA", "lisa.chen@globaltech.com"]
]   

Employee.hire_bulk_employees(bulk_data)
assert Employee.total_employees==4


stats=Employee.get_department_stats()
assert stats["Engineering"]["count"]==1
assert stats['Sales']['count']==1


emp1.add_performance_rating(4.2)
emp1.add_performance_rating(3.8)
emp1.add_performance_rating(4.5)
assert abs(emp1.get_average_performance()-4.17)<0.01


emp1.hire_date=datetime.now()-timedelta(days=800)
assert emp1.get_years_of_service()>=2
assert emp1.is_eligible_for_bonus()==True


net_salary=emp1.calculate_net_salary()
expected_net=85000 - (85000*0.22)
assert abs(net_salary-expected_net)<0.01

