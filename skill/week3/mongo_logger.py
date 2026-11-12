
# mongo_logger.py

from pymongo import MongoClient
from datetime import datetime, timezone


class MongoLogger:

    def __init__(self):

        # Connect to local MongoDB server
        self.client = MongoClient(
            "mongodb://localhost:27017/",
            serverSelectionTimeoutMS=5000
        )

        # Verify MongoDB connection
        self.client.admin.command("ping")

        # Select database
        self.db = self.client["llm_monitoring"]

        # Select collection
        self.collection = self.db["call_logs"]

        print("MongoDB connected successfully!")

    def log_call(self, log_data):

        # Add timestamp
        log_data["timestamp"] = datetime.now(timezone.utc)

        # Insert document into MongoDB
        self.collection.insert_one(log_data)

        print("Call details saved in MongoDB!")

    def close(self):

        self.client.close()
