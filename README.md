# Log Analysis System

A powerful Python tool for analyzing logs, generating performance reports, and validating log data integrity. This system processes JSON log files and produces formatted reports with comprehensive validation and date filtering capabilities.

## 🚀 Features

- **📊 JSON Log Processing**: Read and parse JSON log files with flexible validation
- **✅ Data Validation**: 
  - Comprehensive log entry validation with type checking
  - Timestamp format validation (ISO 8601)
  - Required field validation (`@timestamp`, `status`, `url`,  `request_method`, `response_time`, `http_user_agent`)
  - Automatic filtering of invalid entries with detailed statistics
- **📅 Date Filtering**: Filter logs by specific dates using `--date` parameter
- **📈 Report Generation**:
  - Average response time reports by endpoint
  - Request count statistics
  - Formatted table output using tabulate
- **🔧 Decorator-based Validation**: Clean, reusable validation using Python decorators

## 📋 Requirements

- Python 3.11+
- pip (Python package installer)

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd logs_testovoye
   ```

2. **Create and activate virtual environment**:
   ```bash
   # On Windows
   python -m venv .venv
   .venv\Scripts\activate
   
   # On macOS/Linux
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Quick Start

### Basic Usage

Generate an average response time report:
```bash
python main.py json/example1.log --report average
```

### Date Filtering

Filter logs by specific date (format: YYYY-DD-MM):
```bash
python main.py json/example1.log --report average --date 2025-22-06
```

### Multiple Files

Process multiple log files at once:
```bash
python main.py json/example1.log json/example2.log --report average
```

## 📝 Log Format

The system expects JSON log entries with the following structure:

```json
{
  "@timestamp": "2025-06-22T13:57:32+00:00",
  "status": 200,
  "url": "/api/context/...",
  "request_method": "GET",
  "response_time": 0.024,
  "http_user_agent": "..."
}
```

### Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `@timestamp` | string | ISO 8601 formatted timestamp | `"2025-06-22T13:57:32+00:00"` |
| `status` | integer | HTTP status code | `200` |
| `url` | string | Request URL | `"/api/context/..."` |
| `request_method` | string | Request Method | `"GET"` |
| `response_time` | numeric | Response time in seconds | `0.024` |
| `http_user_agent` | string | User agent string | `"..."` |

## ✅ Validation System

The system automatically validates all log entries.



Invalid entries are automatically filtered out and won't affect the report generation.

## 📊 Reports

### Average Report

Generates a comprehensive table showing endpoint performance metrics:

| Column | Description |
|--------|-------------|
| **Endpoint** | The API endpoint URL |
| **Count** | Number of requests to that endpoint |
| **Avg Response Time** | Average response time in seconds |

#### Example Output

```
| Endpoint           |   Count |   Avg Response Time |
|--------------------|---------|-------------------|
| /api/context/...   |      20 |             0.032 |
| /api/homeworks/... |      15 |             0.128 |
| /api/users/...     |      10 |             0.072 |
| /api/specializations/... | 8 |             0.044 |
```

## 🏗️ Project Structure

```
logs_testovoye/
├── main.py                 # Main CLI application
├── reports/
│   ├── __init__.py        # Report registry
│   └── all_reports.py     # Report generation functions
├── validation/
│   ├── __init__.py        # Validation registry
│   └── validate_logs.py   # Log validation logic
├── tests/
│   ├── __init__.py        # Test registry
│   ├── test_reports.py    # Report function tests
│   ├── test_validation.py # Validation logic tests
│   └── conftest.py        # Test fixtures
├── json/                  # Sample log files
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_validation.py



### Test Coverage

The project includes comprehensive tests for:
- ✅ Log validation logic
- ✅ Report generation functions
- ✅ Date filtering functionality
- ✅ Decorator behavior

## 🔧 Development

### Adding New Reports

1. **Create a new report function** in `reports/all_reports.py`:
   ```python
   @validate_logs
   def new_report(logs: list[dict]) -> str:
       """Create new report from logs data"""

       # Your report logic here
       return tabulate(table, headers=headers, tablefmt="github")
   ```

2. **Add the function** to the `REPORTS` dictionary in `reports/__init__.py`:
   ```python
   REPORTS = {
       "average": average_report,
       "new_report": new_report,  # Add your new report
   }
   ```

3. **Add corresponding tests** in `tests/test_reports.py`

### Validation Rules

The validation system checks:
- All required fields are present
- Timestamp is in valid format
- Status is an integer
- URL is a string
- Request method is string
- Response time is numeric (int or float)
- User agent is a string

## 📦 Dependencies

### Production Dependencies
- `tabulate`: For formatted table output

### Development Dependencies
- `pytest`: For testing framework
