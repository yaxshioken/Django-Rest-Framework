from django.contrib import admin

from poll.models import Choice, Poll, Vote


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "author", "pub_date")
    list_display_links = ("id", "question")
    list_filter = ("author", "pub_date")
    date_hierarchy = "pub_date"


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "poll", "question")
    list_display_links = ("id", "poll")
    list_filter = ("poll", "question")


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("id", "poll", "choice", "voted_by")
