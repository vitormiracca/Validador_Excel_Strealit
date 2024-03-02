import logging
from front import ValidadorExcelUI
from back import excel_to_sql, processa_excel

def main():
    ui = ValidadorExcelUI()
    ui.display_header()

    upload_file = ui.upload_file()
    if upload_file:
        df, result, errors = processa_excel(upload_file)
        ui.display_results(result, errors)

        if errors:
            ui.display_wrong_message()
            logging.error("Planilha apresentava erro no schema...")

        elif ui.display_save_button():
            excel_to_sql(df)
            ui.display_success_message()
            logging.info("Excel carregado com sucesso no banco SQL")


if __name__ == "__main__":
    main()