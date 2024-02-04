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