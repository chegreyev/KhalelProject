from Question import Question


class FillIn(Question):

    def __init__(self , Question):

        self.question = Question
        self.description = Question.description

        self.getRightDescription()

    def getRightDescription(self):
        self.question.setDescription(self.description.replace("{blank}" , "_____"))

