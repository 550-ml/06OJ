# 树的BFS
![例题](/source/pic/LeetCode/03Search/02树的BFS.png)
```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        val = []
        current = []
        nex = []
        current.append(root)
        while current:
            temp = []
            for node in current:
                if node.left: nex.append(node.left)
                if node.right: nex.append(node.right)
                temp.append(node.val)
            val.append(temp)
            current = nex
            nex = []
        return val
```

## 其他方法
- 可以把cur和nex合并起来，使用一种数据结构：队列。3+5+3
- 三个数据结构：ans,visit,q=deque()
- 5是5个操作：
- 3是三个循环：while q:for _ in range(len(q)): for i in range(4)
```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        # 3
        val = []
        visit = []
        q = deque([root])
        # 5 and 3
        while q:
            tmp = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                tmp.append(node.val)
            val.append(tmp)
        return val
```
