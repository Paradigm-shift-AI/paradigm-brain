import random


class FillInTheBlanks:
    """
    Fill in the blanks

    Class to generate fill in the blanks type questions based on processed
    transcript. Replacing the proper nouns.

    Arguments:
        processed_transcript: dict;
    """

    def __init__(self, processed_transcript: dict):
        """
        __init__

        Arguments:
            processed_transcript: dict
        """
        self.processed_transcript = processed_transcript

    def __generate_options(self):
        self.options = set()
        for i in self.processed_transcript["processed-sentences"]:
            if 'NNP' in i:
                self.options.update(set(i['NNP']))
            if 'NN' in i:
                self.options.update(set(i['NN']))

    def __generate_question(self):
        """
        generate question


        Option are the list of proper noun and nouns from the
        processed_transcript. Question is generate by replacing the proper noun
        with a blank, and putting other nouns as options.
        """

        self.question = []

        for i in self.processed_transcript["processed-sentences"]:
            if 'NNP' in i and len(
                    self.options) >= 3 and i['NNP'][0] in self.options:
                _qu = {}
                _qu["type"] = 1
                _qu["question"] = i['sentence'].replace(i['NNP'][0], "_____")
                _qu["option1"] = i["NNP"][0]

                self.options.remove(i["NNP"][0])
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

    def questions(self):
        """
        Return List of FITB question:
            {
                "type": int
                "question": str,
                "option1": str,
                "option2": str,
                "option3": str,
                "option4": str
                "answer": str,
                "score": int
            }
        """
        self.__generate_options()
        self.__generate_question()

        return self.question
