from reports import average_report


def test_average_report_single_endpoint(sample_logs):
    """Test average report with logs for a single endpoint"""

    result = average_report(sample_logs)

    # Check that the result is a string (tabulate output)
    assert isinstance(result, str)
    assert "Endpoint" in result
    assert "Count" in result
    assert "Avg Response Time" in result

    sample_urls = set()
    for log in sample_logs:
        sample_urls.add(log["url"])

    for url in sample_urls:
        assert url in result


def test_average_report_empty_input():
    """Test average report with empty input"""

    result = average_report([])
    assert isinstance(result, str)
    assert "Endpoint" in result
    assert "Count" in result
    assert "Avg Response Time" in result


def test_average_report_with_date_filter(sample_logs):
    """Test average report with date filtering"""

    result = average_report(sample_logs, "2025-22-06")
    assert isinstance(result, str)
    assert "Endpoint" in result


def test_average_report_with_invalid_date_filter(sample_logs):
    """Test average report with invalid date filter"""

    result = average_report(sample_logs, "2025-99-99")
    assert isinstance(result, str)

    # Should return empty table when no logs match the date
    sample_urls = set()
    for log in sample_logs:
        sample_urls.add(log["url"])
    for url in sample_urls:
        assert url not in result


def test_average_report_with_mixed_valid_invalid_logs(mixed_logs):
    """Test average report with mix of valid and invalid logs"""

    result = average_report(mixed_logs)
    assert isinstance(result, str)

    # Should only process the valid logs, skip the invalid one
    assert "/api/test" not in result
