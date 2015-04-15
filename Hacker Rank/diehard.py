from fractions import gcd
t = input()
assert 1 <= t <= 100
for i in range(t):
    a, b, c = map(int, raw_input().strip().split(' '))
    assert 1 <= a <= 1e3
    assert 1 <= b <= 1e3
    assert 1 <= c <= 1e3
    x = gcd(a, b)
    if c % x == 0 and (c <= a or c <= b):
        print "YES"
    else:
        print "NO"