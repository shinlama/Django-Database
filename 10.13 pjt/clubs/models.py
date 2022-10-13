from django.db import models


# Create your models here.

# 동아리 매칭 프로그램 만들기
# 먼저 이에 필요한 동아리를 만든다

class Club(models.Model):
    title=models.CharField(max_length=30)
    content=models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title    




    

