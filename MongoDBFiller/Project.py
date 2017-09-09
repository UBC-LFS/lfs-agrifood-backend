# Class definition for Project object
class Project:

    def __init__(self, title, department, institution, summary, start, end, funding, topic, listResearchers):
        self.title = title
        self.department = department
        self.institution = institution
        self.summary = summary
        self.start = start
        self.end = end
        self.funding = funding
        self.topic = topic
        self.listResearchers = listResearchers

    def getDocument(self, researcherIDs):
        return {
            'title': self.title,
            'department': self.department,
            'institution': self.institution,
            'summary': self.summary,
            'start': self.start,
            'end': self.end,
            'funding': self.funding,
            'topic': self.topic,
            'researchers': researcherIDs
        }
