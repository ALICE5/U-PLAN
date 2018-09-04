from django.shortcuts import render
from roomshow.models import RoomInfo
import json
# 分页的插件
from django.core.paginator import Paginator
import time

# Create your views here.

def indexPage(request):
    room_info = RoomInfo.objects

    price_greater = 0
    price_less = 0
    for room in room_info:
        if (room.price > 500):
            price_greater += 1
        else:
            price_less += 1

    sum = price_less + price_greater

    price_less_percentage = price_less / sum * 100
    price_greater_percentage = price_greater / sum * 100

    result = {"price_greater": price_greater, "price_less": price_less,
              "price_less_percentage": price_less_percentage,
              "price_greater_percentage": price_greater_percentage}

    # return render(request, 'index.html',  {
    #     'result': json.dumps(result)
    # } )

    limit = 10
    pagenator = Paginator(room_info, limit)
    index = 1

    page = request.GET.get("page",index)

    print(request)
    print(request.GET)
    loaded = pagenator.page(page)

    context = {
        "RoomInfo": loaded
    }

    return render(request,'index.html',context)

