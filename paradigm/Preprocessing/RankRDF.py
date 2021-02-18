from bisect import bisect_right
import requests
import os

class RankRDF:
    """
    RankRDF

    Class to find the intersection of tags specified by
    the plugin and the tags extracted from the transcript

    Arguments:
        tags: List of tags extracted from the text
        tokenid: String to uniquely identify the plugin
    """

    def __init__(self, tags: list, toeken_url: str, tokenid : str):
        self.tokenid = tokenid
        self.token_url = toeken_url
        self.tags = tags
        self.final_tags_intersection = []

    def __get_tags_from_plugin(self):
        _make_request = requests.get(self.token_url + self.tokenid)

        if _make_request.status_code == 200:
            self.list_from_plugin = _make_request.json()["tags"]
        elif _make_request == 403:
            raise Exception("Unautorized request for plugin.")
        else:
            raise Exception("Invalid plugin.")

    @staticmethod
    def __binary_search(elements: list, x: str):
        i = bisect_right(elements, x)
        if i != len(elements)+1 and (elements[i-1] == x or elements[i-1] in x.split()):
            return True
        else:
            return False

    def __find_intersection(self):
        for tag in self.tags:
            if self.__binary_search(self.list_from_plugin, tag):
                self.final_tags_intersection.append(tag)

    def get_tags_intersection(self, without_intersection = True):
        """
        get_tags_intersection

        Arguments:
            --NULL--

        Return:
            List of intersection of plugin tags and extracted Tags.
        """

        self.__get_tags_from_plugin()

        if without_intersection:
            return self.list_from_plugin

        self.__find_intersection()

        return self.final_tags_intersection
