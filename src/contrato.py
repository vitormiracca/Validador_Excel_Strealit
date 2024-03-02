from pydantic import BaseModel, EmailStr, PositiveInt, PositiveFloat, field_validator
from datetime import date, datetime
from enum import Enum

class Categoria_Enum(str, Enum):
    materia_prima = "materia_prima"
    escritorio = "escritorio"
    equipamentos = "equipamentos" 

class Compras(BaseModel):
    """
    Modelo de Dados para o excel de Compras
    O excel a ser validado, deverá possuir a estrutura definida aqui para que a passe na validação.
    """

    Data: datetime
    Fornecedor: str
    Categoria: Categoria_Enum
    Produto: str
    Quantidade:	PositiveInt
    Valor_Unitario:	PositiveFloat
    Email_Fornecedor: EmailStr
    Desconto: PositiveFloat
    Valor_Final: PositiveFloat

    @field_validator('Desconto')
    def valida_desconto(cls, valor):
        if valor >= 1.0:
            raise ValueError("O campo 'Desconto' deve ser menor que 1.0 (de 0.01 a 0.99)")
        
        return valor