from django.db import models
from accounts.models import CustomUser

from django.contrib.auth import get_user_model

CustomUser = get_user_model()

# カテゴリ分類(Productクラスより上で定義する必要がある。)
class Category(models.Model):
    # categoryはプルダウン式のため、選択肢を記載
    category_choices = [
        ('1', '和食'),
        ('2', '中華'),
        ('3', 'イタリアン'),
        ('4', 'フレンチ'),
        ('5','寿司'),
        ('6','焼肉'),
        ('7','韓国料理'),
    ]
    category = models.CharField(verbose_name='ジャンル', choices=category_choices, max_length=50)
    
    def __str__(self):
        return dict(self.category_choices)[self.category]

class StoreInfo(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー',on_delete=models.PROTECT)
    store_name = models.CharField(verbose_name='店舗名',max_length=40)
    #カテゴリーはForeignKey
    category = models.ForeignKey(Category,verbose_name='ジャンル', on_delete=models.PROTECT)
    store_detail = models.TextField(verbose_name='店舗詳細',blank=True, null=True)
    photo1 = models.ImageField(verbose_name='写真1',blank=True,default='noImage.png')
    photo2 = models.ImageField(verbose_name='写真2',blank=True,default='noImage.png')
    photo3 = models.ImageField(verbose_name='写真3',blank=True,default='noImage.png')
    create_at = models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時',auto_now=True)

    class Meta:
        verbose_name_plural = 'StoreInfo'

    def __str__(self):
        return self.store_name
    

