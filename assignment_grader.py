
class Grader:
    def __init__(self, file_name):
        """
        Constructor
        """

        self.subjects = []
        self.student_database = {}
        self.subject_database = {}
        self.process_file(file_name)

    def process_file(self, fileName):

        file = open(fileName)
        for i, line in enumerate(file.readlines()):
            line = line.strip()
            content = line.split(',')
            if i > 0:
                # list comprehension version
                self.student_database[content[0].lower()] = [int(grade) for grade in content[1:]]

                # FULL for  loop version
                # self.student_database[content[0].lower()] = []
                # for grade in content[1:]:
                #     self.student_database[content[0].lower()].append(grade)

                for subject, score in zip(self.subjects, content[1:]):
                    self.subject_database[subject].append(int(score))
            else:
                self.subjects = content[1:]
                for subject in self.subjects:
                    self.subject_database[subject] = []
        file.close()

    def students_avg_score(self):
        for name in self.student_database.keys():
            print('{}\'s average score is {:.2f}'.format(name, self.avg_score_per_student(name)))

    def subjects_avg_score(self):
        for name in self.subject_database.keys():
            print('{}\'s average score is {:.2f}'.format(name, self.avg_score_per_subject(name)))

    def avg_score_per_subject(self, name):
        scores = self.subject_database[name.lower()]
        return sum(scores)/len(scores)

    def avg_score_per_student(self, name):
        scores = self.student_database[name.lower()]
        return sum(scores) / len(scores)


def test():

    grader = Grader("student_info.csv")
    grader.students_avg_score()
    print()
    grader.subjects_avg_score()


test()
