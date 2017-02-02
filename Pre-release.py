class Test(object):
    def __init__(self):
        self.TestID = ''
        self.Questions = []
        self.NumberOfQuestions = 0
        self.MaxMarks = 0
        self.Level = ''
        self.DateSet = "" #Date variable add later

    def DesignTest(self):
        n = 0
        question = input("Question: ")
        while(not question.isspace() and question):
            self.Questions.append(Question())
            answer = input("Answer: ")
            marks = input("Marks: ")
            self.MaxMarks += int(marks)
            topic = input("Topic: ")
            self.Questions[n].SetQuestion(n, question, answer, marks, topic)
            n += 1
            if n == 10:
                break
            
            question = input("Question: ")

          
        self.NumberOfQuestions = n
        self.Level = input("Level: ")

    def PrintTest(self):
        for q in self.Questions:
            question = str(q.QuestionID) + ': ' + q.QuestionText
            print(question)

    def PrintAnswers(self):
        for q in self.Questions:
            answer = str(q.QuestionID) + ': ' + q.Answer
            print(answer)


class Question(object):
    def __init__(self):
        QuestionID = ''
        QuestionText = ""
        Answer = ""
        Marks = 0
        Topic = ''

    def SetQuestion(self, ID, text, answer, marks, topic):
        self.QuestionID = ID
        self.QuestionText = text
        self.Answer = answer
        self.Marks = marks
        self.Topic = topic

    def GetQuestion(self):
        return self.QuestionText

    def GetMarks(self):
        return self.Marks

    def GetTopic(self):
        return self.Topic

    def GetAnswer(self):
        return self.Answer

test = Test()
test.DesignTest()
test.PrintTest()
test.PrintAnswers()
print(test.MaxMarks)
input()
