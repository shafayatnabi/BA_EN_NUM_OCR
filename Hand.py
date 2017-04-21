def array_left_rotation(a, n, k):
    temp=a[0:k]
    temp1=a[k:n]
    temp1.extend(temp)
    return temp1

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str, answer))


def check_binary_search_tree_(root):
    if root is None:
        return True
    if check_duplicate(root.data, root) == False:
        return False
    if root.left is not None and check_lesser(root.data, root.left) == False:
        return False
    if root.right is not None and check_greater(root.data, root.right) == False:
        return False
    if check_binary_search_tree_(root.left) == False:
        return False
    if check_binary_search_tree_(root.right) == False:
        return False
    if root.right is not None and root.data >= root.right.data:
        return False
    if root.left is not None and root.data <= root.left.data:
        return False
    return True


def check_duplicate(value, root):
    if root.left is not None and root.left.data == value:
        return False
    if root.right is not None and root.right.data == value:
        return False
    if root.right is not None and check_duplicate(value, root.right) == False:
        return False
    if root.left is not None and check_duplicate(value, root.left) == False:
        return False
    return True


def check_greater(value, root):
    if root.left is not None and root.left.data < value:
        return False
    if root.right is not None and root.right.data < value:
        return False
    if root.right is not None and check_greater(value, root.right) == False:
        return False
    if root.left is not None and check_greater(value, root.left) == False:
        return False
    return True


def check_lesser(value, root):
    if root.left is not None and root.left.data > value:
        return False
    if root.right is not None and root.right.data > value:
        return False
    if root.right is not None and check_lesser(value, root.right) == False:
        return False
    if root.left is not None and check_lesser(value, root.left) == False:
        return False
    return True
