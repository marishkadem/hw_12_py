import csv
from validate import Validate
from lesson import Lesson
class Student:

    name = Validate()
    second_name = Validate()
    surname = Validate()
    _lessons = None

    def __init__(self, name: str, second_name: str, surname: str, lessons_csv: str):
        self.name = name
        self.second_name = second_name
        self.surname = surname
        self._lessons = self.set_lessons(lessons_csv)

    def set_lessons(self, lessons_csv: str):
        self._lessons = {"lessons": []}
        with open(lessons_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                for i in row:
                    self._lessons["lessons"].append(Lesson(i,[],[]))
        return self._lessons

    def print_lessons(self):
        res = "\n"
        for i in self._lessons["lessons"]:
            res = res + i.lesson_name + " marks - " + str(i.get_marks()) + " tests_marks - " + str(i.get_tests_marks()) + "\n"
        return res

    def srednee_marks(self):
        res = 0
        count = 0
        for i in self._lessons["lessons"]:
            count += 1
            for j in i.get_marks():
                res += j
        try:
            return res / count
        except:
            return None

    def srednee_tests_marks(self):
        res_dict = {}
        for i in self._lessons["lessons"]:
            count = 0
            res = 0
            for j in i.get_tests_marks():
                count += 1
                res += j
            try:
                res_dict[i.lesson_name] = res / count
            except:
                res_dict[i.lesson_name] = None
        return res_dict

    def add_s_tests_marks(self, name, mark):
        for i in self._lessons["lessons"]:
            if name == i.lesson_name:
                i.add_tests_marks(mark)

    def add_s_marks(self, name, mark):
        for i in self._lessons["lessons"]:
            if name == i.lesson_name:
                i.add_marks(mark)

    def show_students(self):
        print(self.name, self.second_name, self.surname, self.print_lessons())
        print(self.srednee_marks())
        print(self.srednee_tests_marks())

if __name__ == "__main__":
    s1 = Student(name='Vasya', second_name='Pupkins', surname='Petrovich', lessons_csv="les.csv" )
    s1.add_s_marks("fizika", 5)
    print(s1._lessons["lessons"][0]._marks.append(5))
    print(s1._lessons["lessons"][1]._marks.append(2))
    s1.add_s_marks("fizika", 4)
    s1.add_s_tests_marks("fizika", 50)
    s1.add_s_tests_marks("fizika", 40)
    s1.show_students()