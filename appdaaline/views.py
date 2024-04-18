from django.shortcuts import redirect, render
from .models import CoisaParaFazer, Lugar

# Create your views here.

def listagem(request):
  coisas = CoisaParaFazer.objects.all()
  return render(
    request,
    'home.html',
    {
      'coisas': coisas 
    }
  )

def create_atv(request):
  print("Nova atividade registrada")
  if request.method == "POST":
    # criar nova atividade usando os valores do formulário
    CoisaParaFazer.objects.create(
      nome = request.POST["nome"],
      descricao = request.POST["descricao"],
      tempo = request.POST["tempo"],
      energia = request.POST["energia"],
      numero = request.POST["numero"],
      icone = request.POST["icone"]
    )
    return redirect("listagem")
  return render(request, "forms.html", context={"action": "Adicionar"})

def update_atv(request, id):
  atv = CoisaParaFazer.objects.get(id = id)
  print(atv)
  if request.method == "POST":
    # criar nova atividade usando os valores do formulário
    atv.nome = request.POST["nome"]
    atv.descricao = request.POST["descricao"]
    atv.tempo = request.POST["tempo"]
    atv.energia = request.POST["energia"]
    atv.numero = request.POST["numero"]
    atv.icone = request.POST["icone"]
    atv.save()
    
    return redirect("listagem")
  return render(request, "forms.html", context={"action": "Atualizar", "atv": atv})

"""def update_lugar(request, id):
  lugar = Lugar.objects.get(id = id)
  print(lugar)
  if request.method == "POST":
    # criar nova atividade usando os valores do formulário
    lugar.nome = request.POST["nome"]
    lugar.descricao = request.POST["descricao"]
    lugar.tempo = request.POST["tempo"]
    lugar.energia = request.POST["energia"]
    lugar.numero = request.POST["numero"]
    lugar.icone = request.POST["icone"]
    lugar.save()
  
    return redirect("listagem")
  return render(request, "forms.html", context={"action": "Atualizar", "lugar": lugar})"""

def delete_atv(request, id):
  atv = CoisaParaFazer.objects.get(id = id)
  if request.method == "POST":
    if request.POST["confirm"]:
      atv.delete()
    return redirect("listagem")
  return render(request, "are_you_sure.html", context={"atv": atv})

# não consegui fazer o delete
# erro quando clica em remover