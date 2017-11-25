from flask import Flask,render_template
from handle import getAge,getGender,getOperate,getBrandVolume,getSellerVolume
app = Flask(__name__)


@app.route('/')
def hello_world():
    age=getAge()
    gender=getGender()
    length=range(len(gender['labels']))
    operate=getOperate()
    brand=getBrandVolume()
    seller=getSellerVolume()
    length2=range(len(seller['seller']))
    return render_template('plot.html',**locals())


if __name__ == '__main__':
    app.run(debug=True)
