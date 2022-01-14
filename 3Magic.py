even_count = 0
even_list=[]
three_count = 0
three_list=[]
others = 0
others_list = []
five_count=0
seven_count = 0



start = 1
end = 500
for i in range(start,end+1):
    if i%2==0:
        even_count +=1
        even_list.append(i)
    elif i%3 == 0:
        three_count +=1
        three_list.append(i)
    elif i % 5 == 0:
        five_count += 1
        # three_list.append(i)
    elif i % 7 == 0:
        seven_count += 1
        three_list.append(i)
    else:
        others +=1
        others_list.append(i)

print('even count', even_count)
print('even percent', 100*even_count/end)
print('three count', three_count)
print('three percent', 100*three_count/end)
print('five count', five_count)
print('five percent', 100*five_count/end)
print('seven count', seven_count)
print('seven percent', 100*seven_count/end)
# print('three list', three_list)
print('others count', others)
print('other percent', 100*others/end)
print('others list', others_list)