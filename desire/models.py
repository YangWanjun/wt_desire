from django.db import models


# Create your models here.
class Desire(models.Model):
    full_name = models.CharField(max_length=30, verbose_name='名前')
    email = models.EmailField(verbose_name="会社メールアドレス")
    avatar = models.ImageField(upload_to='avatar/', verbose_name="写真")
    desire = models.ImageField(blank=True, null=True, upload_to='desire/', verbose_name="願望")

    class Meta:
        db_table = 'mst_desire'
        verbose_name = "願望"
        verbose_name_plural = "願望一覧"

    def __str__(self):
        return self.full_name
