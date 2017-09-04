class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        s,e = 0, 0
        res,n = [],0
        for i, word in enumerate(words):
            if len(word)+n+e-s>maxWidth:
                if e-s == 1:
                    res.append(words[s]+' '*(maxWidth-n))
                else:
                    totalspace = maxWidth-n
                    space, remain = divmod(totalspace, e-s-1)
                    for j in range(remain):
                        words[s+j] +=' '
                    res.append((' '*space).join(words[s:e]))
                n = 0
                s = e = i
            e+=1
            n+=len(word)
        res.append(' '.join(words[s:e])+' '*(maxWidth-n-(e-s-1)))
        return res
