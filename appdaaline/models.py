from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class CoisaParaFazer(models.Model):
  nome = models.CharField(max_length = 50)
  icone = models.URLField(max_length = 2000)
  numero = models.IntegerField()
  descricao = models.TextField()
  tempo = models.FloatField()
  energia = models.IntegerField()
  
  def __str__(self):
    return self.nome
  class Meta:
    verbose_name = "Coisa para fazer"
    verbose_name_plural = "Coisas para fazer"
    
class Lugar(models.Model):
  nome = models.CharField(max_length=100)
  link = models.URLField(max_length=2000)
  atividade = models.ForeignKey(CoisaParaFazer, on_delete = models.CASCADE)
  #endereco (fisico)
  endereco = models.CharField(max_length = 300)
  custo = models.FloatField()
    
  def __str__(self):
    return self.nome

  class Meta:
    verbose_name = "Lugar"
    verbose_name_plural = "Lugares"

