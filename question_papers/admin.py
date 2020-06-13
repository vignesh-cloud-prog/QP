from django.contrib import admin
from .models import Question_papers,Provider,Issues

# Register your models here.
admin.site.register(Question_papers)
admin.site.register(Provider)
admin.site.register(Issues)
