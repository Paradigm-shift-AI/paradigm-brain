class Crossword:

    def __init__(self, processed_transcript: dict):
        self.processed_transcript = processed_transcript
        self.question = []

    def __generate_question(self):
        return 1

    def questions(self):
        self.__generate_question()
        return self.question
