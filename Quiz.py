from Question import Question
from FillIn import FillIn
from Test import Test


class Quiz:
    def __init__(self , filePath):
        self.path = filePath
        self.questions = []
        self.loadQuestion()

    def loadQuestion(self):
        file = open(self.path , "r").read().split("\n")
        text = []

        for i in file:

            if i == '':

                if len(text) == 2:
                    q = Question(text[0] , text[1])
                    FillIn(q);
                    self.questions.append(q)
                elif len(text) == 6:
                    choices = text[1] + "\n" + text[2] +"\n"+ text[3] +"\n"+ text[4]
                    q = Question(text[0] , text[5] , answerChoices = choices)
                    Test(q)
                    self.questions.append(q)

                text.clear()
                continue

            text.append(i)

