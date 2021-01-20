from textblob import TextBlob

class GivePOSTags:
    """
    GivePOSTags

    Class that adds the part of speech tags to the each sentence in the list
    of sentences.

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
        self.sentences_with_tags = []

    def __add_tags(self):
        for sentence in self.list_of_sentences:
            _temp = {}
            _temp["sentence"] = sentence
            _tags = TextBlob(sentence).tags

            for tg in _tags:
                if tg[1] not in _temp:
                    _temp[tg[1]] = []
                _temp[tg[1]].append(tg[0])

            self.sentences_with_tags.append(_temp)

    def get_sentences_with_tags(self):
        """
        get_sentences_with_tags

        Returns:
            Dictionary: The schema is ->
                        {"sentence": <sentence>, "NNP": <NNP>}
                        All tags of the sentence in Key-Value pair
        """

        self.__add_tags()

        return self.sentences_with_tags
