def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), '分支必须是树'
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)
    #
    return len(branches(tree)) == 0

t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
print(t)
#[3, [1], [2, [1], [1]]]
print(label(t))
print(branches(t))
print(label(branches(t)[1]))
print(is_leaf(t))
print(is_leaf(branches(t)[0]))

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        return tree(label(left) + label(right), [left, right])

print(fib_tree(5))

print(sum([1, 5, 6, 3]))
print(sum(range(9), 8))
print(sum([[3, 4], [5]], []))
#sum([[3, 4],[5]])不行

print(max([2, 4, 5, 6, 9]))
print(max(range(5)))
print(max(range(9), key=lambda x: 7-(x-2)*(x-4)))

print(all([x < 9 for x in range(9)]))

def count_tree(t):
    if is_leaf(t):
        return 1
    else:
        branch_tree = [count_tree(b) for b in branches(t)]
        return sum(branch_tree)

print(count_tree(fib_tree(5)))

def leaves(tree):
    """Return a list containing the leaf labels of tree
    
    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    """
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])
    
print(leaves(fib_tree(5)))\

def increment_tree(t):
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_tree(b) for b in branches(t)]
        return tree(label(t), bs)
    
def increment(t):
    return tree(label(t) + 1, [increment(b) for b in branches(t)])

def print_tree(t, indent=0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent+1)

print_tree(fib_tree(5))

haste = tree('h', [tree('a', [tree('s'),
                              tree('t')]),
                   tree('e')])

def print_sums(t, so_far):
    so_far = so_far + label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far)

print_sums(haste, '')

def count_paths(t, total):
    """Return the number of paths from the root to any node in tree t
    for which the labels along the path sum to total.
    
    >>> t = tree(3, [tree(-1), tree(1, [tree(2, [tree(1)]), tree(3)]), tree(1, [tree(-1)]))
    >>> count_paths(t, 3)
    2
    >>> count_paths(t, 4)
    2
    >>> count_paths(t, 5)
    0
    >>> count_paths(t, 6)
    1
    >>> count_paths(t, 7)
    2
    """
    if label(t) == total:
        found = 1
    else:
        found = 0
    return found + sum([count_paths(b, total - label(t)) for b in branches(t)])