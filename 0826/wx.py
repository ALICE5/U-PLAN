from wxpy import *


image_path = "./Wechat/product2.jpg"
bot = Bot()

friends = ["ALICE","我叫屁屁"]

for friend in friends:
	my_friend = bot.friends().search(friend)
	print(my_friend)

	if len(my_friend) == 1:
		# my_friend[0].send_image(image_path)
		my_friend[0].send("你是猪吗")
	else:
		print("发送失败，请检查用户名"+friend)


