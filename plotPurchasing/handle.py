#coding:utf-8
import pandas as pd
from config import APP_STATIC_DATA
import os
def getAge():
    path=os.path.join(APP_STATIC_DATA, 'age.csv')
    dataSet=pd.read_csv(path,header=None,sep=',')
    labels=list(dataSet.iloc[:,0].values)
    data = list(dataSet.iloc[:,1].values)
    dic={
        'labels':labels,
        'data':data
    }
    return dic

def getGender():
    path = os.path.join(APP_STATIC_DATA, 'gender.csv')
    dataSet = pd.read_csv(path, header=None, sep=',')
    labels = list(dataSet.iloc[:, 0].values)
    data = list(dataSet.iloc[:, 1].values)
    dic = {
        'labels': labels,
        'data': data
    }
    return dic

def getOperate():
    pd.set_option('precision', 2)
    path = os.path.join(APP_STATIC_DATA, 'operate1.csv')
    dataSet = pd.read_csv(path, header=None, sep=',')
    month = list(dataSet.iloc[:, 1].values)
    click = list(dataSet.iloc[:, 2].values)
    addCart=list(dataSet.iloc[:, 3].values)
    buy=list(dataSet.iloc[:, 4].values)
    collect=list(dataSet.iloc[:, 5].values)
    desc=['点击','加入购物车','购买','收藏']
    dic = {
        'desc':desc,
        'month': month,
        'click': click,
        'addCart':addCart,
        'buy':buy,
        'collect':collect,
    }
    return dic

def getBrandVolume():
    path=os.path.join(APP_STATIC_DATA, 'brand_volume.csv')
    dataSet=pd.read_csv(path,sep=',')
    brand=list(dataSet.iloc[:,0].values)
    volume = list(dataSet.iloc[:,1].values)
    dic={
        'brand':brand,
        'volume':volume
    }
    return dic

def getSellerVolume():
    path=os.path.join(APP_STATIC_DATA, 'seller_volume.csv')
    dataSet=pd.read_csv(path,sep=',')
    seller=list(dataSet.iloc[:,0].values)
    volume = list(dataSet.iloc[:,1].values)
    dic={
        'seller':seller,
        'volume':volume
    }
    return dic

if __name__=='__main__':
    getSellerVolume()