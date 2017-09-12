class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """


    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.dicts=set(dict)
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for i, c in enumerate(word):
            for j in range(26):
                sub = chr(ord('a')+j)
                if sub == c:
                    continue
                newword = word[:i]+sub+word[i+1:]
                if newword in self.dicts:
                    return True
        return False
                    


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
