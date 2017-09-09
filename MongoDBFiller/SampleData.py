from Researcher import Researcher
from Project import Project

# If you want to add more examples to populate the database, add new Researcher and Project objects here. Remember to
# append them to the allSampleResearchers and allSampleProjects lists for them to be added to the DB.
researcherEric = Researcher('Eric Jang', 'Computer Science', 'University of British Columbia')
researcherJoe = Researcher('Joe Smith', 'School of Environmental Design & Rural Development', 'Vancouver Agricultural College')
researcherAnn = Researcher('Ann Williams', 'School of Agriculture', 'Simon Fraser University')

projectFoodIsCool = Project('Food is Cool', 'Land and Food Systems', 'University of British Columbia', 'Did you know that food is cool?',
                            'Feb 23, 2002', 'March 12, 2006', 'Ministry of Education', 'Food', [researcherEric])
projectAgricultureIsAmazing = Project('Agriculture is Amazing', 'School of Agriculture', 'Simon Fraser University',
                                      'This project explains why agriculture is amazing.', 'June 4, 2004', 'Sept 23, 2005',
                                      'VAFA', 'Agriculture', [researcherAnn, researcherJoe])

allSampleResearchers = [researcherEric, researcherJoe, researcherAnn]
allSampleProjects = [projectFoodIsCool, projectAgricultureIsAmazing]

