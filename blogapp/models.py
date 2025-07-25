from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Autor(models.Model):
    id_autor = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    categorias = models.ManyToManyField(Categoria, related_name="posts",blank=True)

    def __str__(self):
        return self.titulo
    
    def publicar_articulo(self):
        self.fecha_publicacion = timezone.now()
        self.save()

class Comentario(models.Model):
    autor_comentario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido_comentario = models.TextField()
    fecha_comentario = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey("Post", related_name="comentarios", on_delete=models.CASCADE)

    comentario_padre = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='respuestas'
    )

    def __str__(self):
        return f" {self.autor_comentario.username} - {self.contenido_comentario[:30]}"