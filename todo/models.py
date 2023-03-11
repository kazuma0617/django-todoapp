from django.db import models

# Create your models here.

# 重要度の色を選択する
CHOICE = (('danger','high'),('warning','normal'),('primary','low'))

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices = CHOICE
    )
    # 日付のデータ
    duedate = models.DateField()

    def __str__(self):
        return self.title