# 输出 9x9 乘法表

numbers = ["零","一","二","三","四","五","六","七","八","九"]

def result(a):
    result_str = ""
    # print(len(a))
    for i in range(len(a)):
        # print(numbers[int(a[i])])
        result_str += numbers[int(a[i])]
    return result_str

for i in range(9,0,-1):
    for j in range(1, i+1):
        print(numbers[j] + "*" + numbers[i] + "=" + result(str(i*j)),end=" ")
    print()

# print(result('12'))
