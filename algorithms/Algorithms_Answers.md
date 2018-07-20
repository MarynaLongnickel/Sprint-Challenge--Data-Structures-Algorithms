Add your answers to the Algorithms exercises here.

a) O(n)

b) O(log(n))

c) O(n)

d) O(nlog(n))

e) O(n^3)

f) O(n)

g) O(n)


II.

a)

def maxDiff(l):
    n = len(l)
    max_diff = l[1] - l[0]
    min_i = l[0]

    for i in range(1, n):
        if l[i] - min_i > max_diff:
            max_diff = l[i] - min_i

        if l[i] < min_i:
            min_i = l[i]
    return max_diff
    
 b)
 
 def drop(floors):

    m = [[0 for x in range(floors + 1)] for x in range(floors + 1)]

    for i in range(1, floors + 1):
        m[i][1] = 1

    for j in range(1, floors + 1):
        m[1][j] = j

    for i in range(2, floors + 1):
        for j in range(2, floors + 1):
            m[i][j] = floors + 1
            for x in range(1, j + 1):
                res = 1 + max(m[i - 1][x - 1], m[i][j - x])
                if res < m[i][j]:
                    m[i][j] = res

    return m[floors][floors]
    
  III.
  
  a) O(n) because the pivot will be each element in the list once
  
  b) O(nlog(n)) because first we have to find the median, which might be the last element in the list, and then sort, which splits the list in half each time.
    
