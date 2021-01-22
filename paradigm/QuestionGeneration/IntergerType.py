from word2number import w2n
import copy


class IntergerType:
    """
    IntergerType

    Class to generate IntergerType questions, by replacing numeric values in
    the text, using NLTK and word2number python package

    Arguments:
        processed_sentences: dict
    """

    def __init__(self, processed_sentences: dict):
        """
        __init__

        Arguments:
            processed_sentences
        """
        self.processed_sentences = processed_sentences
        self.question = []


    def __generate_question(self):
        """
        generate question

        Traverse through the list of numeric words and adjectives
        """
        for i in self.processed_sentences['processed-sentences']:
            if 'CD' in i:
                for _jk in i['CD']:
                    _ques = {}
                    _ques['question'] = i['sentence'].replace(str(_jk), "____")
                    try:
                        _ques['answer'] = w2n.word_to_num(str(_jk))

                        if not isinstance(_ques['answer'], int) or _ques['answer'] == 1:
                            raise Exception

                        _ques['score'] = 1
                        _ques['type'] = 4
                        self.question.append(_ques)
                    except:
                        continue
            elif 'JJ' in i:
                for _jk in i['JJ']:
                    _ques = {}
                    _ques['question'] = i['sentence'].replace(str(_jk), "____")
                    try:
                        _ques['answer'] = w2n.word_to_num(str(_jk))

                        if not isinstance(_ques['answer'], int) or _ques['answer'] == 1:
                            raise Exception

                        _ques['score'] = 1
                        _ques['type'] = 4
                        self.question.append(_ques)
                    except:
                        continue



    def questions(self):
        """
        Returns question in the following format
        {
        question: <>,
        answer: <int>,
        score: 1,
        type: 4
        }

        """
        self.__generate_question()
        return self.question
