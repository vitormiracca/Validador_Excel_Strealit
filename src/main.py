from front import ValidadorExcelUI
from back import processa_excel

def main():
    ui = ValidadorExcelUI()
    ui.display_header()

    upload_file = ui.upload_file()
    if upload_file:
        result, errors = processa_excel(upload_file)
        ui.display_results(result, errors)


if __name__ == "__main__":
    main()