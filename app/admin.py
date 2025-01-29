from django.contrib import admin
from .models import *

admin.site.register(Livro)
admin.site.register(StatusLeitura)
admin.site.register(UsuarioLivro)
admin.site.register(ListaLivros)
admin.site.register(ItemListaLivro)
admin.site.register(MetaLeitura)
admin.site.register(HistoricoLeitura)
admin.site.register(Recomendacao)
