from django.contrib import admin
from django.db.models import Count
from .models import *


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "book_count")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _book_count=Count("book", distinct=True),
        )
        return queryset

    def book_count(self, obj):
        return obj._book_count

    book_count.admin_order_field = "_book_count"
    book_count.short_description = "Počet knih"


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "release_year", "rate_percent")

    def release_year(self, obj):
        return obj.release_date.year

    def rate_percent(self, obj):
        return format_html("<b>{} %</b>", int(obj.rate * 10))

    rate_percent.short_description = "Hodnocení knihy"
    release_year.short_description = "Rok uvedení"


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "filesize")

    def book_title(self, obj):
        return obj.book.title