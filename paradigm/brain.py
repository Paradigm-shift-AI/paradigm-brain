from Preprocessing import Preprocess
from QuestionGeneration import TrueFlase, FillInTheBlanks, MultipleCorrect, IntergerType, SequenceRearrange
import Selection
import json
import random

def qwrite(a, att):
    with open("res{}_{}.json".format(att, random.randint(1, 10**6)), "w") as f:
        f.write(json.dumps(a))
        f.close()

def qread():
    with open("res_text.txt", "r") as f:
        fg = f.read()
        fg = fg.replace("\n", " ")
    return fg

if __name__ == '__main__':

    att = random.randint(1, 1000)

    pr = Preprocess.Preprocess(qread()).get_processed_sentences()
    qwrite(pr, att)

    tf = TrueFlase.TrueFalse(pr)
    fb = FillInTheBlanks.FillInTheBlanks(pr)
    mc = MultipleCorrect.MultipleCorrect(pr)
    ind = IntergerType.IntergerType(pr)

    li = {1: fb.questions(), 2: tf.questions(), 3: mc.questions(), 4: ind.questions()}
    qwrite(li, att)

    fg = Selection.Selection(pr, li).get_final_question()
    qwrite(fg, att)
