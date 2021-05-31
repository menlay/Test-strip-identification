from django.shortcuts import render
import os
from django.http import HttpResponse
import hashlib
from Do_Ident import models
import sqlite3
from subprocess import Popen
from Do_Ident.img_classification.test_model_online import predict

import time
# Create your views here.
def hello(request):
    return render(request,'ming.html')

def lv(request):
    return render(request,'lv.html')

def zhr(request):
    return render(request,'zhr.html')

def ipa(request):
    return render(request, 'ipa.html')

def paper(request):
    if request.method == "POST":
        image = request.FILES['image']
        print(image)
        open_id = request.POST.get('openid')
        basedir = os.path.dirname(__file__)  # 获取当前路径的上一级 极为s1
        path = basedir + '/image/'
        if os.path.exists(path + open_id + '.jpg'):
            os.remove(path + open_id + '.jpg')# 如何不为空
            os.remove('..\TestPaper\Do_Ident\image\\result.txt')
        with open(path + open_id + '.jpg', 'wb')as f:  # 转为二进制写入
            f.write(image.read())
            cmd = 'python ..\TestPaper\Do_Ident\img-classification\\test_model_online.py ..\TestPaper\Do_Ident\image\minghh.jpg ..\TestPaper\Do_Ident\image\\result.txt'
            os.popen(cmd)
            while not os.path.exists('..\TestPaper\Do_Ident\image\\result.txt'):
                time.sleep(1)

            if os.path.exists('..\TestPaper\Do_Ident\image\\result.txt'):
                with open('..\TestPaper\Do_Ident\image\\result.txt', 'r+') as fr:
                    result = fr.read()
                    return HttpResponse(result)

            else:
                return HttpResponse('Error')


def paper1(request):
    conn = sqlite3.connect('test1.db')
    c = conn.cursor()

    if request.method == "POST":
        # image = request.body.split(b'\r\n\r\n')[1]
        image = request.FILES['image'].read()
        image_id = hashlib.md5(image).hexdigest()
        response = HttpResponse("检测结果为：")
        try:
            serch = models.TestPaper.objects.get(paper_idx=image_id).result
            # cursor = c.execute('''select result from mnnu_in_testpaper where paper_idx={id};'''.format(id=image_id))
            result = serch
            response.write(result)
            # response['result'] = result
        except Exception as e:
            isrepeat = models.TestPaper.objects.filter(paper_idx=image_id)
            if isrepeat.count()>1:
                models.TestPaper.objects.filter(paper_idx=image_id).delete()
            # response.write('预测中---！')
            # print(image)
        # open_id = request.POST.get('openid')

            basedir = os.path.dirname(__file__)  # 获取当前路径的上一级 极为s1
            path = basedir + '/image/'
            if os.path.exists(path + image_id + '.jpg'):
                os.remove(path + image_id + '.jpg')# 如何不为空
                # os.remove('E:\gittest\ming-TestPaper\ming\TestPaper\Do_Ident\image\\result.txt')
            with open(path + image_id + '.jpg', 'wb')as f:  # 转为二进制写入
                f.write(image)

                # cmd = 'python E:\gittest\img_classification\\test_model_online.py E:\gittest\ming-TestPaper\ming\TestPaper\Do_Ident\image\{img_path}'.format(img_path=path + image_id + '.jpg')
                # Popen(cmd)
            result = predict(path + image_id + '.jpg')
            # models.TestPaper.objects.create(title='Testpaper', paper_idx=image_id, result=result)
            # c.execute('''insert into mnnu_in_testpaper (paper_idx, result) values ({id}, {result});'''.format(id=str(image_id), result=str(result)))
            # response.write("检测结果为{a}".format(a=result))
            response.write(result)

        return response




            # while not os.path.exists('E:\gittest\ming-TestPaper\ming\TestPaper\Do_Ident\image\\result.txt'):
            #     time.sleep(1)
            # if os.path.exists('E:\gittest\ming-TestPaper\ming\TestPaper\Do_Ident\image\\result.txt'):
            #     with open('E:\gittest\ming-TestPaper\ming\TestPaper\Do_Ident\image\\result.txt', 'r+') as fr:
            #         result = fr.read()
            #         return HttpResponse(result)
            #
            # else:
            #     return HttpResponse('Error')


