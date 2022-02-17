'''
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

complexity = time: O(nlogn + n); space: O(n)
'''


def maximumUnits(boxTypes, truckSize) -> int:
    bxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
    print(bxTypes)
    sumT = 0
    remainder = truckSize
    for bx in bxTypes:
        remainder = remainder - bx[0]
        if remainder > 0:
            sumT += bx[1] * bx[0]
            old = remainder
        else:
            sumT += bx[1] * old
            break
    return sumT

result = maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10)
result = maximumUnits([[1,3],[2,2],[3,1]], 4)
print(result)