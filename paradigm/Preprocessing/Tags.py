from rake_nltk import Rake

class Tags:
    """
    Tags: Class encapsulates the rake nltk library

    Methods:
        get_ranked_phrases( String )
    """

    def __init__(self, text: str):
        """
        __init__

        Arguments:
            text: String; The text to be summarized.
        """

        self.rake = Rake()
        self.rake.extract_keywords_from_text(text)

    def get_ranked_phrases(self):
        """
        get_ranked_phrases()

        Arguments:
            --NULL--

        Returns:
            List: sorted list of keywords in the text.
        """

        return self.rake.get_ranked_phrases()
