# question

class Question:
    def __init__(self, text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self, answer):
        return self.answer == answer


# print(q1.checkAnswer("python"))
# print(q2.checkAnswer("c#"))
# print(q3.checkAnswer("Java"))

# quiz

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1 } : {question.text}")    

        for q in question.choices:
            print("-"+ q)

        answer = input("cevap : ")
        answer = answer.lower()    
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

        
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()


    def showScore(self):
        print(f"Quiz bitti. Puanınız: {quiz.score}")

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1


        if questionNumber > totalQuestion:
            print("Quiz Bitti.")
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(100,"*"))    





q1 = Question("en iyi program dili hangisidir ?" , ["C#", "Python", "Javascript", "Java"], "python")
q2 = Question("en popüler program dili hangisidir ?" , [ "Python", "Javascript","C#", "Java"], "python")
q3 = Question("en çok kazandıran program dili hangisidir ?" , ["C#",  "Javascript", "Python","Java"], "python")
q4 = Question("en kolay program dili hangisidir ?" , [ "Python", "Javascript","C#", "Java"], "python")
q5 = Question("en sevilen  program dili hangisidir ?" , ["C#",  "Javascript", "Python","Java"], "python")

questions = [q1, q2, q3, q4, q5]           

quiz = Quiz(questions)
question = quiz.getQuestion()
quiz.displayQuestion()