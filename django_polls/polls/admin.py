from django.contrib import admin

from .models import Question

from .models import Choice

# Register your models here.


class ChoiceInline(admin.TabularInline):
    # Si queremos que las opciones esten una abajo de otr
    # hay que heredar de  admin.StackedInline 
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]  # permite agregar choices al crear la cuestion
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # como se ven las questions en el admin
    list_filter = ['pub_date']  # añade  las opciones de filtrar por fecha
    search_fields = ['question_text'] # permite que busque preguntas por texto

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)