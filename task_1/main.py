def load_data(path: str) -> list[str]:
    with open(path) as file:
        lines = file.readlines()
    res = {'name': '', 'salary': ''}
    for line in lines:
        if line.strip():
            name, salary = line.split(',')
            res.update({"name": name, "salary": salary})
        return res
    return load_data(path)

def total_salary(path):
    load_data(path)
    def calculated_salary(salary: str) -> int:
        total = 0
        for number in int({"salary": salary}):
            total += number
        average = total  / len(int({"salary": salary}))
        return total, average
    calculated_salary(path)
total, average = total_salary("task_1/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")