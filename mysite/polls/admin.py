from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3

class PollAdmin(admin.ModelAdmin):
  list_display = ('question', 'pub_date', 'was_published_recently')
  list_filter = ['pub_date']
  fieldsets = [
    (None,      {'fields' : ['question']}),
    ('Date Information',      {'fields' : ['pub_date'], 'classes' : ['collapse']})]
  inlines = [ChoiceInline]
  search_fields = ['question']

admin.site.register(Poll, PollAdmin)

# Register your models here.
