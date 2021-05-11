from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
#City - город
#Street - улица
#Shop - город
class City(models.Model):
    '''модель City содержит поля
        :name - наимменование;
        :slug'''
    name = models.CharField(max_length = 100, db_index = True)
    slug = models.SlugField(max_length = 100, unique =True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Город'
        #verbose_name_plural = 'citys'

    def __str__(self):
        return self.name

class Street(models.Model):
    '''модель Street'''
    city = models.ForeignKey(City,
                             related_name='streets',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index = True)
    slug = models.SlugField(max_length=100, db_index = True)
    class Meta:
        ordering =('name',)
        verbose_name = 'Улица'
        verbose_name_plural = 'streets'
        index_together = (('id', 'slug'),)
    def __str__(self):
        return self.name

class Shop(models.Model):
    '''модель Shop'''
    #city = models.ForeignKey(City)
    street = models.ForeignKey(Street,
                              related_name='shops',
                              on_delete=models.CASCADE)

    name = models.CharField(max_length=100, db_index=True)
    home = models.CharField(max_length=5, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    open_shop = models.BooleanField(default=True)
    work_from = models.TimeField()
    work_to = models.TimeField()

    class Meta:
        ordering = ('name',)
        index_together = (('id','slug'),)

    def __str__(self):
        return self.name
    
        
