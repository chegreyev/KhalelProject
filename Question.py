class Question:
    def __init__(self , description , answer , answerChoices = None):

        # Needed data
        self.description = description
        self.answer = answer

        # Only for Test class
        self.answerChoices = answerChoices

    def setDescription(self , description):
        self.description = description

    def setAnswerChoices(self , choices):
        self.answerChoices = choices

    def toString(self):
        return self.description + "\n" + self.answerChoices + "\n"


    def getDescription(self):
        return self.description