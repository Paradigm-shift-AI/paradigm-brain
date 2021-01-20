class MultipleCorrect:

    def __init__(self, processed_transcript: list):
        """
        __init__

        Arguments:
            processed_transcript: dict
        """

        self.processed_transcript = processed_transcript
        self.question = []

    @staticmethod
    def __format_string(st: str):
        _st = ""
        _stopwords = ",.!@#$%^&*()_+-=;<>?/"
        for i in st:
            if i in _stopwords:
                _st += i
        return _st


    def __generate_question(self):
        for i in self.processed_transcript['sentences']:
            _formatted_sentence = self.__format_string(i)



    def questions():
        self.question
