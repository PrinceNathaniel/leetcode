#O(m * n * k), where m is string length, n is dictionary size, k is word length
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res, nums, charlen = [], len(words), len(words[0])
        dicts = collections.defaultdict(int)
        for word in words:
            dicts[word] += 1
        
        for i in range(len(s)+1-nums*charlen):
            cur, j = collections.defaultdict(int), 0
            while j < nums:
                word = s[i+j*charlen:i+(j+1)*charlen]
                if word not in dicts:
                    break
                cur[word]+=1
                if cur[word] > dicts[word]:
                    break
                j += 1
            if j == nums:
                res.append(i)
        return res
 #method 2
 #O(n * k*2)
 class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
          # Create a list for results.
        wordFoundIndices = []


        lengthOfWord = len(words[0])

        lengthOfs = len(s)

        lengthOfSubstring = lengthOfWord*len(words)

        # Creates a dictionary to keep desired number count of all the words found in the string value.
        wordCounterDict = collections.defaultdict(int)
        for word in words:
                wordCounterDict[word] += 1


        # Get the range of loop. Go from 0 to the last character 
        for i in xrange(min(lengthOfWord, lengthOfs-lengthOfSubstring+1)):

            wordStartIndex = i

            stringStartIndex = i

            wordsSeenDict = collections.defaultdict(int)

            while stringStartIndex + lengthOfSubstring <= lengthOfs:

                word = s[wordStartIndex:wordStartIndex+lengthOfWord]
                wordStartIndex += lengthOfWord

                # Checks if current word is part of the list.
                if(word in wordCounterDict):
                    wordsSeenDict[word] += 1


                    # Checks if word seen is now more than required.
                    while(wordsSeenDict[word]>wordCounterDict[word]):

                        # Delete all the previous words seen from this i.
                        wordsSeenDict[s[stringStartIndex:stringStartIndex+lengthOfWord] ] -=1

                        # Increments string start to skip all the values before.
                        stringStartIndex+=lengthOfWord

                    # Checks if the the last word index subracts the string start index is equal total length of the string.
                    if wordStartIndex - stringStartIndex == lengthOfSubstring:
                        wordFoundIndices.append(stringStartIndex)

                else:

                    # Resets everything.
                    stringStartIndex = wordStartIndex  

                    # Clears words seen dictionary.
                    wordsSeenDict.clear()                    

        return wordFoundIndices
