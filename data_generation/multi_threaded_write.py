import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import random


# Function to generate a chunk of records
def generate_chunk(start, end, timestamp):
    records = []
    for i in range(start, end):
        message_id = f"{i:09d}"  # Format message_id as zero-padded 9-digit number
        account_id = random.randint(1, 100000)  # Generate random account ID
        transaction_amount = random.randint(500, 10000)  # Generate random transaction amount
        external_account_number = random.randint(250000, 1000000)  # Generate random external account number
        records.append(f"{message_id},{timestamp},{account_id},{transaction_amount},{external_account_number}\n")
    return records


# Function to write all records to a file at once
def write_to_file(output_file, all_records):
    header = "resource_id,timestamp,account_id,transaction_amount,external_account_number\n"  # Define the header
    with open(output_file, 'w', buffering=1024 * 1024) as file:  # Buffered I/O for faster writing
        file.write(header)  # Write the header first
        file.writelines(all_records)  # Write the records


# Main function to generate records using multithreading
def generate_records_multithreaded(output_file, total_records, num_threads=4):
    chunk_size = total_records // num_threads
    all_records = []
    timestamp = datetime.now().isoformat()  # Generate timestamp once

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for i in range(num_threads):
            start = i * chunk_size + 1
            end = start + chunk_size if i < num_threads - 1 else total_records + 1
            futures.append(executor.submit(generate_chunk, start, end, timestamp))

        # Collect all generated records
        for future in futures:
            all_records.extend(future.result())

    # Write all records to the file in one operation
    write_to_file(output_file, all_records)


if __name__ == "__main__":
    start_time = time.time()
    generate_records_multithreaded("output.csv", 50_000_000, num_threads=8)
    print(f"Finished generating 50 million records in {time.time() - start_time:.2f} seconds.")