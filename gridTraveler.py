#uses recursion and memoization
#normal method
def gridTraveler(m,n):
    #base cases
    if m==0 or n==0: return 0
    if m==1 and n==1: return 1
    #down +right
    return gridTraveler(m-1, n) + gridTraveler(m, n-1)

#memoized method
def gridTraveler_mem(m,n, memo={}):
    key = (m, n)
    if m>n: key = (n,m)  #gridTraveller(a,b)= gridtraveler(b,a)
    if key in memo: return memo[key]
    if m==0 or n==0: return 0
    if m==1 and n==1: return 1
    #down +right
    memo[key] = gridTraveler_mem(m-1, n, memo) + gridTraveler_mem(m, n-1, memo)
    return memo[key]

print(gridTraveler_mem(2,3))
print(gridTraveler_mem(3,3))
print(gridTraveler_mem(6,6))
print(gridTraveler_mem(180,180))