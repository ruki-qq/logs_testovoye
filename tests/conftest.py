import pytest


@pytest.fixture
def sample_logs():
    return [
        {
            "@timestamp": "2025-06-22T13:57:32+00:00",
            "status": 200,
            "url": "/api/context/...",
            "request_method": "GET",
            "response_time": 0.024,
            "http_user_agent": "...",
        },
        {
            "@timestamp": "2025-06-22T13:57:32+00:00",
            "status": 200,
            "url": "/api/homeworks/...",
            "request_method": "GET",
            "response_time": 0.06,
            "http_user_agent": "...",
        },
        {
            "@timestamp": "2025-06-23T13:57:34+00:00",
            "status": 200,
            "url": "/api/context/...",
            "request_method": "GET",
            "response_time": 0.032,
            "http_user_agent": "...",
        },
    ]


@pytest.fixture
def valid_log_entry():
    return {
        "@timestamp": "2025-06-22T13:57:32+00:00",
        "status": 200,
        "url": "/api/context/...",
        "request_method": "GET",
        "response_time": 0.024,
        "http_user_agent": "...",
    }


@pytest.fixture
def valid_log_entry_with_int_respone_time():
    return {
        "@timestamp": "2025-06-22T13:57:32+00:00",
        "status": 200,
        "url": "/api/test",
        "request_method": "GET",
        "response_time": 1,  # Integer is valid
        "http_user_agent": "test",
    }


@pytest.fixture
def invalid_log_entry():
    return {
        # Missing required fields
        "url": "/api/test",
        "response_time": 0.1,
    }


@pytest.fixture
def invalid_log_entry_with_wrong_timestamp_type():
    return {
        "@timestamp": 123,  # Should be string
        "status": 200,
        "url": "/api/test",
        "request_method": "GET",
        "response_time": 0.1,
        "http_user_agent": "test",
    }


@pytest.fixture
def invalid_log_entry_with_wrong_status_type():
    return {
        "@timestamp": "2025-06-22T13:57:32+00:00",
        "status": "200",  # Should be int
        "url": "/api/test",
        "request_method": "GET",
        "response_time": 0.1,
        "http_user_agent": "test",
    }


@pytest.fixture
def invalid_log_entry_with_wrong_url_type():
    return {
        "@timestamp": "2025-06-22T13:57:32+00:00",
        "status": 200,
        "url": 1,  # Should be string
        "request_method": "GET",
        "response_time": "0.1",
        "http_user_agent": "test",
    }


@pytest.fixture
def invalid_log_entry_with_wrong_request_method_type():
    return {
        "@timestamp": "2025-06-22T13:57:32+00:00",
        "status": 200,
        "url": "/api/test",
        "request_method": 1,  # Should be string
        "response_time": "0.1",
        "http_user_agent": "test",
    }


@pytest.fixture
def invalid_log_entry_with_wrong_response_time_type():
    return {
        "@timestamp": "2025-06-22T13:57:32+00:00",
        "status": 200,
        "url": "/api/test",
        "request_method": "GET",
        "response_time": "0.1",  # Should be numeric
        "http_user_agent": "test",
    }


@pytest.fixture
def invalid_log_entry_with_wrong_useragent_type():
    return {
        "@timestamp": "2025-06-22T13:57:32+00:00",
        "status": 200,
        "url": "/api/test",
        "request_method": "GET",
        "response_time": 0.1,
        "http_user_agent": 123,  # Should be string
    }


@pytest.fixture
def mixed_logs():
    """Log entries with mix of valid and invalid data"""

    return [
        {
            "@timestamp": "2025-06-22T13:57:32+00:00",
            "status": 200,
            "url": "/api/context/...",
            "request_method": "GET",
            "response_time": 0.024,
            "http_user_agent": "...",
        },
        {
            # Missing required fields
            "url": "/api/test",
            "response_time": 0.1,
        },
        {
            "@timestamp": "2025-06-22T13:57:32+00:00",
            "status": 200,
            "url": "/api/homeworks/...",
            "request_method": "GET",
            "response_time": 0.06,
            "http_user_agent": "...",
        },
    ]
