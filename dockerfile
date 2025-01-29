# Usa a imagem oficial do Python como base
FROM python:3.9

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o código-fonte da aplicação para dentro do container
COPY . /app/

# Expõe a porta que o Django irá rodar
EXPOSE 8000

# Comando para iniciar o servidor do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
