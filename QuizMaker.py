from Quiz import Quiz


class QuizMaker:

    pathToFile = "/Users/ChD/PycharmProjects/Khalel/quiz.txt"

    def __init__(self):
        self.quiz = Quiz(filePath=self.pathToFile)
        self.questions = self.quiz.questions
        self.length = len(self.questions)
        self.rightAnswers = 0

    def welcomeText(self):
        print("WELCOME TO PYTHON QUIZ!")
        self.printLine()

    def printLine(self):
        print("----------------------------------------------\n")

    def start(self):

        # TO CHANGE

        self.counter = 0
        self.welcomeText()

        for i in range(self.length):
            self.printQuestion(i+1)

        print("Your score is : " + str(self.rightAnswers) + "/" + str(self.length) + " . ")


    def printQuestion(self , numerator):
        if self.questions[self.counter].answerChoices is None:
            print(str(numerator)+ ")  " + self.questions[self.counter].getDescription())
            self.checkAnswer(self.questions[self.counter])
            self.printLine()
            self.counter += 1
        else:
            print(str(numerator)+ ")  " + self.questions[self.counter].toString())
            self.checkAnswer(self.questions[self.counter])
            self.printLine()
            self.counter += 1

    def checkAnswer(self ,question):

        userA = input("Your answer is : ")

        if userA == question.answer:
            print("\nCorrect!")
            self.rightAnswers += 1
        else:
            print("\nIncorrect!")

quizmaker = QuizMaker().start()