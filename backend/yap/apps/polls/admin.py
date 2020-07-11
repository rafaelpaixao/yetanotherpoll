from django.contrib import admin

from .models import Answer, Option, Poll


class OptionAdmin(admin.StackedInline):
    model = Option
    extra = 0


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ["__str__", "created", "modified"]
    inlines = [
        OptionAdmin,
    ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["__str__", "created", "modified"]
