from tabulate import tabulate

from validation import validate_logs


@validate_logs
def average_report(logs: list[dict]) -> str:
    """Create report with endpoint stats: count and average response time"""

    stats = {}
    for log in logs:
        url = log.get("url")
        resp_time = log.get("response_time")

        # Initialize stats for new endpoint
        if url not in stats:
            stats[url] = {"count": 0, "total_time": 0.0}

        stats[url]["count"] += 1
        stats[url]["total_time"] += float(resp_time)

    # Create table with stats
    table = []
    for url, data in stats.items():
        avg_time = data["total_time"] / data["count"] if data["count"] else 0
        table.append([url, data["count"], round(avg_time, 4)])
    return tabulate(
        table, headers=["Endpoint", "Count", "Avg Response Time"], tablefmt="github"
    )
