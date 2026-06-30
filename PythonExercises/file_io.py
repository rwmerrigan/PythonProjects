#region Froms and Imports
from datetime import datetime
from io import StringIO # gives a file like object, but is stored in memory
from pathlib import Path
from datetime import date
import xml.etree.cElementTree as ET
import os
import sys
import platform
import tempfile
import csv
import json
import shutil
import stat
import time
#endregion

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
#endregion

#region Globomantics - Full CSV Handling: Importing, Updating, and Exporting Product Data
# Setup
os.makedirs("data", exist_ok=True)

# File paths
supplier_csv_path = "data/supplier_products.csv"
updated_csv_rows = "data/updated_products_row.csv"
updated_csv_dicts = "data/updated_products_dict.csv"

# --- Step 1: Write sample supplier CSV using csv.writer (row-based) ---
print("Creating supplier csv using csv.writer...")

with open(supplier_csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["SKU", "Product", "Weight(kg)", "Status"])
    writer.writerow(["GLOBO-001", "Smart Tracker", "0.12", "Available"])
    writer.writerow(["GLOBO-002", "Thermal Label Printer", "0", "Available"])
    writer.writerow(["GLOBO-003", "Warehouse Scanner", "0.8", "Available"])

print(f"Supplier CSV created at: {supplier_csv_path}\n")

updated_rows = []

with open(supplier_csv_path, 'r', newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        weight = float(row[2])
        if weight == 0:
            row[3] = "Out of stock"
        updated_rows.append(row)

with open(updated_csv_rows, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(updated_rows)

print(f"Row-based updated file written to: {updated_csv_rows}\n")

print("Re-reading with csv.DictReader for structured parsing...")

products = []

with open(supplier_csv_path, 'r', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        weight = float(row["Weight(kg)"])
        if weight == 0:
            row["Status"] = "Out of Stock"
        products.append(row)

with open(updated_csv_dicts, 'w', newline='') as f:
    fieldnames = ["SKU", "Product", "Weight(kg)", "Status"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products)

print(f"Dict-based updated file written to: {updated_csv_dicts}")
#endregion

#region Globomantics - User Preferences Handler using JSON
# Ensure the config folder exists
os.makedirs("config", exist_ok=True)

# File to store preferences
prefs_file = "config/user_preferences.json"

# --- Step 1: Define sample user preferences (nested/heiarchical structure)
user_preferences = {
    "user_id": "logistics_manager_01", 
    "region_filter": ["North America", "Europe"],
    "alerts": {
        "delivery_delay": True,
        "temperature_threshold": 5.0
    },
    "dashboard_layout": {
        "theme": "dark", 
        "widgets": ["shipment_map", "latest_orders", "alert_panel"]
    }
}

with open(prefs_file, 'w') as file:
    # takes user_preferences and writes as json into the file
    json.dump(user_preferences, file, indent=4)

print(f"Preferences saved to file: {prefs_file}")

with open(prefs_file, 'r') as file:
    # json.load turns the data in the file into a dictionary 
    loaded_preferences = json.load(file)

print("\nLoaded preferences from file:")
print(loaded_preferences)

# non file approach to the same problem 
# dumps converts the python object into a string, s in dumps standing for string
json_string = json.dumps(user_preferences, indent=2) 
print("\nPreferences as JSON string:")
print(json_string)

# similar to dumps, loads takes a json string and converts it into a python
# object, s in loads stands for string
parsed_from_string = json.loads(json_string)
print("\nParsed JSON from string (dict):")
print(parsed_from_string)
#endregion

#region Globomantics - Product Catalog Processor (XML)
# Ensure the directory exists
os.makedirs("xml_data", exist_ok=True)

# File paths
input_xml_path = "xml_data/supplier_product_catalog.xml"
output_xml_path = "xml_data/internal_product_catalog.xml"

# --- Step 1: Create sample XML Catalog ---
sample_xml = '''<?xml version="1.0"?>
<catalog>
    <product>
        <id>GLOBO-001</id>
        <name>Smart Tracker</name>
        <weight>0.12</weight>
        <status>Available</status>
    </product>
    <product>
        <id>GLOBO-002</id>
        <name>Thermal Label Printer</name>
        <weight>0</weight>
        <status>Available</status>
    </product>
    <product>
        <id>GLOBO-003</id>
        <name>Warehouse Scanner</name>
        <weight>0.8</weight>
        <status>Available</status>
    </product>
</catalog>
'''

with open(input_xml_path, 'w') as f:
    f.write(sample_xml)

print(f"Sample product catalog saved to: {input_xml_path}")

tree = ET.parse(input_xml_path)
root = tree.getroot()

print("\nParsing product catalog and updating stock status...")

for product in root.iter("product"):
    weight = float(product.find("weight").text)
    status_elem = product.find("status")
    if weight == 0:
        status_elem.text = "Out of stock"
    print(f"-> {product.find('id').text}: {status_elem.text}")

tree.write(output_xml_path, encoding="utf-8", xml_declaration=True)
print(f"\nUpdated catalog written to: {output_xml_path}")
#endregion

#region Globomantics - Deployment Directory Manager
# --- Step 1: Define deployment structure for a new project region
region_code = "LATAM"
base_dir = Path("deployments") / region_code

subfolders = ["configs", "logs", "reports"]

print(f"\nSetting up deployment structure for region: {region_code}")

if not base_dir.exists():
    base_dir.mkdir(parents=True) # makes sure any missing parent dirs are created 
    print(f"Created base directory: {base_dir}")
else:
    print(f"Directory already exists: {base_dir}")

for folder in subfolders:
    full_path = os.path.join(base_dir, folder) # create the folder path in the base_dir
    if not os.path.exists(full_path):
        os.mkdir(full_path)
        print(f"Created {full_path}")
    else:
        print(f"Already exists: {full_path}")

cleanup = False # whether or not we want to delete everything after setup
if cleanup: # if cleanup is true
    import shutil
    shutil.rmtree(base_dir)
    print(f"\nCleaned up deployment folder for region: {region_code}")
else:
    print(f"\nDeployment structure created and ready")

reports_path = os.path.join(base_dir, "reports")
# check if the folder exists and if theres nothing inside it
if os.path.exists(reports_path) and not os.listdir(reports_path):
    os.rmdir(reports_path) # remove dir
    print(f"Deleted empty folder: {reports_path}")
else:
    print(f"Cannot delete {reports_path}: Not empty or doesn't exist.")

print("\nFinal folder structure: ")
for folder in base_dir.iterdir():
    # example of a code block in a print f 
    print(f" - {folder.name} {'Deleted' if not folder.exists() else ''}")
#endregion

#region Globomantics - Report Archiver for Daily Logistics Report
# Setup: Define file structure
region = "North"
today = date.today().isoformat() # e.g., '2025-07-24'

source_folder = "reports/incoming"
archive_folder = "archive/archive"
central_folder = "central/consolidated"

# Ensure folders exist
os.makedirs(source_folder, exist_ok=True)
os.makedirs(archive_folder, exist_ok=True)
os.makedirs(central_folder, exist_ok=True)

incoming_filename = "shipment_report.txt"
incoming_path = os.path.join(source_folder, incoming_filename)

if not os.path.exists(incoming_path):
    with open(incoming_path, 'w') as f:
        f.write("ShipmentID,Status,Region,\n1001,Delivered,North\n1002,In Transit,North\n")
else:
    print(f"Using existing report: {incoming_path}")

input("This is a pause...")

renamed_filename = f"{today}_{region}_shipment_report.txt"
renamed_path = os.path.join(source_folder, renamed_filename)

if not os.path.exists(renamed_path):
    os.rename(incoming_path, renamed_path)
else:
    print(f"Skipping rename: {renamed_filename} already exists.")

archived_path = os.path.join(archive_folder, renamed_filename)
shutil.copy(renamed_path, archived_path)
print(f"Copied report to archive: {archived_path}")

final_destination = os.path.join(central_folder, renamed_filename)
shutil.move(renamed_path, final_destination)
print(f"Moved report to central location: {final_destination}")
#endregion

#region Globomantics - Payroll Report Security Script
# Setup: Simulate a sensitive payroll export
os.makedirs("exports", exist_ok=True)
payroll_path = "exports/payroll_2025_Q3.csv"

if not os.path.exists(payroll_path):
    with open(payroll_path, 'w') as f:
        f.write("EmployeeID,Name,GrossSalary\n101,Alice,85000\n102,Bob,90000\n")
    print(f"Created payroll export: {payroll_path}")
else:
    print(f"Found existing payroll file: {payroll_path}")

print("\nChecking file accessibility...")

can_read = os.access(payroll_path, os.R_OK)
can_write = os.access(payroll_path, os.W_OK)
can_execute = os.access(payroll_path, os.X_OK)

print(f"Readable? {'OK' if can_read else 'Not OK'}")
print(f"Writeable? {'OK' if can_write else 'Not OK'}")
print(f"Executable? {'OK' if can_write else 'Not OK'}")

print("\nFile Metadata:")
stats = os.stat(payroll_path)

print(f" - Size: {stats.st_size} bytes")
print(f" - Last modified: {time.ctime(stats.st_mtime)}")
print(f" - Permissions (octal): {oct(stats.st_mode)}")

print("\nApplying secure permissions (owner read/write only)...")

os.chmod(payroll_path, stat.S_IRUSR | stat.S_IWUSR)

updated_stats = os.stat(payroll_path)
print(f" - Updated permissions (octal): {oct(updated_stats.st_mode)}")

print("\nVerifying access after chmod:")
print(f"Readable? {'OK' if os.access(payroll_path, os.R_OK) else 'Not OK'}")
print(f"Writeable? {'OK' if os.access(payroll_path, os.W_OK) else 'Not OK'}")
print(f"Executable? {'OK' if os.access(payroll_path, os.X_OK) else 'Not OK'}")

#endregion

#region Globomantics - Regional Configuration Loader
# Define expected config path (simulate a missing file)
region = "EMEA"
config_path = f"configs/{region}_config.ini"
default_config = {
    "currency": "USD",
    "timezone": "UTC", 
    "retry_limit": "3"
}

# Step 1: Attempt to load configuration file ---
print(f"Loading config for region: {region}")

config_data = ""

try:
    config_file = open(config_path, 'r')
    config_data = config_file.read()
    print(f"Loaded config from file:\n{config_data}")
except FileNotFoundError: # if the config file does not exist create a default file
    print(f"File not found: {config_path}. Creating file with default config")
    # ini file string syntax, write the key value pairs to the file
    config_data = "\n".join(f"{k}={v}" for k, v in default_config.items())

    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    with open(config_path, 'w') as new_file:
        new_file.write(config_data)
    print(f"Created new config file: {config_path}")
except PermissionError: # in case of a locked down system or permissions errors
    print(f"Permission denied: Cannot access {config_path}. Using in-memory defaults.")
    # again, writing the key value pairs of the default config dict to the file
    config_data = "\n".join(f"{k}={v}" for k, v in default_config.items())
finally:
    # if the file was open and hasn't been closed, we close it
    if 'config_file' in locals() and not config_file.closed:
        config_file.close()
        print("File closed correctly.")



#endregion

#region Globomantics - Safe Concurrent Logger
log_file = "logs/shipment_activity.log"
os.makedirs("logs", exist_ok=True)

log_entry = f"[{time.strftime('%Y-%m-%d %H:%M%S')}] Shipment update from service {os.getpid()}\n"

def write_with_native_locking(filepath, data):
    if platform.system() == "Windows":
        import msvcrt
        with open(filepath, "a") as f:
            print("Locking with msvcrt...")
            # locks the number of bytes we write
            msvcrt.locking(f.fileno(), msvcrt.LK_LOCK, len(data))
            f.write(data)
            f.flush()
            time.sleep(1)
            input("...") # interacting with the file here should show an error
            msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, len(data))
            print("Unlocked")
    else: 
        import fcntl # linux system
        with open(filepath, "a") as f:
            print("Locking with fcntl...")
            f.write(data)
            f.flush()
            time.sleep(1)
            fcntl.flock(f, fcntl.LOCK_UN)
            print("Unlocked")

def write_with_portalocker(filepath, data):
    import portalocker
    with open(filepath, "a") as f:
        print("Locking with portalocker...")
        portalocker.lock(f, portalocker.LOCK_EX)
        f.write(data)
        f.flush()
        time.sleep(1)
        input("...") # interacting with the file here should show an error
        portalocker.unlock(f)
        print("Unlocked portalocker...")

print("\nAppending log entry safely...")
method = sys.argv[1] if len(sys.argv) > 1 else "native"

try:
    if method == "portalocker":
        write_with_portalocker(log_file, log_entry)
    else:
        write_with_native_locking(log_file, log_entry)
except Exception as e:
    print(f"Error during write {e}")

print("\nLog entry complete.")
#endregion


