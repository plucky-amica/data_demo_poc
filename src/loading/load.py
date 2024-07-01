import psycopg2

def load_data(data):
    conn = psycopg2.connect(
        dbname="yourdbname", user="youruser", password="yourpassword", host="yourhost"
    )
    cur = conn.cursor()
    for item in data:
        cur.execute("INSERT INTO yourtable (id, value) VALUES (%s, %s)", (item["id"], item["value"]))
    conn.commit()
    cur.close()
    conn.close()
    print("Data loaded into database")

if __name__ == "__main__":
    sample_data = [{"id": 2, "value": 15}]
    load_data(sample_data)
