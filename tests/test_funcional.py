from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest
import subprocess

@pytest.fixture
def driver():
    # Streamlit em background
    process = subprocess.Popen(["streamlit", "run", "src/main.py"])
    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options)
    driver.set_page_load_timeout(5)
    yield driver

    # Fechar o WebDriver e o Streamlit após o teste
    driver.quit()
    process.kill()

def test_open_title(driver):
    # Verificar se a página abre
    driver.get("http://localhost:8501")
    # Verifica se o titulo de página é
    sleep(2)
    # Capturar o título da página
    page_title = driver.title

    # Verificar se o título da página é o esperado
    expected_title = "Upload Compras - Validação"  # Substitua com o título real esperado
    assert page_title == expected_title