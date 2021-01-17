import random

class FillInTheBlanks:

    def __init__(self, processed_transcript: str):
        self.processed_transcript = processed_transcript

    def __generate_options(self):
        self.options = set()
        for i in self.processed_transcript["processed-sentences"]:
            if 'NNP' in i:
                self.options.add(i['NNP'])
            if 'NN' in i:
                self.options.add(i['NN'])

    def __generate_question(self):
        self.question = []

        for i in self.processed_transcript["processed-sentences"]:
            if 'NNP' in i and len(self.options) >= 3:
                _qu = {}
                _qu["question"] = i['sentence'].replace(i['NNP'], "_____")
                _qu["option1"] = i["NNP"]

                self.options.remove(i["NNP"])
                _qu["option2"] = random.sample(self.options, 1)[0]

                self.options.remove(_qu["option2"])
                _qu["option3"] = random.sample(self.options, 1)[0]

                self.options.remove(_qu["option3"])
                _qu["option4"] = "None of the above"

                if len(self.options) >= 1:
                    _qu["option4"] = random.sample(self.options, 1)[0]

                _qu["answer"] = _qu["option1"]
                _qu["score"] = 1

                self.question.append(_qu)


    def question(self):
        self.__generate_options()
        print(self.options)
        self.__generate_question()

        return self.question
