from faker import Faker
import random
import json

fake = Faker()

# Number of records to generate
num_records = 100

# Generate Online Sales Data
def generate_online_sales_data():
    return {
        "order_id": fake.unique.bothify(text="OS###"),
        "customer_id": fake.unique.bothify(text="C###"),
        "items": [
            {
                "product_id": fake.unique.bothify(text="P###"),
                "quantity": random.randint(1, 5),
                "price": round(random.uniform(50.0, 5000.0), 2)
            } for _ in range(random.randint(1, 5))
        ],
        "order_date": fake.date_between(start_date="-1y", end_date="today").strftime("%Y-%m-%d"),
        "payment_info": {
            "method": random.choice(["Credit Card", "Debit Card", "UPI", "Net Banking", "Cash On Delivery"]),
            "status": random.choice(["Paid", "Pending", "Failed"]),
            "transaction_id": fake.unique.bothify(text="T######")
        },
        "delivery_status": {
            "status": random.choice(["Shipped", "In Transit", "Delivered", "Cancelled"]),
            "tracking_id": fake.unique.bothify(text="TRK#####")
        }
    }

# Generate Offline Sales Data
def generate_offline_sales_data():
    return {
        "invoice_id": fake.unique.bothify(text="INV###"),
        "store_id": fake.unique.bothify(text="S###"),
        "customer_id": fake.unique.bothify(text="C###"),
        "products": [
            {
                "product_id": fake.unique.bothify(text="P###"),
                "quantity": random.randint(1, 5),
                "price": round(random.uniform(50.0, 5000.0), 2)
            } for _ in range(random.randint(1, 5))
        ],
        "purchase_date": fake.date_between(start_date="-1y", end_date="today").strftime("%Y-%m-%d"),
        "salesperson": {
            "id": fake.unique.bothify(text="SP###"),
            "name": fake.name()
        }
    }

# Generate Customer Service Data
def generate_customer_service_data():
    return {
        "ticket_id": fake.unique.bothify(text="T###"),
        "customer_id": fake.unique.bothify(text="C###"),
        "issue_type": random.choice(["Device Malfunction", "Late Delivery", "Payment Issue", "Other"]),
        "status": random.choice(["Open", "In Progress", "Resolved", "Closed"]),
        "resolution_details": {
            "resolution_date": fake.date_between(start_date="-1y", end_date="today").strftime("%Y-%m-%d"),
            "service_center_id": fake.unique.bothify(text="SC###"),
            "comments": fake.sentence()
        }
    }

# Generate Customer Experience Data
def generate_customer_experience_data():
    return {
        "feedback_id": fake.unique.bothify(text="FB###"),
        "customer_id": fake.unique.bothify(text="C###"),
        "feedback_date": fake.date_between(start_date="-1y", end_date="today").strftime("%Y-%m-%d"),
        "ratings": {
            "product_quality": random.randint(1, 5),
            "delivery_service": random.randint(1, 5),
            "customer_support": random.randint(1, 5)
        },
        "comments": fake.sentence()
    }

# Generate Data
online_sales_data = [generate_online_sales_data() for _ in range(num_records)]
offline_sales_data = [generate_offline_sales_data() for _ in range(num_records)]
customer_service_data = [generate_customer_service_data() for _ in range(num_records)]
customer_experience_data = [generate_customer_experience_data() for _ in range(num_records)]

# Save to JSON files
with open("online_sales_data.json", "w") as f:
    json.dump(online_sales_data, f, indent=4)

with open("offline_sales_data.json", "w") as f:
    json.dump(offline_sales_data, f, indent=4)

with open("customer_service_data.json", "w") as f:
    json.dump(customer_service_data, f, indent=4)

with open("customer_experience_data.json", "w") as f:
    json.dump(customer_experience_data, f, indent=4)

print("Data generation complete. JSON files saved.")