from django.contrib import admin

from .models import Poll, Choice


class ChoiceAdmin(admin.ModelAdmin):
    fields = ["choice_text", "poll"]


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1


class PollAdmin(admin.ModelAdmin):
    fields = ['question', 'created_by']

    inlines = [ChoiceInline,]

admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Poll, PollAdmin)
