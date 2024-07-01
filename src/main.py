from extraction.extract import extract_data
from transformation.transform import transform_data
from loading.load import load_data
from utils.logger import setup_logger

def main():
    logger = setup_logger()
    logger.info("Starting ETL process...")

    data = extract_data()
    transformed_data = transform_data(data)
    load_data(transformed_data)

    logger.info("ETL process completed.")

if __name__ == "__main__":
    main()
