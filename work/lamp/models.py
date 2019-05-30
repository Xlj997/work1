from django.db import models

# Create your models here.

# 分类
class Classification(models.Model):

    # 分类名称
    name = models.CharField(max_length=30, verbose_name='分类名称')

    # 产品外键
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)

    parentClass = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

# 产品
class Product(models.Model):
    # 产品名称
    name = models.CharField(max_length=30, verbose_name='产品名称')

    # 产品价格
    price = models.CharField(max_length=30, verbose_name='产品价格')

    # 产品图片
    img = models.FileField( verbose_name='产品图片')

    # 产品简介
    introduce = models.TextField( verbose_name='产品简介')

    # 产品品牌
    brand = models.CharField(max_length=30, verbose_name='产品品牌')

    # 产品尺寸
    size = models.CharField(max_length=30, verbose_name='产品尺寸')

    # 产品颜色
    color = models.CharField(max_length=30, verbose_name='产品颜色')

    # 产品材料
    material = models.CharField(max_length=30, verbose_name='产品材料')

    # 库存
    inventory = models.IntegerField(verbose_name='库存')

    # 已卖出数量
    number = models.IntegerField(default=0, verbose_name='已卖出数量')

    classfi = models.ForeignKey(Classification,on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = verbose_name
# 类型
class Type(models.Model):
    # 类型名字
    name = models.CharField(max_length=30, verbose_name='类型名字')

    # 产品外键
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '类型'
        verbose_name_plural = verbose_name


# 购物车
class ShoppingCart(models.Model):
    # 产品外键
    product = models.ManyToManyField(Product)

    # 产品数量
    number = models.IntegerField(verbose_name='产品数量')

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name



# 账户
class Account(models.Model):

    # 性名
    name = models.CharField(max_length=30, verbose_name='性名')

    # 账户邮箱
    email = models.EmailField(max_length=30, verbose_name='账户邮箱')

    # 电话
    phone = models.CharField(max_length=30, verbose_name='电话')

    # 性别
    gender = models.CharField(max_length=30, verbose_name='性别')

    # 密码
    pwd = models.CharField(max_length=30, verbose_name='密码')

    # 注册时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')

    # 购物车外键
    shoppingcart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)

    # 激活 0为未激活 1为激活
    activation = models.CharField(max_length=30,default=0)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = '账户'
        verbose_name_plural = verbose_name


