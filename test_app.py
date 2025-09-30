import pytest
import flet as ft
from app import main  # importa a função main do seu código

def test_calculo_imc():
    # Criar uma página de teste
    page = ft.Page()
    main(page)

    # Encontrar campos (pela ordem em que foram adicionados)
    nome = page.controls[0].controls[3]   # TextField Nome
    peso = page.controls[0].controls[4]   # TextField Peso
    altura = page.controls[0].controls[5] # TextField Altura
    btn_calcular = page.controls[0].controls[6].controls[0]  # Botão Calcular
    resultado = page.controls[0].controls[7]  # Texto de resultado

    # Preencher valores
    nome.value = "Maria"
    peso.value = "60"
    altura.value = "1.65"

    # Simular clique
    btn_calcular.on_click(None)

    # Validar resultado
    assert "📊 IMC calculado e salva" in resultado.value