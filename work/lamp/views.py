from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import View
from . import models
# Create your views here.

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
        account = models.Account.objects.filter(name=username)
        print(account)
        if account[0].name==username and account[0].pwd == pwd:
            return render(request, 'index.html')
        return redirect(reverse('lamp:login'))

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
            print(product, type(product))
            shoppingcart.product.add(product)


            account = models.Account()
            account.pwd = pwd
            account.name = name
            account.email = email
            account.phone = phone
            account.gender = gender
            account.shoppingcart = shoppingcart
            account.save()



            return render(request,'login.html',{'a':'chengg'})
        else:

            return redirect(reverse('lamp:accountl'))
