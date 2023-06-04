from django.db import models

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey('user.User',on_delete=models.CASCADE,verbose_name='사용자')
    #user app 내의 models.User라는 클래스를 ForeginKey로 사용하겠다

    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='상품')
    quantity = models.IntegerField(verbose_name='수량')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='주문시간')

    class Meta :
     db_table = 'haeseung_order' #데이터베이스 테이블명 지정
     verbose_name = '주문' #django-admin에서 보는 이름지정
     verbose_name_plural = '주문' #django-admin에서 보는 복수형 이름도 지정해주기로 함