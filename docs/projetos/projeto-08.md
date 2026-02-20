# Projeto 08: Por Dentro do Código ⚪

## 🎯 Objetivo
Analisar a lógica interna e garantir 100% de cobertura de decisão.

## 🛠️ O que fazer
Código a ser testado:
```python
def validar_cupom(codigo, valor_minimo):
    if codigo == "MOD11":
        if valor_minimo > 50:
            return "Desconto Aplicado"
        return "Valor insuficiente"
    return "Cupom inválido"
```
1.  Desenhe o grafo de fluxo.
2.  Quantos casos de teste são necessários para 100% de cobertura de **Decisão**?
3.  Liste as entradas (codigo, valor_minimo) para cada caso.

## 📤 Entrega
Desenho do fluxo e lista de casos de teste estruturais.
