from pathlib import Path

path = Path("task-2/cats_file.txt") 

def get_cats_info(path):
    with open(path, "r") as file:
        lines = file.readlines()
    
    cats = {'id': '', 'name': '', 'age': ''}
    for line in lines:
        id, name, age = line.split(',')
        cats.update({"id": id, "name": name, "age": age})
        if line.strip():
            return cats

cats_info = get_cats_info("cats_file.txt")
print(cats_info)