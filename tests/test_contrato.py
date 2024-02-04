import pytest
from datetime import datetime
from src.contrato import Compras
from pydantic import ValidationError

def test_compras_com_dados_validos():
    """
    Testa a criação de uma instância da classe Compras com dados válidos.

    Este teste verifica se a classe Compras aceita e armazena corretamente os dados válidos fornecidos.
    O teste confirma se os valores armazenados na instância correspondem aos dados fornecidos.
    """
    dados_validos = {
        "Data": datetime.now(),
        "Fornecedor": "EletricalPartner",
        "Categoria": "equipamentos",
        "Produto": "Impressora Epson",
        "Quantidade": 2,
        "Valor_Unitario":	365.99,
        "Email_Fornecedor": "vendas@eletricalpartner.com.br",
        "Desconto": 0.17,
        "Valor_Final": 607.54,
        }

    compra = Compras(**dados_validos)

    assert compra.Data == dados_validos["Data"]
    assert compra.Fornecedor == dados_validos["Fornecedor"]
    assert compra.Categoria == dados_validos["Categoria"]
    assert compra.Produto == dados_validos["Produto"]
    assert compra.Quantidade == dados_validos["Quantidade"]
    assert compra.Valor_Unitario == dados_validos["Valor_Unitario"]
    assert compra.Email_Fornecedor == dados_validos["Email_Fornecedor"]
    assert compra.Desconto == dados_validos["Desconto"]
    assert compra.Valor_Final == dados_validos["Valor_Final"]

def test_compras_com_dados_invalidos():
    """
    Testa a criação de uma instância da classe compras com dados inválidos.

    Este teste verifica a validação de dados na classe Compras. Dados inválidos incluem um email incorreto, 
    data em formato inválido, valor negativo, nome do produto vazio, quantidade negativa, e uma categoria válida.
    Espera-se que a classe compras gere uma exceção ValidationError quando dados inválidos são fornecidos.
    """

    dados_invalidos = {
        "Data": "nao é uma data aqui",
        "Fornecedor": "",
        "Categoria": "materia_prima", # único campo correto (validação específica a seguir)
        "Produto": "",
        "Quantidade": -1,
        "Valor_Unitario": -10.10,
        "Email_Fornecedor": "vendas",
        "Desconto": 20,
        "Valor_Final": "20.00",
        }

    with pytest.raises(ValidationError):
        Compras(**dados_invalidos)

def test_validacao_categoria():
    """
    Testa a validação da categoria na criação de uma instância da classe compras.

    Este teste especificamente verifica se a classe compras valida a categoria do produto. 
    Ele utiliza dados válidos para todos os campos, exceto pela categoria, que é definida como uma categoria inexistente.
    Espera-se que a classe compras gere uma exceção ValidationError devido à categoria inválida.
    """
    dados = {
        "Data": datetime.now(),
        "Fornecedor": "EletricalPartner",
        "Categoria": "Categoria Inexistente",
        "Produto": "Impressora Epson",
        "Quantidade": 2,
        "Valor_Unitario":	365.99,
        "Email_Fornecedor": "vendas@eletricalpartner.com.br",
        "Desconto": 0.17,
        "Valor_Final": 607.54,
        }

    with pytest.raises(ValidationError):
        Compras(**dados)