class Color:
    BLACK = 'BLACK'
    RED = 'RED'


def right_swap(node):
    right_child = node.right
    between_child = right_child.left
    right_child.left = node
    node.right = between_child
    right_child.color = node.color
    node.color = Color.RED
    return right_child


def left_swap(node):
    left_child = node.left
    between_child = left_child.right
    left_child.right = node
    node.left = between_child
    left_child.color = node.color
    node.color = Color.RED
    return left_child


def color_swap(node):
    node.right.color = Color.BLACK
    node.left.color = Color.BLACK
    node.color = Color.RED


def rebalance(node):
    result = node
    need_rebalance = True
    while need_rebalance:
        need_rebalance = False
        if result.right is not None and result.right.color is Color.RED and \
            (result.left is None or result.left.color is Color.BLACK):
            need_rebalance = True
            result = right_swap(result)
        elif result.left is not None and result.left.color is Color.RED and \
            result.left.left is not None and result.left.left.color is Color.RED:
            need_rebalance = True
            result = left_swap(result)
        elif result.left is not None and result.left.color is Color.RED and \
            result.right is not None and result.right.color is Color.RED:
            need_rebalance = True
            color_swap(result)
    return result


class RBTree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, value):
            self.value = value
            self.color = None
            self.right = None
            self.left = None

    def exist(self, value):
        node = self.find_node(self.root, value)
        return node is not None

    def find_node(self, node, value):
        if node is None:
            return None
        elif node.value > value:
            return self.find_node(node.left, value)
        else:
            return self.find_node(node.right, value)

    def add(self, value):
        if self.root is not None:
            result = self.add_node(self.root, value)
            root = rebalance(self.root)
            root.color = Color.BLACK
            return result
        else:
            root = RBTree.Node(value)
            root.color = Color.BLACK
            root.value = value
            return True

    def add_node(self, node, value):
        if node.value is value:
            return False
        else:
            if node.value > 0:
                if node.left is not None:
                    result = self.add_node(node.left, value)
                    node.left = rebalance(node.left)
                    return result
                else:
                    node.left = RBTree.Node(value)
                    node.left.color = Color.RED
                    node.left.value = value
                    return True
            else:
                if node.right is not None:
                    result = self.add_node(node.right, value)
                    node.right = rebalance(node.right)
                    return result
                else:
                    node.right = RBTree.Node(value)
                    node.right.color = Color.RED
                    node.right.value = value
                    return True

if __name__ == '__main__':
    tree = RBTree()
    nums = [2, 3, 7, 24, 32, 19, 4, 12, 34]
    for i in nums:
        tree.add(i)