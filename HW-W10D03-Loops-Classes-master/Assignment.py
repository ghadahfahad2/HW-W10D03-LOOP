class Assignment:
    def __init__(self,name,github_url,completed,grade ):
        self.github_url=github_url
        self.name=name
        self.completed=False
        self.grade=None

    def mark_done(grade):
        self.grade=grade
        self.completed=True


class Student():
    def __init__(self,name,pending_homeworks ,completed_homeworks ):
        self.name=name
        self.pending_homeworks=[]
        self.completed_homeworks=[]
    
    def assign_homework(self,Assignment ):
        self.pending_homeworks.append(Assignment)

    def complete_homework(self,HomeWorkName,grade):
        for homwork in self.pending_homeworks:
            if homwork == HomeWorkName:
                self.pending_homeworks.remove(HomeWorkName)
                self.completed_homeworks.append(HomeWorkName)
                Assignment.mark_done(grade)
                return True
            else:
                return False

    
    def print_outstanding_homeworks(self):
        for name in self.pending_homeworks:
            print(name)


class SeiClass(Student) :
    def __init__(self,name):
        self.name=name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def assign_homework(self, assignment1):
        self.pending_homeworks.append(assignment1)
    

nick = Student('Nick')
sarah = Student('Sarah')
brandi = Student('Brandi')

sei30 = SeiClass('sei30')
sei30.add_student(nick)
sei30.add_student(sarah)
sei30.add_student(brandi)

assignment1 = Assignment('Bounty Hunters', 'https://github.com/WDI-SEA/mongoose-practice')

sei30.assign_homework(assignment1)

nick.complete_homework('Bounty Hunters', 98)
sarah.complete_homework('Bounty Hunters', 95)

nick.print_outstanding_homeworks()
sarah.print_outstanding_homeworks()
brandi.print_outstanding_homeworks()