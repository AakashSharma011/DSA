s = "AABABBA"
k = 1
def characterReplacement(self, s, k):
        left=0
        freq={}
        ans=0
        for right in range(len(s)):
            if s[right] in freq:
                freq[s[right]]+=1
            else:
                freq[s[right]]=1
            max_freq = max(freq.values())
        # freq[s[right]]=freq.get(s[right],0)+1
            while (right-left+1)-max_freq>k:
                freq[s[left]]-=1
                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1
            ans=max(ans,right-left+1)
        return ans

print(characterReplacement(0, s, k))