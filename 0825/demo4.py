from wxpy import *

# 通过机器人对象 Bot 的 chats(), friends()，groups(), mps() 方法,
# 可分别获取到当前机器人的 所有聊天对象、好友、群聊，以及公众号列表。


image_path = "/Users/alice/Desktop/U-PLAN/0825/img/img/product1.jpg"
bot = Bot()

friends = ["ALICE"]

for friend in friends:
    friend_search = bot.friends().search(friends)
    if (len(friend_search) == 1):
        friend_search[0].send("测试测试")
        # friend_search[0].send_image(image_path)
    else:
        print("发送失败")
