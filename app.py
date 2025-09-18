import requests
from lxml import etree
from flask import Flask, render_template, request

app = Flask(__name__)

def search(phone):
    url = f'https://whocall.cc/search/{phone}'
    resp = requests.get(url)

    resp.encoding = 'utf-8'
    e = etree.HTML(resp.text)
    type = e.xpath("string(//div[@id='comment']/div[@class='container'][2]/div[@class='row'][1]/div[@class='col-md-6 col-lg-4 col-10']/div[@class='row']/div[@class='card col-12']/dic[@class='card-body']/div[@class='card-text']/table[@class='table']/tbody/tr[1]/td[@class='p-1'])")
    company = e.xpath("string(//div[@id='comment']/div[@class='container'][2]/div[@class='row'][1]/div[@class='col-md-6 col-lg-4 col-10']/div[@class='row']/div[@class='card col-12']/dic[@class='card-body']/div[@class='card-text']/table[@class='table']/tbody/tr[2]/td[@class='p-1'])")
    cnt = e.xpath("string(//div[@id='comment']/div[@class='container'][2]/div[@class='row'][1]/div[@class='col-md-6 col-lg-4 col-10']/div[@class='row']/div[@class='card col-12']/dic[@class='card-body']/div[@class='card-text']/table[@class='table']/tbody/tr[3]/td[@class='p-1'])")
    reg = e.xpath("string(//div[@id='comment']/div[@class='container'][2]/div[@class='row'][1]/div[@class='col-md-6 col-lg-4 col-10']/div[@class='row']/div[@class='card col-12']/dic[@class='card-body']/div[@class='card-text']/table[@class='table']/tbody/tr[4]/td[@class='p-1'])")
    data = [type, company, cnt, reg]
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/phone_searching')
def phone_searching():
    phone = request.args.get('phone')
    data = search(phone=phone)

    return render_template('search.html', data=data, phone=phone)

app.run()