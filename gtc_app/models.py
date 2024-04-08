from django.db import models

class usuario(models.Model):  # Define uma classe chamada Usuario que herda da classe models.Model
    nome = models.CharField(max_length=100)  # Define um campo chamado nome como um CharField com no máximo 100 caracteres
    data_nascimento = models.DateField()  # Define um campo chamado data_nascimento como um DateField para armazenar datas
    email = models.EmailField(unique=True)  # Define um campo chamado email como um EmailField com a restrição unique=True para garantir que seja único
    pais = models.ForeignKey('Pais', on_delete=models.CASCADE)  # Define um campo chamado pais como uma ForeignKey que estabelece uma relação com o modelo Pais, com a opção on_delete=models.CASCADE indicando que se o país associado a um usuário for excluído, o usuário também será excluído

    def __str__(self):  # Define um método especial __str__() para representar a instância do modelo como uma string
        return self.nome  # Retorna o nome do usuário como representação da instância do modelo

class pais(models.Model):  # Define uma classe chamada Pais que herda da classe models.Model
    nome = models.CharField(max_length=100)  # Define um campo chamado nome como um CharField com no máximo 100 caracteres

    def __str__(self):  # Define um método especial __str__() para representar a instância do modelo como uma string
        return self.nome  # Retorna o nome do país como representação da instância do modelo
