from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import View
from . import models
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from itsdangerous import TimedJSONWebSignatureSerializer as Tser,SignatureExpired
# Create your views here.
from django.core import serializers
class Index(View):
    def get(self, request):
        products = models.Product.objects.all()



        return render(request, 'index.html', locals())

class Single(View):
    def get(self, request, id):
        product = models.Product.objects.get(pk=id)
        return render(request, 'single.html', locals())

class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self,request):
        username = request.POST['username']
        pwd = request.POST['pwd']
        user = get_object_or_404(models.Account,name=username)
        if user.activation!='0':

            account = models.Account.objects.filter(name=username)
            # print(account)
            if account[0].name==username and account[0].pwd == pwd:
                return render(request, 'index.html')
            return redirect(reverse('lamp:login'))

        else:
            return render(request, 'login.html',{'a': '用户尚未激活,请去激活'})

class Accountl(View):
    # models.Account(name=username, pwd=pwd).save()
    def get(self,request):

        return render(request,'account.html',locals())
    def post(self,request):


        name = request.POST['name']
        pwd = request.POST['pwd']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['radio']

        accounts = models.Account.objects.filter(name=name)
        if len(accounts)==0:

            shoppingcart = models.ShoppingCart()
            product = models.Product.objects.get(pk=1)
            shoppingcart.number = 0
            shoppingcart.save()
            # print(product, type(product))
            shoppingcart.product.add(product)


            account = models.Account()




            account.pwd = pwd
            account.name = name
            account.email = email
            account.phone = phone
            account.gender = gender
            account.shoppingcart = shoppingcart
            account.save()

            tser = Tser(settings.SECRET_KEY)
            result = tser.dumps({'userid':account.id}).decode('utf-8')
            print(account.id)
            url = "<a href='http:127.0.0.1:8001/activation/%s/'>点击激活用户</a>"%(result)
            print(url)
            msg = EmailMultiAlternatives('点击激活用户',url,settings.DEFAULT_FROM_EMAIL,[email])
            msg.content_subtype = "html"
            msg.send()

            return render(request,'login.html',{'a':'chengg'})
        else:

            return redirect(reverse('lamp:accountl'))

class Activation(View):
    def get(self, request, info):
        tser = Tser(settings.SECRET_KEY)
        try:
            obj = tser.load(info)
            id = obj['userid']

            user = get_object_or_404(models.Account, pk=id)
            user.activation = 1
            user.save()
            return render(request, 'login.html', {'a':'chengg'})
        except SignatureExpired as e:
            return HttpResponse('过期了')



class Product(View):
    def get(self,request):
        products = models.Product.objects.all()
        classifications = models.Classification.objects.filter(parentClass=None)
        return render(request,'product.html',locals())



class Ajaxurl(View):
    def get(self,request,id):
        # # a = request.GET['id']
        # # print(a)
        # print('进了')
        # print(dir(request))
        return HttpResponse('1131321313213')


class Checkout(View):
    def get(self,request):
        return render(request,'checkout.html')
        # return HttpResponse('chenggong')