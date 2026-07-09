ransomNote = "aa"
magazine = "aab"
def canConstruct(ransomNote, magazine):
        hashmap={}
        for ch in magazine:
            if ch in hashmap:
                hashmap[ch]+=1
            else:
                hashmap[ch]=1
        for ch in ransomNote:
            if ch  not in hashmap:
                return False
            hashmap[ch]-=1
            if hashmap[ch]<0:
                return False
        return True
print(canConstruct(ransomNote, magazine))