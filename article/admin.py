from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin	
from jalali_date import datetime2jalali
from article.models import Article, Category

def make_published_article(modeladmin, request, queryset):
    queryset.update(status='publish')
make_published_article.short_description = 'انتشار مقالات انتخابی'

def make_drafted_article(modeladmin, request, queryset):
    queryset.update(status='draft')
make_drafted_article.short_description = 'پیش نویس مقالات انتخابی'

def make_arshived_article(modeladmin, request, queryset):
    queryset.update(status='arshive')
make_arshived_article.short_description = 'آرشیو مقالات انتخابی'

def make_is_important_article(modeladmin, request, queryset):
    queryset.update(is_important=True)
make_is_important_article.short_description = 'افزودن مقالات انتخابی به اسلایدر'

def make_is_not_important_article(modeladmin, request, queryset):
    queryset.update(is_important=False)
make_is_not_important_article.short_description =  'حذف مقالات انتخابی از اسلایدر'


@admin.register(Article)
class ArticleAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'status', 'author', 'view_count', 'jcreated')
    list_filter = ('status', 'created')
    readonly_fields = ('view_count',)
    # list_display_links = ('status',)
    search_fields = ('title', 'body')
    actions = [make_published_article, make_drafted_article, make_is_important_article, make_is_not_important_article]

    # def jCreated(self, obj):
    #     return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')
    # jCreated.short_description = 'تاریخ ایجاد'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'status')
    # fields = ('title', 'slug')

