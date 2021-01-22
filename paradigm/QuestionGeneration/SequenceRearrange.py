import requests
import os

class SequenceRearrange:
    """
    SequenceRearrange

    Class that create SequenceRearrange question, it use the sequence defined in
    the plugin and the intersection of the tags discovered in the transcript to
    create the question

    Arguments:
        processed_transcript: dict
    """

    def __init__(self, processed_transcript: list, tokenid: str = None):
        """
        __init__

        Arguments:
            processed_transcript: dict
        """
        self.processed_transcript = processed_transcript
        self.question = []
        self.tokenid = tokenid

    def __generate_question(self):
        _req = requests.get(os.environ["PLUGIN_STORE_URL"] + self.tokenid + '/seq')

        if _req.status_code == 200:
            for i in _req.json()['seq']:
                _gh = True
                for j in i:
                    if j not in self.processed_transcript["tag-intersection"]:
                        _gh = False
                        break;
                if _gh:
                    _ques = {}
                    _inde = 1
                    for j in i:
                        _ques['option' + str(_inde)] = j
                        _inde += 1
                    _ques['score'] = len(i)
                    _ques['type'] = 5
                    self.question.append(_ques)


    def questions(self):
        """
        Returns question in the following format:
        {
        option1: <>,
        option2: <>,
        option3: <>,
        score: 3,
        type: 5
        }
        """
        if self.tokenid:
            self.__generate_question()
        return self.question
