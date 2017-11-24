# Class definition for Researcher object
class Researcher:

    def __init__(self, name, department, institution, orcid):
        self.name = name
        self.department = department
        self.institution = institution
        # Adding the same random OrcID for testing purposes TODO: Fix this later
        self.orcid = "0000-0003-0392-0702"

    def getDocument(self):
        return {
            'name' : self.name,
            'department' : self.department,
            'institution' : self.institution,
            'orcid' : self.orcid
        }
