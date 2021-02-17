import random

class Selection:

    def __init__(self, preprocessed_question, list_of_questions):
        """
        list_of_questions:
        [
            questionTypeID: [<question_object>],
        ]
        """

        self.preprocessed_question = preprocessed_question
        self.list_of_questions = list_of_questions
        self.final_question = []

    def __get_proper_noun(self):
        jk = set()
        for j in self.preprocessed_question["processed-sentences"]:
            if "NNP" in j:
                for k in j["NNP"]:
                    jk.add(k)
        return list(jk)

    def __select_fill_in_blanks(self):
        for i in self.list_of_questions[1]:
            if i["answer"] in self.__get_proper_noun():
                self.final_question.append(i)

    def __select_true_or_false(self, type):
        for i in self.list_of_questions[type]:
            for j in self.preprocessed_question["tag"][0:5]:
                if j in i["question"]:
                    self.final_question.append(i)

    def __select_multiple_correct(self):
        for i in self.list_of_questions[3]:
            if i["answer1"] in self.__get_proper_noun():
                if i["answer2"] in self.__get_proper_noun():
                    self.final_question.append(i)

    def __select_relevant_question(self):

        def f(questionType):
            return {
                1: self.__select_fill_in_blanks(),
                2: self.__select_true_or_false(2),
                3: self.__select_multiple_correct(),
                4: self.__select_true_or_false(4)
            }[questionType]

        for questionType in [2, 3, 4, 5]:
            if questionType in self.list_of_questions:
                f(questionType)

        if len(self.final_question) > 2:
            random.shuffle(self.final_question)
            self.final_question = self.final_question[0:2]


    def get_final_question(self):
        self.__select_relevant_question()
        return self.final_question
