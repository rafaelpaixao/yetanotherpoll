from django.contrib import admin

from .models import Option, Poll, Vote


class OptionAdmin(admin.StackedInline):
    model = Option
    extra = 0


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ["__str__", "created", "modified"]
    inlines = [
        OptionAdmin,
    ]


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ["__str__", "created", "modified"]
