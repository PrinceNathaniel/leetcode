class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        wordList=set(wordList)
        cur = [beginWord]
        visited = set([beginWord])
        count = 1
        while cur:
            nextcur = []
            for word in cur:
                if word == endWord:
                    return count
                for i in range(len(word)):
                    for j in 'qwertyuiopasdfghjklzxcvbnm':
                        possibleword = word[:i]+j+word[i+1:]
                        if possibleword not in visited and possibleword in wordList:
                            nextcur.append(possibleword)
                            visited.add(possibleword)
            count+=1
            cur = nextcur
        return 0
