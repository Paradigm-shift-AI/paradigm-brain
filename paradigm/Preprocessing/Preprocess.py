import Tags
import RankRDF
import getSentences
import Grammar
import POSTag


class Preprocess:
    """
    Preprocess

    Main class, acts as an entrypoint to Preprocess the text.
    Combines, integrates all the other class of the module.

    Arguments
        text: string; The text to be Preprocessed
        Tokenid: string; ID of the plugin used.
    """

    def __init__(self, text: str, tokenid: str = None):
        """
        __init__

        Arguments:
            text: string; The text to be Preprocessed
            Tokenid: string; ID of the plugin used.
        """

        self.text = text
        self.tokenid = tokenid

    def __process_text(self):
        self.results = {}
        self.results["tag"] = Tags.Tags(self.text).get_ranked_phrases()

        if self.tokenid is not None:
            self.results["tag-intersection"] = RankRDF.RankRDF(
                self.results["tag"], self.tokenid).get_tags_intersection()

        self.results["processed-sentences"] = POSTag.GivePOSTags(
            Grammar.Grammar(
                getSentences.ExtractedSentences(
                    self.text).get_processed_sentences()).get_processed_sentences()).get_sentences_with_tags()

    def get_processed_sentences(self):
        """
        get_processed_sentences

        Returns:
            Dictionary object of the following format
            {"tags": keywords in the text,
             "tags-intersection": Intersection of keywords from the plugin,
             "processed-sentences": List of sentences, find its schema in
              preprocess.py }
        """
        self.__process_text()

        return self.results
