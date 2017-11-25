from models import *

def getAge():
    labels=Age.objects.values_list('labels').order_by('id')
    data=Age.objects.values_list('data').order_by('id')
    labelsList=[]
    dataList=[]
    for la in labels:
        labelsList.append(la[0])
    for da in data:
        dataList.append(da[0])
    dic={
        'labels':labelsList,
        'data':dataList,
    }
    return dic

def getGender():
    labels = Gender.objects.values_list('labels').order_by('id')
    data = Gender.objects.values_list('data').order_by('id')
    labelsList = []
    dataList = []
    for la in labels:
        labelsList.append(la[0])
    for da in data:
        dataList.append(da[0])
    print labelsList
    print dataList
    dic = {
        'labels': labelsList,
        'data': dataList,
    }
    return dic

def getOperate():
    month = Operate.objects.values_list('month').order_by('id')
    click = Operate.objects.values_list('click').order_by('id')
    addCart=Operate.objects.values_list('addCart').order_by('id')
    buy=Operate.objects.values_list('buy').order_by('id')
    collect=Operate.objects.values_list('collect').order_by('id')

    monthList = []
    clickList = []
    addCartList=[]
    buyList=[]
    collectList=[]
    for mon in month:
        monthList.append(mon[0])
    for cl in click:
        clickList.append(cl[0])
    for add in addCart:
        addCartList.append(add[0])
    for bu in buy:
        buyList.append(bu[0])
    for col in collect:
        collectList.append(col[0])

    print monthList
    print clickList
    print addCartList
    print buyList
    print collectList

    dic = {
        'month': monthList,
        'click': clickList,
        'addCart': addCartList,
        'buy': buyList,
        'collect':collectList

    }
    return dic