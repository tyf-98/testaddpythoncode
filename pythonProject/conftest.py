# conftest.py
import datetime


def pytest_configure(config):
    if config.option.htmlpath:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        config.option.htmlpath = f"reports/report_{timestamp}.html"