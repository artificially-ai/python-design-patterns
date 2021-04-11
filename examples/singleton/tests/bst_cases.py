from examples.singleton.logging import Logger
from examples.singleton.tests.binary_tree import TreeNode

from collections import deque

# Creating several of those. The logs should print the object and the stdout IDs as well.
logger_1 = Logger()


def create_inorder(flat_tree, root, index, length):
    if index < length:
        root = TreeNode(val=flat_tree[index])
        root.left = create_inorder(flat_tree, root.left, 2 * index + 1, length)
        root.right = create_inorder(flat_tree, root.right, 2 * index + 2, length)

    return root


def tree_height(node):
    if node is None:
        return 0
    else:
        left_height = tree_height(node.left)
        right_height = tree_height(node.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1


def traverse_level_order(root, queue):
    # Creating several of those. The logs should print the object and the stdout IDs as well.
    logger_3 = Logger()
    logger_3.info('Traversing the tree, level-order style: breadth first.')

    if not root:
        return queue

    aux_queue = deque()
    aux_queue.append(root)
    while aux_queue:
        curr_node = aux_queue.popleft()
        if curr_node.left:
            aux_queue.append(curr_node.left)
        if curr_node.right:
            aux_queue.append(curr_node.right)
        queue.append(curr_node.val)


def traverse_pre_order(root, queue):
    logger_2.info('Traversing the tree, pre-order style: depth first.')
    if root:
        queue.append(root.val)
        traverse_pre_order(root.left, queue)
        traverse_pre_order(root.right, queue)


if __name__ == '__main__':
    # Creating several of those. The logs should print the object and the stdout IDs as well.
    logger_2 = Logger()

    """
    Create a binary tree.
    """
    flat_tree = range(1, 11, 1)
    tree = create_inorder(flat_tree, None, 0, len(flat_tree))

    """
    Traverse the tree depth first
    """
    aux_queue = deque()
    traverse_pre_order(tree, aux_queue)
    for e in aux_queue:
        logger_1.info(e)

    """
    Traverse the tree breadth first
    """
    # Creating several of those. The logs should print the object and the stdout IDs as well.
    logger_4 = Logger()
    aux_queue = deque()
    traverse_level_order(tree, aux_queue)
    for e in aux_queue:
        logger_4.info(e)
