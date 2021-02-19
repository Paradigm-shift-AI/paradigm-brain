from .Preprocessing import Preprocess
from .QuestionGeneration import TrueFlase, FillInTheBlanks, MultipleCorrect, IntergerType, SequenceRearrange
from . import Selection
import json
import random
import os

class Brain:

    def __init__(self, text: str, token_url = None, token_id = None, fill_in_the_blanks = True, true_or_false = True, multiple_corrent = True, interger_type = True):
        self.text = text
        self.pr = Preprocess.Preprocess(self.text, token_url, token_id).get_processed_sentences()
        self.li = {}

        if true_or_false:
            self.tf = TrueFlase.TrueFalse(self.pr)
            self.li[1] = self.tf.questions()


        if fill_in_the_blanks:
            self.fb = FillInTheBlanks.FillInTheBlanks(self.pr)
            self.li[2] = self.fb.questions()

        if multiple_corrent:
            self.mc = MultipleCorrect.MultipleCorrect(self.pr)
            self.li[3] = self.mc.questions()

        if interger_type:
            self.ind = IntergerType.IntergerType(self.pr)
            self.li[4] = self.ind.questions()

        self.fg = Selection.Selection(self.pr, self.li, True).get_final_question()

    def generate_question(self):
        return self.fg
