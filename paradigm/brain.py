from Preprocessing import Preprocess
from QuestionGeneration import TrueFlase, FillInTheBlanks, MultipleCorrect, IntergerType


if __name__ == '__main__':
    text = "Systems engineers coordinate the creation, maintenance and growth of a business or organization's computer systems. They coordinate each department's needs, suggest technical direction, and set up any networks that link up computers with the company. Being a software engineer is a great career choice for someone who is exceptionally good at both left and right-brained thinking (analytical skills as well as problem-solving skills). Software engineers are instinctive problem-solvers, good at working with others and focused on seeing issues through to their successful completion."

    # text = "Contribution, maintenance of github"
    text = "There are eighty one countries in the world."
    pr = Preprocess.Preprocess(text).get_processed_sentences()
    # tf = TrueFlase.TrueFalse(pr, "abs")
    # fb = FillInTheBlanks.FillInTheBlanks(pr)
    # mc = MultipleCorrect.MultipleCorrect(pr)
    print(pr)
    ind = IntergerType.IntergerType(pr)

    print(ind.questions())
