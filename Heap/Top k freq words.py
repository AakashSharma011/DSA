from heapq import heappop,heappush
words = ["i","love","leetcode","i","love","coding"] 
k = 2
class Pairs:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def __lt__(self,other):
        if self.first!=other.first:
            return self.first<other.first
        else:
            return self.second>other.second

class Solution:
    def topKFrequent(self, words, k):
        freq={}
        for word in words:
            freq[word]=freq.get(word,0)+1
        heap=[]
        for word,count in freq.items():
            heappush(heap,Pairs(count,word))
            if len(heap)>k:
                heappop(heap)
        res=[]
        while heap:
            res.append(heappop(heap).second)
        return res[::-1]
print(Solution().topKFrequent(words,k))