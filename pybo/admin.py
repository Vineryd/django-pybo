from django.contrib import admin
from .models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    list_display = ['id', 'subject', 'create_date']
<<<<<<< HEAD
    ordering = ['-id']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
=======
    ordering = ['id']  # -로 

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
# Register your models here.
>>>>>>> f0cf70c187a02ef13c7821c4c612dbff267fc274
