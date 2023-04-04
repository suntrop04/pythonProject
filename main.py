groupmates = [
    {
        "name": "Алексей",
        "surname": "Иванов",
        "exams": ["БЖ", "Метрология","ИТиП","СИИ","МСиП",],
        "marks": [4, 3, 5, 5, 3]
    },
    {
        "name": "Ваня",
        "surname": "Петров",
        "exams": ["БЖ", "Метрология","ИТиП","СИИ","МСиП",],
        "marks": [4, 4, 4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["БЖ", "Метрология","ИТиП","СИИ","МСиП",],
        "marks": [5, 5, 5, 5, 5]
    },
    {
        "name": "Марк",
        "surname": "Владов",
        "exams": ["БЖ", "Метрология","ИТиП","СИИ","МСиП",],
        "marks": [5, 5, 5, 5, 5]
    },
    {
        "name": "Леня",
        "surname": "Петров",
        "exams": ["БЖ", "Метрология","ИТиП","СИИ","МСиП",],
        "marks": [5, 5, 5, 5, 5]
    }
]
def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(43), u"Оценки".ljust(20), u"средняя оценка".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20), str(student["middle"]).ljust(20))
def searchMiddle():
    search = float(input("средняя оценка"))
    new_group = []
    for students in groupmates:
        middle = sum(students['marks'])/len(students['marks'])
        if(middle > search):
            students['middle'] = middle
            new_group.append(students)
    print_students(new_group)

searchMiddle()