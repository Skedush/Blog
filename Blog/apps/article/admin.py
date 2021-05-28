from django.contrib import admin
from.models import Category, Article

# Register your models here.


# class ParentListFilter(admin.SimpleListFilter):
#     title = (u'父分类')
#     parameter_name = 'parent__name'

#     def lookups(self, request, model_admin):
#         qs = model_admin.model.objects.all()
#         ret = []
#         for category in qs:
#             ret.append((category.id, category.name))
#         return ret

#     def queryset(self, request, queryset):
#         if self.value():
#             return queryset.filter(parent__id=self.value())
#         else:
#             return queryset

class ParentInlineAdmin(admin.TabularInline):
    model = Category.parent.through

    fk_name = 'from_category'
    # raw_id_fields = ('to_category',)
    extra = 3


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'describe', 'is_delete', 'sort', '父分类')
    list_display_links = ['name', ]
    search_fields = ['name', 'describe']
    fieldsets = (
        (None, {'fields': ('name', 'describe', 'sort')}),
    )
    list_filter = (('parent',
                   admin.RelatedOnlyFieldListFilter), )
    inlines = [ParentInlineAdmin, ]

    ordering = ('sort', '-id')
    list_per_page = 10

    def 父分类(self, obj):
        return [item.name for item in obj.parent.all()]


class CategoryInlineAdmin(admin.TabularInline):
    model = Article.category.through

    # fk_name = 'from_category'
    # raw_id_fields = ('to_category',)
    extra = 3


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sub_title', 'is_delete', 'sort', '分类')
    list_display_links = ['title', ]
    search_fields = ['title', 'sub_title']
    fieldsets = (
        (None, {'fields': ('title', 'sub_title', 'content', 'sort')}),
    )
    list_filter = (('category',
                   admin.RelatedOnlyFieldListFilter), )
    inlines = [CategoryInlineAdmin, ]

    ordering = ('sort', '-id')
    list_per_page = 10

    def 分类(self, obj):
        return [item.name for item in obj.category.all()]
