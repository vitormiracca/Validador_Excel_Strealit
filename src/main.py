import logging
from front import ValidadorExcelUI
from back import excel_to_sql, processa_excel
import sentry_sdk

logging.basicConfig(
    filename='logs_streamlit_app.txt',
    filemode='a',
    encoding='utf-8',
    format='%(levelname)s:%(asctime)s:%(message)s'
)

sentry_sdk.init(
    dsn="https://54353fa5553232b68bcf5d2ec46b2f29@o4506847618924544.ingest.sentry.io/4506847626199040",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)


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
            sentry_sdk.capture_message("O Database não foi atualizado pois a planilha estava errada...")

        elif ui.display_save_button():
            excel_to_sql(df)
            ui.display_success_message()
            logging.info("Excel carregado com sucesso no banco SQL")
            sentry_sdk.capture_message("O Database foi atualizado com sucesso...")


if __name__ == "__main__":
    main()