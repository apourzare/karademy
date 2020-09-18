from account.models import User
from django.db import models
from django.urls import reverse
from jalali_date import datetime2jalali, date2jalali


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان دسته‌بندی')
    slug = models.SlugField(allow_unicode=True, verbose_name='لینک یکتا', unique=True)
    status = models.BooleanField(default=False, verbose_name='وضعیت انتشار')
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)

    class Meta:
        ordering = ('title', 'status')
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'

    def __str__(self):
        return self.title


class ArticleManager(models.Manager):
    def published(self, number=None):
        if number == None:
            return self.filter(status='publish')
        else:
            return self.filter(status='publish')[:number]
    def is_import(self):
        return self.filter(status='publish', is_important=True)
        

class Article(models.Model):
    STATUS_CHOICES = (
        ('publish', 'انتشار'),
        ('draft', 'پیش‌نویس'),
        ('archive', 'آرشیو'),
    )
    ro_titre = models.CharField(max_length=200, verbose_name='رو تیتر', null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name='عنوان مقاله')
    slug = models.SlugField(allow_unicode=True, verbose_name='لینک یکتا', unique=True)
    abstruct = models.TextField(verbose_name='خلاصه', null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, verbose_name='وضعیت انتشار', max_length=10)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='نویسنده')
    body = models.TextField(verbose_name='متن مقاله')
    thumbnail = models.ImageField(upload_to='images/', verbose_name='تصویر شاخص', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='دسته‌بندی')
    is_important = models.BooleanField(default=False, verbose_name='خبر ویژه')
    view_count = models.IntegerField(default=0, verbose_name='تعداد بازدید')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='آخرین ویرایش')

    def j_created(self):
        return datetime2jalali(self.created).strftime('%y/%m/%d')

    j_created.short_description = 'تاریخ ایجاد'
    jcreated = property(j_created)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article:article-detail", kwargs={'slug': self.slug})

    objects = ArticleManager()