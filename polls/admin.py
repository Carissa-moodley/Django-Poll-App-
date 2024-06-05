from django.contrib import admin
from .models import Question, Choice

# Register the Question class so admin can add questions
admin.site.register(Question)
# Register the Choice class so admin can add answer choices
admin.site.register(Choice)