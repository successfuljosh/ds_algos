#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'valuation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER reqArea
#  2. LONG_INTEGER_ARRAY area
#  3. LONG_INTEGER_ARRAY price
#
# calculate standard deviation
def std(data):
    if len(data) <= 1:
        return 0
    mean = sum(data) / len(data)
    diff_sq = [(x - mean) ** 2 for x in data]
    diff_sum = sum(diff_sq)
    st_dev = math.sqrt(diff_sum / (len(data) - 1))
    return st_dev


def removeOutlier(area, price):
    dict_ap = {area[i]:price[i] for i in range(len(area))}
    print(dict_ap)
    new_area = []
    new_price = []
    for i in range(len(area)):
        current_area = area[i]
        current_price = price[i]
        comp_list = []
        for j in range(i + 1, len(area)):
            if area[j] == current_area:
                comp_list.append(price[j])
        if len(comp_list) == 0:
            new_area.append(int(current_area))
            new_price.append(int(current_price))
        else:
            p_m = sum(comp_list) / len(comp_list)
            std_dev = std(comp_list)
            diff = abs(current_price - p_m)
            if not diff > 3 * std_dev:
                new_area.append(int(current_area))
                new_price.append(int(current_price))

    return new_area, new_price


def check_boundary(ans):
    ans = int(ans)
    if ans < 10 ** 3:
        return 10 ** 3
    if ans > 10 ** 6:
        return 10 ** 6
    return ans


def valuation(reqArea, area, price):
    # Write your code here
    n_area, n_price = removeOutlier(area, price)

    if n_area == None or len(n_area) == 0:
        ans = reqArea * 1000
        return check_boundary(ans)

    if len(n_area) == 1:
        a = int(n_price[0])
        return check_boundary(a)

    index_req = [i for i in range(len(n_area)) if n_area[i] == reqArea]
    if len(index_req) >= 1:
        prices = [n_price[i] for i in index_req]
        ans = sum(prices) / len(prices)
        return check_boundary(ans)

    # interpolation
    area_price = [(n_area[i], n_price[i]) for i in range(len(n_area))]
    area_price.sort(key=lambda k: k[0])
    # interpolation
    for i in range(0, len(area_price) - 1):
        current = area_price[i]
        next_a = area_price[i + 1]
        if reqArea < current[0] and reqArea < next_a[0]:
            ans = current[1] + (reqArea - current[0]) * ((next_a[1] - current[1]) / (next_a[0] - current[0]))
            return check_boundary(ans)

    # extrapolation from the right
    if reqArea > area_price[-1][0]:
        ans = area_price[-2][1] + (reqArea - area_price[-2][0]) * (
                    (area_price[-1][1] - area_price[-2][1]) / (area_price[-1][0] - area_price[-2][0]))
        return check_boundary(ans)

        # extrapolation from the left
    if reqArea < area_price[0][0]:
        ans = area_price[1][1] - (area_price[1][0] - reqArea) * (
                    (area_price[1][1] - area_price[0][1]) / (area_price[1][0] - area_price[0][0]))
        return check_boundary(ans)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    reqArea = int(input().strip())

    area_count = int(input().strip())

    area = []

    for _ in range(area_count):
        area_item = int(input().strip())
        area.append(area_item)

    price_count = int(input().strip())

    price = []

    for _ in range(price_count):
        price_item = int(input().strip())
        price.append(price_item)
    print(area)
    print(price)
    result = valuation(reqArea, area, price)
    print(result)
    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
