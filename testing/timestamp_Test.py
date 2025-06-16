# import datetime
#
# window_id = "20240607153045"  # example value
# dt = datetime.datetime.strptime(window_id, "%Y%m%d%H%M%S")
# timestamp_str = dt.isoformat()  # e.g., '2024-06-07T15:30:45'
# print(timestamp_str)


import datetime
import logging


def run():
# Get current datetime
    now = datetime.datetime.now()
    logging.info(f"Current datetime: {now}")

    # Format as window_id string
    window_id = now.strftime('%Y%m%d%H%M%S')
    logging.info(f"window_id string: {window_id}")

    # Parse back to datetime
    parsed_dt = datetime.datetime.strptime(window_id, '%Y%m%d%H%M%S')
    logging.info(f"Parsed datetime from window_id: {parsed_dt}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Script executed successfully.")
    # You can add more functionality here if needed