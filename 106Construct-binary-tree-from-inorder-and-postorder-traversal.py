class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        maps= {}
        i = 0
        for num in inorder:
            maps[num] = i
            i+=1
        return self.recur(inorder,postorder,len(postorder)-1,0,len(inorder),maps)
    def recur(self,inorder,postorder,postpos,inorderstart,inorderend,maps):
        if inorderstart == inorderend:
            return None
        node = TreeNode(postorder[postpos])
        index = maps[postorder[postpos]]
        node.left = self.recur(inorder,postorder,postpos-(inorderend-index),inorderstart,index,maps)
        node.right = self.recur(inorder,postorder,postpos-1,index+1,inorderend,maps)
        return node
