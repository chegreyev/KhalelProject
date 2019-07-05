from Question import Question


class Test(Question):
    def __init__(self , Question):
        self.question = Question

        self.answerChoices = Question.answerChoices

        self.getRightDescription()

    def getRightDescription(self):

        rawDescription = self.answerChoices.split("\n")

        rawText = ""
        choices = ["A) " , "B) " , "C) " , "D) "]
        counter = 0

        for i in rawDescription:
            rawText += choices[counter] + i + "\n"
            counter+=1

        self.question.setAnswerChoices(rawText)


