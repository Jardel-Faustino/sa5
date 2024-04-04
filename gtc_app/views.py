from django.http import JsonResponse
from django.shortcuts import render

def processar_formulario(request):
    if request.method == 'POST':
        # Processar os dados do formulário
        # Aqui você pode salvar os dados no banco de dados ou fazer qualquer outra coisa que precisar
        # Por enquanto, vamos apenas retornar uma resposta JSON indicando que o cadastro foi bem-sucedido
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Método não permitido'}, status=405)


# Criar as Visualizações das Rotas do nosso Sistema de Cadastro GTC.

def index (request):
    return render(request, "gtc_app/global/index.html")

def menu (request):
    return render(request, "gtc_app/rotas/menu.html")

def principal (request):
    return render(request, "gtc_app/rotas/principal.html")

def cadastrar (request):
    return render(request, "gtc_app/rotas/cadastrar.html")

def atualizar (request):
    return render(request, "gtc_app/rotas/atualizar.html")

def deletar (request):
    return render(request, "gtc_app/rotas/deletar.html")

def pesquisar (request):
    return render(request, "gtc_app/rotas/pesquisar.html")