def pathSum(self, root, targetSum):
    res=[]
    path=[]
    def dfs(node,curr_sum):
        if node is None:
            return
        path.append(node.val)
        curr_sum+=node.val
        if node.left is None and node.right is None :
            if curr_sum==targetSum:
                res.append(path[:])
        else:
            dfs(node.left,curr_sum)
            dfs(node.right,curr_sum)
        path.pop()
    dfs(root,0)
    return res