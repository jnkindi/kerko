"""
Custom filters for Jinja2 templates.
"""

from urllib.parse import urlparse

from w3lib.url import safe_url_string

from .datetime import format_datetime, reformat_date


def register_filters(blueprint):
    """Add custom template filters."""
    blueprint.add_app_template_filter(format_datetime, name='kerko_format_datetime')
    blueprint.add_app_template_filter(reformat_date, name='kerko_reformat_date')
    blueprint.add_app_template_filter(
        lambda text: urlparse(text).hostname, name='kerko_url_hostname'
    )
    blueprint.add_app_template_filter(safe_url_string, name='kerko_url_sanitize')
