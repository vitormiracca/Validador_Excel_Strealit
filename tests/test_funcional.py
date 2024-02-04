from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest
import subprocess

@pytest.fixture
def driver():
    # Inicia o Streamlit em background
    process = subprocess.Popen(["streamlit", "run", "src/main.py"])
    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options)
    driver.set_page_load_timeout(5)
    yield driver

    # Fechar o WebDriver e o Streamlit após o teste
    driver.quit()
    process.kill()

def test_app(driver):
    # Verificar se a página abre
    driver.get("http://localhost:8501")
    sleep(5)
    page_title = driver.title
    assert page_title == "Upload Compras - Validação"
