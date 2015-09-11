#!/usr/bin/python


dp = {}
# l needs to be sorted
# l is a list of nimbers.
def mex(l):
    res = 0
    for a in l:
        if res == a:
            res += 1
    return res

def possibleMoves(n, k):
    if n == 0:
        return []
    l = []
    for i in xrange(n):
        if i + 1 == k:
            continue
        l.append((n - i - 1, i + 1))
    return l

def nimber(n, k):
    if dp.get((n,k)) is not None:
        return dp.get((n,k))
    l = [nimber(n1,k1) for (n1,k1) in possibleMoves(n,k)]
    l.sort()
    res = mex(l)
    dp[(n,k)] = res
    return res

def exhaustive(n):

    for i in xrange(n):
        print "n:", "{0:2d}".format(i), "|",
        for j in range(i):
            print "{0:2d}".format(nimber(i,j)),
        print "{0:2d}".format(nimber(i,i))

def search(target, n):
    for i in xrange(n):
        for j in xrange(i):
            if (nimber(i,j) == target):
                print i,j, i - j
def search_specific(target, n, diff):
        for i in xrange(n):
            if i < diff or i % 2 == 0:
                continue
            if nimber(i, i - diff) != target:
                print i
def single_line(n):
    for j in range(n):
        print "{0:2d}".format(nimber(n,j)),
    print "{0:2d}".format(nimber(n,n))
def dosearch(mode):
    n = input('Enter the maximal n to search to: ')
    if mode == 1:
        exhaustive(n)
    elif mode == 2:
        target = int(input('Target: '))
        search(target, n)
    elif mode == 3:
        target = input('Target: ')
        diff = input('Diff: ')
    elif mode == 4:
        single_line(n)
    elif mode == 5:
        k = input('k: ')
        play(n, k, True)
def selectBest(n, k):
    moves = possibleMoves(n, k)
    for m in moves:
        (a,b) = m
        if nimber(a,b) == 0:
            return n - a
    (a,b) = moves[0]
    return n - a
def play(n, k, isComputer):
    print 'n: {0:d}, k: {1:d}, nimber: {2:d}.'.format(n,k, nimber(n,k))
    if n == 0:
        print "Terminal position reached."
        return
    if (isComputer):
        move = selectBest(n, k)
    else:
        move = input('move: ')
    n-= move
    k = move

    play(n, k, not isComputer)
def searchForNimber(nimber_target, n):
    for i in xrange(n):
        for j in xrange(i):
            if nimber(i,j) == nimber_target:
                print i,j, i - j
        if nimber(i,i) == nimber_target:
            print i,i,0
print """This program will print the nimbers for a single pile of stones in our variant of Nim.
The piles are represented in in the format (n,k), where
n is the number of stones remaining in the pile, and k is the number of stones removed in the
last move. As a reminder, if k stones were taken from the pile in the last move,
you cannot take k stones until a different number of stones are taken.
          """
while True:

    print "Display Format: (value of n) | (nimbers for k = 0,1,2,...n-1, seperated by spaces)"
    mode = 1
    while mode not in [1,2,3,4,5]:
        mode = int(input('1/2/3/4/5(exhaustive, search, search_specific, single_line, play):\n'))
    dosearch(mode)
