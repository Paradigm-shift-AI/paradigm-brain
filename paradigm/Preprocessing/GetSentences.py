import urllib.request
from bs4 import BeautifulSoup
import spacy
import neuralcoref
from nltk.tokenize import sent_tokenize


class ExtractedSentences:
    """
    ExtractedSentences

    Class to preprocess the sentences. Preprocessing happens in two ways
    1. The corefrence is resolved using scapy and neuralcoref
    2. The text is tokenized into separate sentences.

    Arguments:
        text: String; The transcipt generally.
    """

    def __init__(self, text: str):
        """
        __init__

        Arguments:
            text: str
        """

        self.text = text
        self.nlp = spacy.load('en_core_web_lg')
        neuralcoref.add_to_pipe(self.nlp)

    def __resolve_coreference(self):
        _doc = self.nlp(self.text)
        self.resolved_text = _doc._.coref_resolved

    def __tokenize_sentences(self):
        self.tokenized_sentences = sent_tokenize(self.resolved_text)

    def get_processed_sentences(self):
        """
        Function returns the processed sentences list

        Returns:
            List of strings
        """

        self.__resolve_coreference()
        self.__tokenize_sentences()

        return self.tokenized_sentences
