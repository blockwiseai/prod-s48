import json
from datetime import datetime
from typing import Any


class Logger:
    def __init__(self, log_file_path: str):
        """
        Initialize the logger with the file path to store logs.

        :param log_file_path: Path to the log file.
        """
        self.log_file_path = log_file_path

    def _get_timestamp(self) -> int:
        """
        Get the current UTC timestamp.

        :return: Current UTC timestamp in seconds.
        """
        return int(datetime.utcnow().timestamp())

    def log(self, data_type: str, data: Any, send_receive: str):
        """
        Log a message to the log file in the specified format.

        :param data_type: Type of the data being logged.
        :param data: The actual data to log.
        :param send_receive: Whether the data was 'send' or 'receive'.
        """
        log_entry = {
            "timestamp": self._get_timestamp(),
            "data_type": data_type,
            "data": data,
            "send_receive": send_receive,
        }

        # Append log to the specified file in JSON format
        with open(self.log_file_path, "a") as log_file:
            log_file.write(json.dumps(log_entry) + "\n")

    def log_event(
        self, event_id: str, description: str, probability: float, send_receive: str
    ):
        """
        Log a specific event with more structured data.

        :param event_id: The ID of the event.
        :param description: Description of the event.
        :param probability: Probability value for the event.
        :param send_receive: Whether the data was 'send' or 'receive'.
        """
        event_data = {
            "event_id": event_id,
            "description": description,
            "probability": probability,
        }

        self.log(data_type="event", data=event_data, send_receive=send_receive)
