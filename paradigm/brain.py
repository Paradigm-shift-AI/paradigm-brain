from Preprocessing import Preprocess
from QuestionGeneration import TrueFlase, FillInTheBlanks, MultipleCorrect, IntergerType, SequenceRearrange


if __name__ == '__main__':
    text = "Systems engineers coordinate the creation, maintenance and growth of a business or organization's computer systems. They coordinate each department's needs, suggest technical direction, and set up any networks that link up computers with the company. Being a software engineer is a great career choice for someone who is exceptionally good at both left and right-brained thinking (analytical skills as well as problem-solving skills). Software engineers are instinctive problem-solvers, good at working with others and focused on seeing issues through to their successful completion."

    # text = "Contribution, maintenance of github"
    text = "Three functions are called that are, on create, on start, on resume"
    td = """
    because-- just as, you know, 1,000
    05:07
    was a big number a couple of decades ago,
    05:09
    and now it's kind of a small number-- it's
    05:12
    quite possible that by the time you guys are professors
    05:16
    teaching this class in some university
    05:18
    that a trillion is going to be a small number.
    05:20
    And we're going to be talking about-- I don't know--
    05:24
    10 raised to 18 as being something
    05:27
    that we're concerned with from a standpoint of a common case
    05:32
    input for an algorithm.
    05:34
    So scalability is important.
    05:38
    And we want to be able to track how our algorithms are going
    05:41
    to do as inputs get larger and larger.
    05:44
    05:47
    You going to learn a bunch of different data structures.
    05:52
    We'll call them classic data structures,
    05:56
    like binary search trees, hash tables-- that
    06:01
    are called dictionaries in Python-- and data
    06:06
    structures-- such as balanced binary search trees-- that
    06:09
    are more efficient than just the regular binary search trees.
    06:12
    And these are all data structures
    06:14
    that were invented many decades ago.
    06:18
    But they've stood the test of time,
    06:20
    and they continue to be useful.
    06:23
    We're going to augment these data structures in various ways
    06:26
    to make them more efficient for certain kinds of problems.
    06:30
    And while you're not going to be doing a whole lot of algorithm
    06:33
    design in this class, you will be
    06:36
    doing some design and a whole lot of analysis.
    06:38
    06:40
    The class following this one, 6.046 Designing Analysis
    06:46
    of Algorithms, is a class that you
    06:48
    should take if you like this one.
    06:52
    And you can do a whole lot more design of algorithms in 6.046.
    06:57
    But you will look at classic data structures
    06:59
    and classical algorithms for these data structures,
    07:06
    including things like sorting and matching, and so on.
    07:12
    And one of the nice things about this class
    07:17
    is that you'll be doing real implementations of these data
    07:21
    structures and algorithms in Python.
    07:25
    07:28
    And in particular are each of the problem
    07:30
    sets in this class are going to have both a theory
    07:38
    part to them, and a programming part to them.
    07:41
    So hopefully it'll all tie together.
    07:43
    The kinds of things we're going to be talking about in lectures
    07:46
    and recitations are going to be directly connected
    07:51
    to the theory parts of the problem sets.
    07:53
    And you'll be programming the algorithms that we talk about
    07:55
    in lecture, or augmenting them, running them.
    07:58
    Figuring out whether they work well on large inputs or not.
    08:03
    08:06
    So let me talk a little bit about the modules
    08:09
    in this class and the problem sets.
    08:11
    And we hope that these problem sets
    08:12
    are going to be fun for you.
    08:15
    And by fun I don't mean easy.
    08:19
    I mean challenging and worthwhile, so at the end of it
    08:22
    you feel like you've learned something,
    08:24
    and you had some fun along the way.
    08:26
    All right?
    08:28
    So content wise--
    08:30
    08:37
    --we have eight modules in the class.
    08:41
    Each of which, roughly speaking, has
    08:44
    a problem set associated with it.
    08:47
    The first of these is what we call algorithmic thinking.
    08:51
    08:55
    And we'll kick start that one today.
    08:59
    We'll look at a particular problem, as I mentioned,
    09:01
    of peak finding.
    09:02
    And as part of this, you're going
    09:04
    to have a problem set that's going to go out today as well.
    09:07
    And you'll find that in this problem set
    09:12
    some of these algorithms I talk about today will
    09:14
    be coded in Python and given to.
    09:17
    A couple of them are going to have bugs in them.
    09:20
    You'll have to analyze the complexity of these algorithms;
    09:24
    figure out which ones are correct and efficient;
    09:27
    and write a proof for one of them.
    09:29
    All right?
    09:30
    So that's sort of an example problem set.
    09:33
    And you can expect that most of the problem sets
    09:37
    are going to follow that sort of template.
    09:40
    All right.
    09:40
    So you'll get a better sense of this
    09:44
    by the end of the day today for sure.
    09:46
    Or a concrete sense of this, because we'll
    09:48
    be done with lecture and you'll see your first problem set.
    09:52
    We're going to be doing a module on sorting and trees.
    09:57
    Sorting you now about, sorting a bunch of numbers.
    10:00
    Imagine if you had a trillion numbers
    """



    text = ""
    for i in td.split("\n"):
        a = i.strip()
        try:
            if not a[2] == ":":
                a = a.replace("-", "")
                text += a
                text += " "
        except Exception as e:
            pass

    pr = Preprocess.Preprocess(text, "vedang").get_processed_sentences()
    # tf = TrueFlase.TrueFalse(pr)
    # fb = FillInTheBlanks.FillInTheBlanks(pr)
    # mc = MultipleCorrect.MultipleCorrect(pr)
    # ind = IntergerType.IntergerType(pr)
    # {"FillInTheBlanks": fb.questions(), "TrueFalse": tf.questions(), "MultipleCorrect": mc.questions(), "IntergerType": ind.questions()}
    # print(pr)
    # sq = SequenceRearrange.SequenceRearrange(pr, "vedang")
    import json
    with open('res2.json', 'w') as f:
        f.write(text)
    # print(fb.questions())
