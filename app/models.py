from django.db import models
from django.contrib.auth.models import User

# Cadastro de Livros
class Livro(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título")
    autor = models.CharField(max_length=255, verbose_name="Autor")
    genero = models.CharField(max_length=100, verbose_name="Gênero")
    data_publicacao = models.DateField(verbose_name="Data de Publicação")
    descricao = models.TextField(verbose_name="Descrição")
    capa = models.ImageField(upload_to='capas_livros/', blank=True, null=True, verbose_name="Capa")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

# Gerenciamento de Leituras
class StatusLeitura(models.TextChoices):
    NAO_INICIADO = 'nao_iniciado', 'Quero Ler'
    EM_ANDAMENTO = 'em_andamento', 'Em Andamento'
    PAUSADO = 'pausado', 'Pausado'
    CONCLUIDO = 'concluido', 'Concluído'

class UsuarioLivro(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, verbose_name="Livro")
    status = models.CharField(
        max_length=20,
        choices=StatusLeitura.choices,
        default=StatusLeitura.NAO_INICIADO,
        verbose_name="Status"
    )
    data_inicio = models.DateField(blank=True, null=True, verbose_name="Data de Início")
    data_fim = models.DateField(blank=True, null=True, verbose_name="Data de Conclusão")
    notas = models.TextField(blank=True, null=True, verbose_name="Notas")
    resenha = models.TextField(blank=True, null=True, verbose_name="Resenha")

    def __str__(self):
        return f"{self.usuario.username} - {self.livro.titulo} ({self.status})"

    class Meta:
        verbose_name = "Usuário Livro"
        verbose_name_plural = "Usuários Livros"

# Listas de Livros
class ListaLivros(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    nome = models.CharField(max_length=100, verbose_name="Nome da Lista")
    livros = models.ManyToManyField(Livro, through='ItemListaLivro')

    def __str__(self):
        return f"{self.nome} ({self.usuario.username})"

    class Meta:
        verbose_name = "Lista de Livros"
        verbose_name_plural = "Listas de Livros"

class ItemListaLivro(models.Model):
    lista = models.ForeignKey(ListaLivros, on_delete=models.CASCADE, verbose_name="Lista")
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, verbose_name="Livro")
    status = models.CharField(
        max_length=20,
        choices=StatusLeitura.choices,
        default=StatusLeitura.NAO_INICIADO,
        verbose_name="Status"
    )

    def __str__(self):
        return f"{self.livro.titulo} em {self.lista.nome} ({self.status})"

    class Meta:
        verbose_name = "Item da Lista de Livros"
        verbose_name_plural = "Itens das Listas de Livros"

# Metas de Leitura
class MetaLeitura(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    meta_livros = models.PositiveIntegerField(blank=True, null=True, verbose_name="Meta de Livros")
    meta_paginas = models.PositiveIntegerField(blank=True, null=True, verbose_name="Meta de Páginas")
    data_inicio = models.DateField(verbose_name="Período Inicial")
    data_fim = models.DateField(verbose_name="Período Final")

    def __str__(self):
        return f"{self.usuario.username} - Meta de Leitura"

    class Meta:
        verbose_name = "Meta de Leitura"
        verbose_name_plural = "Metas de Leitura"

# Histórico de Leituras
class HistoricoLeitura(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, verbose_name="Livro")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_fim = models.DateField(verbose_name="Data de Conclusão")
    resenha = models.TextField(blank=True, null=True, verbose_name="Resenha")

    def __str__(self):
        return f"Histórico: {self.usuario.username} - {self.livro.titulo}"

    class Meta:
        verbose_name = "Histórico de Leitura"
        verbose_name_plural = "Históricos de Leituras"

# Recomendações de Livros
class Recomendacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    livros_recomendados = models.ManyToManyField(Livro, verbose_name="Livros Recomendados")
    data_geracao = models.DateTimeField(auto_now_add=True, verbose_name="Data da Geração")

    def __str__(self):
        return f"Recomendações para {self.usuario.username}"

    class Meta:
        verbose_name = "Recomendação"
        verbose_name_plural = "Recomendações"
