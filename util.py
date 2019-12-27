import requests
import logging

from requests.exceptions import BaseHTTPError
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from time import sleep

from config import cfg


def requests_retry_session(
    retries=cfg.get("mdb", {}).get("retries", 3),
    backoff_factor=cfg.get("mdb", {}).get("backoff_factor", 0.3),
    status_forcelist=(500, 502, 504),
    session=None):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('%s://' % cfg.get("scheme", "https"), adapter)
    return session
