class Work:
    def __init__(self, place):
        self.place = place
    def work_info(self):
        print("Место работы:", self.place)
class Working_student(Work):
    def __init__(self, place, name, study_place):
        super().__init__(place)
        self.name = name
        self.study_place = study_place
    def information(self):
        self.work_info()
        print("Имя:", self.name)
        print("Место учёбы:", self.study_place)
student = Working_student("Автослесарь","Каплан","Сириус")
student.information()





