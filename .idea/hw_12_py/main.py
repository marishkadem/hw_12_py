from student import Student

s1 = Student(name='Vasya', second_name='Pupkins', surname='Petrovich', lessons_csv="les.csv" )
s1.add_s_marks("fizika", 5)
s1._lessons["lessons"][0]._marks.append(5)
s1._lessons["lessons"][1]._marks.append(2)
s1.add_s_marks("fizika", 4)
s1.add_s_tests_marks("fizika", 50)
s1.add_s_tests_marks("fizika", 40)
s1.show_students()