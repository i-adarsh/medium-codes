from google.cloud import firestore
import random
import string

def generate_dummy_data(record_id):
    # Generate dummy data for a record
    return {
        "id": record_id,
        "name": ''.join(random.choices(string.ascii_letters, k=10)),
        "age": random.randint(18, 65),
        "email": ''.join(random.choices(string.ascii_lowercase, k=5)) + "@example.com",
        "address": ''.join(random.choices(string.ascii_letters + string.digits, k=15)),
        "phone": ''.join(random.choices(string.digits, k=10)),
    }

def create_collection_and_insert_dummy_records(collection_name, num_records):
    # Initialize Firestore client
    db = firestore.Client()

    # Reference to the collection
    collection_ref = db.collection(collection_name)

    # Insert dummy records
    for i in range(1, num_records + 1):
        record_id = f"record_{i}"
        data = generate_dummy_data(record_id)
        collection_ref.document(record_id).set(data)
        print(f"Inserted record {record_id}")

if __name__ == "__main__":
    collection_name = "dummy_collection"  # Replace with your desired collection name
    num_records = 60  # Number of dummy records to insert

    create_collection_and_insert_dummy_records(collection_name, num_records)
