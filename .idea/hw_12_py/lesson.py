class Lesson:

    lesson_name = None
    _tests_marks = []
    _marks = []

    def __init__(self, lesson_name, test_marks:list, marks:list):
        self.lesson_name = lesson_name
        self._tests_marks = test_marks
        self._marks = marks

    def add_marks(self, value):
        if value in range(2,6):
            self._marks.append(value)
        return self._marks

    def add_tests_marks(self, value):
        if value in range(0,101):
            self._tests_marks.append(value)
        return self._tests_marks

    def get_marks(self):
        return self._marks

    def get_tests_marks(self):
        return self._tests_marks

    def lesson_print(self):
        print(self.lesson_name)
        print(self._marks)
        print(self._tests_marks)


if __name__ == '__main__':
    math = Lesson("math")
    math.add_marks(99)
    for i in range(0,10):
        math.add_tests_marks(i)
        math.add_marks(i)
    math.lesson_print()
