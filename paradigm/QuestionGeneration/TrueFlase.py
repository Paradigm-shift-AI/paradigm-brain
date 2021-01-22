import en_core_web_sm
import requests
import os
import random
import nltk
from nltk.corpus import wordnet


class TrueFalse:
    """
    True and False

    Class to generate fill in the blanks type questions based on processed
    transcript. Replacing the proper nouns.

    Arguments:
        processed_transcript: dict;
    """

    def __init__(self, processed_transcript: list, tokenid: str = None):
        """
        __init__

        Arguments:
            processed_transcript: dict
        """

        self.processed_transcript = processed_transcript
        self.nlp = en_core_web_sm.load()
        self.tokenid = tokenid
        self.question = []

    @staticmethod
    def __get_replacement_from_plugin(tokenid: str, type: str):
        """
        RDF provides related replacements for a particular kind of word.
        Example: Person, organization names.
        """
        _req = requests.get(os.environ["PLUGIN_STORE_URL"] + tokenid +"/"+type)

        if _req.status_code == 200:
            return _req.get()["data"]
        return None

    @staticmethod
    def __get_antonym(word: str):
        """Provides the antonym of an adjective."""
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                if l.antonyms():
                    return l.antonyms()[0].name()
        return None

    def __named_entity_recognition(self):
        """
        Named entity are recognized and randomly replaced
        by related words, using RDF.
        """

        for i in self.processed_transcript["processed-sentences"]:
            _doc = self.nlp(i['sentence'])
            for X in _doc.ents:
                _rep = None
                if self.tokenid:
                    _rep = self.__get_replacement_from_plugin(self.tokenid, X.label_)
                if _rep:
                    _to_flip = random.choice([0, 1])
                    _ques = {}
                    if _to_flip == 1:
                        _ques["question"] = i['sentence'].replace(X.text, _rep)
                        _ques["answer"] = False
                    else:
                        _ques["question"] = i['sentence']
                        _ques["answer"] = True
                    _ques["score"] = 1
                    _ques["type"] = 2
                    self.question.append(_ques)

    def __adjective_replacement(self):
        """Adjective are replaced with their antonyms randomly."""

        for i in self.processed_transcript["processed-sentences"]:
            if "JJ" in i:
                _ran = random.choice(i['JJ'])
                _rep = self.__get_antonym(_ran)
                if _rep:
                    _to_flip = random.choice([0, 1])
                    _ques = {}
                    if _to_flip == 1:
                        _ques["question"] = i['sentence'].replace(_ran, _rep)
                        _ques["answer"] = False
                    else:
                        _ques["question"] = i['sentence']
                        _ques["answer"] = True
                    _ques["score"] = 1
                    _ques["type"] = 2
                    self.question.append(_ques)

    def __generate_question(self):
        if self.tokenid:
            self.__named_entity_recognition()
        self.__adjective_replacement()

    def questions(self):
        """
        Returns List of question in the format

        {
            question: <>,
            answer: True/False,
            score: 1,
            type: 2
        }
        """
        self.__generate_question()
        return self.question
