# 当前目录下有一个文件名为btc_price.txt的文件，存储着2018年第一季度比特币的价格，
# 共有时间、价格两列，请计算第一季度每个月比特币的平均价格，并按照价格由低到高的顺序，
# 将数据以月份、价格两列存放到另一文件btc_price_season1.txt中，并在屏幕上以字典的形式输出。

with open("btc_price.txt", "r") as file:
    bitCoin = {'1':0,'2':0,'3':0,'4':0}
    for line in file.readlines():
        for i in range(1,5):
            if int(line[5:7]) == i :
                bitCoin[str(i)] += float(line.split(" ")[1])
    print(bitCoin)
    print(sorted(bitCoin.items(),key=lambda x:x[1]))

with open("resultBitcoin.txt","w") as resultFile:
    for i in sorted(bitCoin.items(),key=lambda x: x[1]):
        resultFile.write(i[0] + "月 " + str(i[1]) + "\n")


    # count = 0
    # priceSum = 0
    # bitCoin = {}
    # 审错题目 求成所有平均值并将所有排序
    # for line in file.readlines():
        # count += 1
        # priceSum += float(line.split(" ")[1])
        # bitCoin[line.split(" ")[0]] = float(line.split(" ")[1].replace("\n",""))

#     print("1-4月的比特币的平均价格为" + str(priceSum/count))
#     print(bitCoin)
#     print(sorted(bitCoin.items(),key=lambda x: x[1]))
#
#
# with open("resultBitcoin.txt","w") as resultFile:
#     for i in sorted(bitCoin.items(),key=lambda x: x[1]):
#         resultFile.write(i[0] + " " + str(i[1]) + "\n")