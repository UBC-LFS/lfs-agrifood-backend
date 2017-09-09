# Class definition for Researcher object
class Researcher:

    def __init__(self, name, department, institution):
        self.name = name
        self.department = department
        self.institution = institution

    def getDocument(self):
        return {
            'name' : self.name,
            'department' : self.department,
            'institution' : self.institution
        }
