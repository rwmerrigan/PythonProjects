from datetime import datetime

#region Globomantics - Chat Transcript Logger (simple open example)
# Simulated chatbot conversation with a client
chat_transcript = [
    "Client: Hello, I need to check the status of my shipment.",
    "Bot: Sure, can I have your tracking number?",
    "Client: It's GLOBO123456.",
    "Bot: Thank you. Your package is currently in transit and should arrive by Thursday.",
    "Client: Great, thanks!",
    "Bot: You're welcome. Have a nice day!"
]

# Define the file path
file_path = "transcripts/2025-07-24_chat_log.txt"

file = open(file_path, 'w') # open in write mode, if it already exists this overwrites it
for line in chat_transcript:
    file.write(line + "\n")
file.close() # important to close the file after

print(f"Chat transcript saved to {file_path}")

file = open(file_path, 'r') # open in read mode
contents = file.read()
file.close()

print("\nTranscript Preview:\n")
print(contents)
#endregion

#region Globomantics - Daily Metrics Logger (with example)
# Sample daily metrics collected from a regional logistics hub
daily_metrics = {
    "date":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "region": "West Coast Hub",
    "shipments_processed": 428,
    "delivery_failures": 7, 
    "avg_transit_time_hrs": 26.4
}

# Define the log file path
log_file_path = "logs/shipment_metrics.log"

import os

if not os.path.exists("logs"): # create the folder if it doesn't exist
    os.makedirs("logs")

log_entry = (
    f"[{daily_metrics['date']}] "
    f"Region: {daily_metrics['region']} | "
    f"Shipments: {daily_metrics['shipments_processed']} | "
    f"Failures: {daily_metrics['delivery_failures']} | "
    f"Avg Transit Time: {daily_metrics['avg_transit_time_hrs']} hrs\n"
)

# with handles opening and closing of the file (in this case named log_file)
with open(log_file_path, 'a') as log_file:
    log_file.write(log_entry)

print("Daily shipment metrics logged successfully.")
#endregion

#region Globomantics - Access Log Processor (Line-by-line)
# File path for the simulated access log
log_shipment_access_file_path = "logs/shipment_access.log"

# Ensure the logs directory exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# --- Create of overwrite sample access log data ---
with open(log_shipment_access_file_path, 'w') as file:
    for i in range(1, 101): # Simulate 100 log entries
        status = "SUCCESS" if i % 10 != 0 else "FAILURE"
        file.write(f"EventID={1000+i} | Status={status} | Hub=West | Timestamp=2025-07-24T10:{i%60:02d}: 00Z\n")

print(f"Simulated access log written to {log_shipment_access_file_path}")

print("\n=== Failed Shipments Detected ===")
failed_count = 0

log_file = open(log_shipment_access_file_path, 'r')

for line in log_file:
    if "FAILURE" in line:
        print(line.strip())
        failed_count += 1

log_file.close()
print(f"\nTotal failed shipment events: {failed_count}")

print("\n=== First 5 log entries ===")
log_file = open(log_shipment_access_file_path, 'r')

for _ in range(5):
    print(log_file.readline().strip())

log_file.close()

with open(log_shipment_access_file_path, 'r') as file:
    all_lines = file.readlines()
    print(f"\nTotal lines (using readlines): {len(all_lines)}")

#endregion

#region Globomantics - Multilingual Customer Review Handler
# Simulated customer review from multiple regions (including special characters)
customer_reviews = [
    "Great service and fast delivery!", # English (UTF-8)
    "Gran servicio y entrega rápida!", # Spanish (UTF-8)
    "Excellent service et livraison rapide!", # French (UTF-8)
    "Toller Service und schnelle Lieferung!", # German (UTF-8)
    "Ótimo serviço e entrega rápida!", # Portugese (UTF-8)
    "Отличный сервис и быстрая доставка!", # Russian (UTF-8)
    "素晴らしいサービスと迅速な配送!" # Japanese (UTF-8)
]

# folder to store the reviews
folder = "review"
if not os.path.exists(folder):
    os.makedirs(folder)

# File path for saving the reviews
# utf8 encoding stores most all characters
utf8_file = f"{folder}/customer_reviews_utf8.txt"
# iso encoding is more limited, expecting an error in this case
iso_file = f"{folder}/customer_reviews_iso8859_1.txt"

with open(utf8_file, 'w', encoding='utf-8') as file:
    for review in customer_reviews:
        file.write(review + '\n')

print(f"Saved reviews using UTF-8 encoding: {utf8_file}")

print("\ntrying to read UTF-8 file using incorrect encoding (ISO-8859-1): ")
try:
    with open(utf8_file, 'r', encoding='iso-8859-1') as file:
        contents = file.read()
        print(contents)
except UnicodeDecodeError as e:
    print(f"Decode Error: {e}")

# check that every characters unicode code point is less then 256 (iso standard?)
filtered_iso_compatible_reviews = [r for r in customer_reviews if all(ord(c) < 256 for c in r)]

with open(iso_file, 'w', encoding='iso-8859-1') as file:
    for review in filtered_iso_compatible_reviews:
        file.write(review + "\n")

print(f"\nSaved ISO-8859-1-compatible reviews to: {iso_file}")
# endregion

#region Globomantics - Binary File Archiver for Uploaded Shipping Docs
# Source files (simulating uploaded content)
pdf_source = "uploads/sample_invoice.pdf"
image_source = "uploads/sample_delivery.jpg"

# Target archive folder
archive_folder = "archived_docs"

# Ensure directories exist
# ok=true prevents an error if folder already exists
os.makedirs("uploads", exist_ok=True) 
os.makedirs(archive_folder, exist_ok=True)

# File destinations (creating them)
pdf_target = os.path.join(archive_folder, "2025-07-24_invoice_copy.pdf")
image_target = os.path.join(archive_folder, "2025-07-24_delivery_photo.jpg")

pdf_in = open(pdf_source, 'rb') # rb is binary mode
pdf_bytes = pdf_in.read()
pdf_in.close()

pdf_out = open(pdf_target, 'wb')
pdf_out.write(pdf_bytes)
pdf_out.close()

print(f"PDF archived {pdf_target} (Size: {len(pdf_bytes)} bytes)")

img_in = open(image_source, 'rb') # read with rb
img_bytes = img_in.read()
img_in.close()

img_out = open(image_target, 'wb') # write with wb
img_out.write(img_bytes)
img_out.close()

print(f"Image archived: {image_target} (Size: {len(img_bytes)} bytes)")
# use this approach for archiving non text content

#endregion

#region Globomantics - In-Memory & Temporary File Handler
# === Part 1: Using StringIO to simulate a text file upload (e.g., from a web form) ===
import tempfile
from io import StringIO # gives a file like object, but is stored in memory

uploaded_text = """Client ID: 45231
Region: East Hub
Notes: Package delayed due to weather
Resolution: Priority delivery requested"""

text_file = StringIO(uploaded_text) # wrap uploaded text into a stringio object
print("=== Reading Uploaded Text File From Memory ===")
for line in text_file:
    print(line.strip())

text_file.close()

# Part 2: Using BytesIO to simulate a binary file upload (e.g., image of PDF) ===
from io import BytesIO

# b prefix here indicates its a byte string
pdf_binary_data = b"%PDF-1.4\nDummy PDF File Header...\n..."

pdf_file = BytesIO(pdf_binary_data)
print("\n=== Reading Uploaded Binary File From Memory")
header = pdf_file.read(15)
print(f"Binary file header: {header}")

pdf_file.close()

# === Part 3: Using tempfile to create a temporary directory and write a review file ===
print("\n=== Writing Temporary Review File ===")
with tempfile.TemporaryDirectory() as tmp_dir:
    temp_path = os.path.join(tmp_dir, "client_review.txt")
    with open(temp_path, 'w') as temp_file:
        temp_file.write("Client: GLOBO123456\nRating: 4/5\nComment: Smooth process overall.")
    print(f"Temporary file created at: {temp_file}")

    with open(temp_path, 'r') as temp_file:
        print("Contents of temp file:")
        print(temp_file.read())
    
print("\nTemporary directory and file removed after block exits.")







