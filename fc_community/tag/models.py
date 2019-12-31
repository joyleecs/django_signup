from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='tag name')
    registered_dttm = models.DateTimeField(auto_now_add=True, 
                                verbose_name='registered_time')
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'fastcampus_tag'
        verbose_name = '패스트캠퍼스 태그'
        verbose_name_plural = '패스트캠퍼스 태그'

        
        