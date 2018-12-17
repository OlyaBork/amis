"""
Є студенти у групі. кожен студент має ім'я, назву групи , вік та бали з предметів. Вивести імена студентів.
 Вивести студента, що має оцінку з математики вищу ніж 3.
"""


dataset = {
    "student1": {
                "name": "Liza",
                "second name": "Boyko",
                "group": "KN-109",
                "subjects": {
                            "math": 5,
                            "English": 3,
                            "IT": 4
                            }
                },

    "student2": {
                "name": "Katya",
                "second name": "Kim",
                "group": "KN-108",
                "subjects": {
                             "math": 4,
                             "English": 5,
                             "IT": 4
                            }
                }
 }


def print_names(dataset, keys):
    if len(keys) == 0:
        return None
    key = keys[0]
    print(dataset[key]['name'])
    print_names(dataset, keys[1:])


def good_student(dataset, discipline):
    students = []
    for key in dataset:
        if dataset[key]['subjects'][discipline] >= 3:
            students.append(key)
    return students


keys = [key for key in dataset.keys()]
print_names(dataset, keys)

print(good_student(dataset, 'math'))
