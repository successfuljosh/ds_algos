def highFive(items):
    def add_as_top_five(lst, val):
        if len(lst) < 5:
            lst.append(val)
        else:
            if val > lst[-1]:
                lst[-1] = val
        lst = sorted(lst, reverse=True)
        return lst

    students = dict()
    for item in items:
        if item[0] in students:
            students[item[0]] = add_as_top_five(students[item[0]], item[1])
        else:
            students[item[0]] = list()
            students[item[0]].append(item[1])

    for (k, v) in students.items():
        students[k] = sum(v) // 5
    students = dict(sorted(students.items(), key=lambda item: item[0]))
    ans = [[i, ave] for i, ave in students.items()]

    return ans

l = [[5,91],[5,92],[3,93],[3,97],[5,60],[3,77],[5,65],[5,87],[5,100],[3,100],[3,76]]
print(highFive(l))