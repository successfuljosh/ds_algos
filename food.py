N = int(input())
food = {}
for i in range(0,N):
    plate = input().split(' ')
    plate[1] = int(plate[1])
    if plate[0] in food:
        if plate[1] > food[plate[0]]:
            food[plate[0]] = plate[1]
    else:
        food[plate[0]] = plate[1]
print(sum(food.values()))