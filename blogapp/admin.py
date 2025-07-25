from django.contrib import admin
from .models import Autor, Post, Categoria, Comentario

# Register your models here.
class AutorAdmin(admin.ModelAdmin):
    fields= ('user', 'nombre', 'apellido', 'email', 'biografia')
    list_display = ('nombre', 'email')
    search_fields = ('email')
    list_filter = ('nombre')

admin.site.register(Autor)
admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Comentario)