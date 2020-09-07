from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin	
from jalali_date import datetime2jalali
from article.models import Article, Category


@admin.register(Article)
class ArticleAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'status', 'author', 'view_count', 'jCreated')
    list_filter = ('status', 'created')
    readonly_fields = ('view_count',)
    # list_display_links = ('status',)
    search_fields = ('title', 'body')

    def jCreated(self, obj):
        return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')
    jCreated.short_description = 'تاریخ ایجاد'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'status')
    # fields = ('title', 'slug')

