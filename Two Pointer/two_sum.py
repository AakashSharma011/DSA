class Solution(object):
    def findTarget(self, root, k):

        asc = []
        desc = []

        # Leftmost path
        node = root
        while node:
            asc.append(node)
            node = node.left

        # Rightmost path
        node = root
        while node:
            desc.append(node)
            node = node.right

        def getSmall():
            node = asc.pop()

            temp = node.right
            while temp:
                asc.append(temp)
                temp = temp.left

            return node

        def getBig():
            node = desc.pop()

            temp = node.left
            while temp:
                desc.append(temp)
                temp = temp.right

            return node

        i = getSmall()
        j = getBig()

        while i != j:
            s = i.val + j.val

            if s == k:
                return True
            elif s > k:
                j = getBig()
            else:
                i = getSmall()

        return False