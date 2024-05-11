
def get_cats_info(path):
    with open(path) as file:
        lines = [el.strip() for el in file.readlines()]
        #print(lines)
    
    cats = []
    for line in lines:
        if line not in cats:
            id, name, age = line.split(',')
            cats.append({"id": id, "name": name, "age": age})
        
    return cats

cats_info = get_cats_info("task_2/cats_file.txt")
print(cats_info)