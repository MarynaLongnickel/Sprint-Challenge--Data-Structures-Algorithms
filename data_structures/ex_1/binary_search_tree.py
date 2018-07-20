class Node:
    def __init__(self, value=None, L=None, R=None):
        self.value = value
        self.L = L
        self.R = R


class BinarySearchTree:
    def __init__(self, root=None, L=None, R=None):
        self.root = Node(root)
        self.L = L
        self.R = R

    def depth_first_for_each(self):
        nodes = []
        stack = [self.root]
        while stack:
            cur_node = stack.pop(0)
            if cur_node not in nodes:
                nodes.append(cur_node)
                if cur_node.L:
                    if cur_node.L not in nodes:
                        stack.append(cur_node.L)
                if cur_node.R:
                    if cur_node.R not in nodes:
                        stack.append(cur_node.R)
        return [n.value for n in nodes]

    def breadth_first_for_each(self):
        nodes = []
        stack = [self.root]
        while stack:
            cur_node = stack[0]
            if cur_node is None: break
            stack = stack[1:]
            nodes.append(cur_node)
            if cur_node.L: stack.append(cur_node.L)
            if cur_node.R: stack.append(cur_node.R)
        return [n.value for n in nodes]

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if node.value > value:
            if node.L is None:
                node.L = Node(value)

            else:
                self._insert(node.L, value)
        else:
            if node.R is None:
                node.R = Node(value)
            else:
                self._insert(node.R, value)

    def contains(self, target):
        if self.root is None:
            return None
        node = self.root
        while node is not None:
            if node.value == target:
                return True
            if target >= node.value:
                node = node.R
            else:
                node = node.L
        return False

    def get_max(self):
        if self.root is None:
            return None
        node = self.root
        while node.R is not None:
            node = node.R
        return node.value
