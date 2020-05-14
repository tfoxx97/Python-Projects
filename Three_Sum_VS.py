# author: Tyler Elenberger
# created: 3/24/2020

def ThreeSum(nums):
    result = set([])
    plus = sorted([i for i in nums if i>0])
    plus_c = set(plus)
    zero = sorted([i for i in nums if i==0])
    minus = sorted([i for i in nums if i<0])
    minus_c = set(minus)
    if len(zero) > 2:
        result.add((0,0,0))
    if len(zero) > 0:
        for n in minus:
            if -n in plus_c:
                result.add((-n,0,n))
    n = len(minus)
    for i in range(n):
        for j in range(i+1, n):
            diff = -(minus[i] + minus[j])
            if diff in plus_c:
                result.add((minus[i], minus[j], diff))
    n = len(plus)
    for i in range(n):
        for j in range(i+1, n):
            diff = -(plus[i] + plus[j])
            if diff in minus_c:
                result.add((diff, plus[i], plus[j]))
    return list(result)

x = ThreeSum([-1, -2, 5, 4, -2, 0, 0, 0, 4, 3, 6, -9, -11, 6, 5, 20, -18, 99, 73, -2])
print(x)
