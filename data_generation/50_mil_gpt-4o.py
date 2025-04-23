import time
from datetime import datetime

# Decorator to measure execution time
def time_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds to execute.")
        return result
    return wrapper

@time_execution
def generate_records(output_file, total_records):
    with open(output_file, 'w', buffering=1024*1024) as file:  # Use buffered I/O for faster writing
        for i in range(1, total_records + 1):
            message_id = f"{i:09d}"  # Format message_id as zero-padded 9-digit number
            current_timestamp = datetime.now().isoformat()
            file.write(f"{message_id},{current_timestamp}\n")

if __name__ == "__main__":
    generate_records("output.csv", 50_000_000)