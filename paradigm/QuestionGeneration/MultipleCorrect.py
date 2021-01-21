import random
from textblob import TextBlob
import copy

class MultipleCorrect:
    """
    MultipleCorrect

    Class to generate more than one correct question
    Arguments:
        processed_transcript: dict
    """

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
        """Remove special characters"""
        _st = ""
        _stopwords = ",.!@#$%^&*()_+-=;<>?/"
        for i in st:
            if i not in _stopwords:
                _st += i
        return _st


    def __generate_question(self):
        """
        Looks for the following patters:

        {<JJ><JJ><JJ>}
        {<JJ><CC><JJ>
        {<JJ><JJ>}
        {<NN><NN>}
        """


        for i in self.processed_transcript['processed-sentences']:
            _formatted_sentence = self.__format_string(i['sentence']).split()
            _temp_list = []

            if 'JJ' in i:
                for j in i['JJ']:
                    if j in _formatted_sentence:
                        _temp_list.append(_formatted_sentence.index(j))

            _temp_list.sort()
            print(_temp_list)

            _to_replace = []
            for k in range(1, len(_temp_list)):
                if _temp_list[k] == _temp_list[k-1] + 1:
                    if _temp_list[k-1] == _temp_list[k-2] + 1:
                        _to_replace.append([_temp_list[k-2], _temp_list[k-1], _temp_list[k]])
                    else:
                        _to_replace.append([_temp_list[k-1], _temp_list[k]])
                elif _temp_list[k] == _temp_list[k-1] + 2:
                    if _formatted_sentence[_temp_list[k-1]+1] in i['CC']:
                        _to_replace.append([_temp_list[k], _temp_list[k-1]])

            for kl in _to_replace:
                _ques = {}
                _vb = copy.deepcopy(_formatted_sentence)
                _rest_option = i['JJ']

                _igh = 1
                for _gh in kl:
                    _ques['option' + str(_igh)] = _formatted_sentence[_gh]
                    if _formatted_sentence[_gh] in _rest_option:
                        _rest_option.remove(_formatted_sentence[_gh])
                    _ques['answer' + str(_igh)] = _formatted_sentence[_gh]
                    _vb[_gh] = "_____"
                    _igh += 1

                _ques['question'] = " ".join(_vb)

                if _igh == 3 or _igh == 4:
                    for _jk in i['JJ']:
                        if _jk != _ques['option1'] and _jk != _ques['option2']:
                            _ques['option' + str(_igh)] = _jk
                            _igh += 1
                        if _igh == 5:
                            break

                if _igh == 4:
                    _ques['option4'] = "None of these"

                if _igh == 3:
                    _extra_list = []
                    if 'NN' in i:
                        _extra_list += i['NN']
                    if 'NNP' in i:
                        _extra_list += i['NNP']
                    if 'NNS' in i:
                        _extra_list += i['NNS']
                    _ques['option3'] = random.choice(_extra_list)
                    _ques['option4'] = "None of these"

                _ques['score'] = len(_ques) - 5
                _ques['type'] = 3
                self.question.append(_ques)



    def questions(self):
        """
        Returns question in the format
        {
        question: <>,
        option1: <>,
        option2: <>,
        option3: <>,
        option4: <>,
        answer1: <>,
        answer2: <>,
        answer3: <>,
        score: <len(answer)>
        type: 3
        }

        """

        self.__generate_question()
        return self.question