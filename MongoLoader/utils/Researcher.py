# Class definition for Researcher object
class Researcher:

    # TODO: Actually make use of the orcid input once we have valid orcids in the database
    def __init__(self, name, department, institution, orcid):
        self.name = name
        self.department = department
        self.institution = institution
        # TODO: This is not good, but there is no other way to handle this currently
        if (name == 'Rickey Y. Yada'):
            self.orcid = '0000-0002-8648-2156'
        else:
            self.orcid = None

    def getDocument(self):
        return {
            'name' : self.name,
            'department' : self.department,
            'institution' : self.institution,
            'orcid' : self.orcid
        }
