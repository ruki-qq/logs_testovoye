from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional


def validate_log_entry(log: dict[str, Any]) -> bool:
    """Validate if log entry contains all necessary keys with correct types"""

    required_keys = {
        "@timestamp",
        "status",
        "url",
        "request_method",
        "response_time",
        "http_user_agent",
    }

    # Check if all required keys exist
    if not all(key in log for key in required_keys):
        return False

    # Validate types
    try:
        # Try to parse the timestamp
        datetime.fromisoformat(log["@timestamp"])
        date = datetime.fromisoformat("2025-06-22 13:57:32")
        print(date)

        # Validate status (should be integer)
        if not isinstance(log["status"], int):
            return False

        # Validate url (should be string)
        if not isinstance(log["url"], str):
            return False

        # Validate request_method (should be string)
        if not isinstance(log["request_method"], str):
            return False

        # Validate response_time (should be numeric)
        response_time = log["response_time"]
        if not isinstance(response_time, (int, float)):
            return False

        # Validate http_user_agent (should be string)
        if not isinstance(log["http_user_agent"], str):
            return False

        return True

    except (ValueError, TypeError):
        return False


def validate_logs(func: Callable) -> Callable:
    """Decorator to validate log entries before processing"""

    @wraps(func)
    def wrapper(logs: list[dict], date_filter: Optional[str] = None, *args, **kwargs):
        valid_logs = []
        invalid_line_numbers = []

        # Check each log entry and track invalid ones
        for idx, log in enumerate(logs, 1):
            if validate_log_entry(log):
                # Apply date filter if specified
                if date_filter:
                    try:
                        log_date = datetime.fromisoformat(log["@timestamp"]).date()
                        filter_date = datetime.strptime(date_filter, "%Y-%d-%m").date()
                        if log_date != filter_date:
                            continue
                    except (ValueError, TypeError):
                        continue
                valid_logs.append(log)
            else:
                invalid_line_numbers.append(idx)

        if invalid_line_numbers:
            print(f"Invalid entries: {len(invalid_line_numbers)}")
            print(f"Invalid line numbers: {invalid_line_numbers}")

        if date_filter:
            print(f"Filtered by date: {date_filter}")
            print(f"Valid entries after date filtering: {len(valid_logs)}")

        return func(valid_logs, *args, **kwargs)

    return wrapper
