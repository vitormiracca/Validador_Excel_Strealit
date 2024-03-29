import streamlit as st

class ValidadorExcelUI:

    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(page_title="Upload Compras - Validação")

    def display_header(self):
        st.title("Validação do Excel - Compras")

    def upload_file(self):
        return st.file_uploader("Carregue seu arquivo excel aqui", type=["xlsx"])
    
    def display_results(self, result, error):
        if error:
            for i in error:
                st.error(f"Erro de validação: {i}")
        else:
            st.success("O schema do arquivo Excel está correto!")

    def display_save_button(self):
        return st.button("Carregar os dados no Database")
    
    def display_wrong_message(self):
        return st.error("Necessário corrigir a planilha!")
    
    def display_success_message(self):
        return st.success("Dados salvos com sucesso no banco de dados!")