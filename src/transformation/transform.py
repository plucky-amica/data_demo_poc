def transform_data(data):
    transformed_data = [item for item in data if item["value"] > 10]
    print("Data transformed:", transformed_data)
    return transformed_data

if __name__ == "__main__":
    sample_data = [{"id": 1, "value": 5}, {"id": 2, "value": 15}]
    transform_data(sample_data)
