
def load_data(path: str) -> list[str]:
    with open(path) as file:
        lines = [el.strip() for el in file.readlines()]

    res = []
    for line in lines:
        if line not in res:
            name, salary = line.split(',')
            res.append({"name": name, "salary": salary})
    return res  

def list_of_salary(file_path) -> list[int]:
    data = load_data(file_path)
    salary_list = []
    for person in data:
        salary = person.get('salary')
        salary_list.append(salary)
        continue                
    return salary_list

 
def total_salary(file_path) -> list[int]:
    data = list_of_salary(file_path)
    total = 0
    average = 0
    for salary in data:
        print(salary)
        total += int(salary)
        average = total  / len(data)
    return total, average
  

total, average = total_salary("task_1/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")