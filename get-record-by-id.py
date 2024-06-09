from google.cloud import firestore

def fetch_document_by_id(collection_name, document_id):
    # Initialize Firestore client
    db = firestore.Client()

    # Reference to the specific document
    doc_ref = db.collection(collection_name).document(document_id)

    # Fetch the document
    doc = doc_ref.get()

    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
        return doc.to_dict()
    else:
        print("No such document!")
        return None

if __name__ == "__main__":
    collection_name = "dummy_collection"  # replace with your collection name
    document_id = "record_3"  # replace with your document ID
    
    fetch_document_by_id(collection_name, document_id)
