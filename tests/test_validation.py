from validation import validate_log_entry, validate_logs


def test_validate_log_entry_valid(valid_log_entry):
    """Test validation with valid log entry"""
    assert validate_log_entry(valid_log_entry) is True


def test_validate_log_entry_missing_timestamp(invalid_log_entry):
    """Test validation with missing fields"""

    assert validate_log_entry(invalid_log_entry) is False


def test_validate_log_entry_invalid_timestamp_type(
    invalid_log_entry_with_wrong_timestamp_type,
):
    """Test validation with invalid timestamp type"""

    assert validate_log_entry(invalid_log_entry_with_wrong_timestamp_type) is False


def test_validate_log_entry_invalid_status_type(
    invalid_log_entry_with_wrong_status_type,
):
    """Test validation with invalid status type"""

    assert validate_log_entry(invalid_log_entry_with_wrong_status_type) is False


def test_validate_log_entry_invalid_url_type(invalid_log_entry_with_wrong_url_type):
    """Test validation with invalid url type"""

    assert validate_log_entry(invalid_log_entry_with_wrong_url_type) is False


def test_validate_log_entry_invalid_request_method_type(
    invalid_log_entry_with_wrong_request_method_type,
):
    """Test validation with invalid request_method type"""

    assert validate_log_entry(invalid_log_entry_with_wrong_request_method_type) is False


def test_validate_log_entry_invalid_response_time_type(
    invalid_log_entry_with_wrong_response_time_type,
):
    """Test validation with invalid response_time type"""

    assert validate_log_entry(invalid_log_entry_with_wrong_response_time_type) is False


def test_validate_log_entry_invalid_user_agent_type(
    invalid_log_entry_with_wrong_useragent_type,
):
    """Test validation with invalid http_user_agent type"""

    assert validate_log_entry(invalid_log_entry_with_wrong_useragent_type) is False


def test_validate_log_entry_with_integer_response_time(
    valid_log_entry_with_int_respone_time,
):
    """Test validation with integer response_time"""

    assert validate_log_entry(valid_log_entry_with_int_respone_time) is True


# Test the decorator functionality
def test_validate_logs_decorator_with_valid_logs(sample_logs):
    """Test the validation decorator with all valid logs"""

    @validate_logs
    def test_function(logs):
        return len(logs)

    result = test_function(sample_logs)
    assert result == 3  # All 3 logs should be valid


def test_validate_logs_decorator_with_mixed_logs(mixed_logs):
    """Test the validation decorator with mix of valid and invalid logs"""

    @validate_logs
    def test_function(logs):
        return len(logs)

    result = test_function(mixed_logs)
    assert result == 2  # Only 2 valid logs should be processed


def test_validate_logs_decorator_with_date_filter(sample_logs):
    """Test the validation decorator with date filtering"""

    @validate_logs
    def test_function(logs):
        return len(logs)

    result = test_function(sample_logs, "2025-22-06")
    assert result == 2  # Only 2 logs from 2025-06-22 should be included


def test_validate_logs_decorator_with_invalid_date_filter(sample_logs):
    """Test the validation decorator with invalid date filter"""

    @validate_logs
    def test_function(logs):
        return len(logs)

    result = test_function(sample_logs, "2025-99-99")
    assert result == 0  # No logs should match invalid date
