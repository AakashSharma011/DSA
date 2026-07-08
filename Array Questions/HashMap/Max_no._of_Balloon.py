text='bbbbblllllnnnnooooaaaaaaccccdddlloooaannbbbd'
class Solution(object):
    def maxNumberOfBalloons(self, text):
        hashmap = {}

        # Frequency count
        for ch in text:
            if ch in hashmap:
                hashmap[ch] += 1
            else:
                hashmap[ch] = 1

        return min(
            hashmap.get('b', 0),
            hashmap.get('a', 0),
            hashmap.get('l', 0) // 2,
            hashmap.get('o', 0) // 2,
            hashmap.get('n', 0)
        )
print(Solution().maxNumberOfBalloons(text))