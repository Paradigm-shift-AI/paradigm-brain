import language_tool_python

class Grammar:
    """
    Grammar

    Class rectifies grammatical mistakes and spelling errors using
    language_tool_python.

    Arguments:
        list_of_sentences: List
    """

    def __init__(self, list_of_sentences: list):
        """
        __init__

        Arguments:
            list_of_sentences: List
        """

        self.list_of_sentences = list_of_sentences
        self.processed_list_of_sentences = []
        self.tool = language_tool_python.LanguageTool('en-US')

    def __rectify_grammar(self):
        for sentence in self.list_of_sentences:
            self.processed_list_of_sentences.append(self.tool.correct(sentence))

    def get_processed_sentences(self):
        """
        get_processed_sentences

        Returns:
            List of string.
        """
        self.__rectify_grammar()

        return self.processed_list_of_sentences
