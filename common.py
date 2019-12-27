import requests
import logging
import uuid
import json

from requests.exceptions import BaseHTTPError
from time import sleep

from config import cfg
from util import requests_retry_session

def cluster_get(cluster_id, path, headers):
    url = f"{cfg['scheme']}://{cfg['mdb']['api_url']}/{path}/clusters/{cluster_id}"
    logging.info("Fetching cluster")
    with requests.Session() as s:
        s.headers.update(headers)
        try:
            r = requests_retry_session(session=s).get(url)
        except BaseHTTPError as e:
            logging.error("Network error: %s" % e)
            return None

        if r.status_code != 200:
            logging.error("Got status %s" % r.status_code)
            return None

        js = r.json()
        return js


def cluster_backup(cluster_id, path, headers):
    url = f"{cfg['scheme']}://{cfg['mdb']['api_url']}/{path}/clusters/{cluster_id}:backup"
    logging.info("Backuping cluster")
    with requests.Session() as s:
        s.headers.update(headers)
        try:
            r = s.post(url)
        except BaseHTTPError as e:
            logging.error("Network error: %s" % e)
            raise Exception("Network error: %s" % e)

        if r.status_code != 200:
            logging.error("Got status %s" % r.status_code)
            raise Exception("Got status %s. Details: %s" % (r.status_code, r.text))

        js = r.json()
        return js


def cluster_rename(cluster_id, path, new_name, headers):
    _data = {
        "updateMask": "name",
        "name": new_name or uuid.uuid4().hex
    }
    url = f"{cfg['scheme']}://{cfg['mdb']['api_url']}/{path}/clusters/{cluster_id}"
    logging.info("Updating cluster")
    with requests.Session() as s:
        s.headers.update(headers)
        try:
            r = s.patch(url, data=json.dumps(_data))
        except BaseHTTPError as e:
            logging.error("Network error: %s" % e)
            raise Exception("Network error: %s" % e)

        if r.status_code != 200:
            logging.error("Got status %s" % r.status_code)
            raise Exception("Got status %s. Details: %s" % (r.status_code, r.text))

        js = r.json()
        return js


def cluster_get_hosts(cluster_id, path, headers):
    url = f"{cfg['scheme']}://{cfg['mdb']['api_url']}/{path}/clusters/{cluster_id}/hosts"
    logging.info("Fetching host list")
    with requests.Session() as s:
        s.headers.update(headers)
        try:
            r = requests_retry_session(session=s).get(url)
        except BaseHTTPError as e:
            logging.error("Network error: %s" % e)
            raise Exception("Network error: %s" % e)

        if r.status_code != 200:
            logging.error("Got status %s" % r.status_code)
            raise Exception("Got status %s. Details: %s" % (r.status_code, r.text))

        js = r.json()
        return js


def backup_get_latest(cluster_id, path, headers):
    url = f"{cfg['scheme']}://{cfg['mdb']['api_url']}/{path}/clusters/{cluster_id}/backups"
    logging.info("Fetching backup list")
    with requests.Session() as s:
        s.headers.update(headers)
        try:
            r = requests_retry_session(session=s).get(url)
        except BaseHTTPError as e:
            logging.error("Network error: %s" % e)
            raise Exception("Network error: %s" % e)

        if r.status_code != 200:
            logging.error("Got status %s" % r.status_code)
            raise Exception("Got status %s. Details: %s" % (r.status_code, r.text))

        js = r.json()
        if len(js.get("backups", [])) < 1:
            js = None
        else:
            js = js["backups"][0] # TODO: latest?

        return js

def network_list_subnets(network_id, headers):
    url = f"{cfg['scheme']}://{cfg['vpc']['api_url']}/{cfg['vpc']['path']}/{network_id}/subnets"
    logging.info("Fetching subnet list")
    with requests.Session() as s:
        s.headers.update(headers)
        try:
            r = requests_retry_session(session=s).get(url)
        except BaseHTTPError as e:
            logging.error("Network error: %s" % e)
            raise Exception("Network error: %s" % e)

        if r.status_code != 200:
            logging.error("Got status %s" % r.status_code)
            raise Exception("Got status %s. Details: %s" % (r.status_code, r.text))

        js = r.json()
        subnets = {}
        for subnet in js["subnets"]:
            subnets[subnet["zoneId"]] = subnet["id"]
        return js


def wait_for_operation(operation_id, headers):
    url = f"{cfg['scheme']}://{cfg['operations']['api_url']}/{cfg['operations']['path']}/{operation_id}"
    with requests.Session() as s:
        s.headers.update(headers)
        for _ in range(cfg["operations"]["wait"]):
            try:
                r = requests_retry_session(session=s).get(url)
            except BaseHTTPError as e:
                logging.error("Network error: %s" % e)
                continue

            if r.status_code != 200:
                logging.error("Got status %s" % r.status_code)
                raise Exception("Got status %s" % r.status_code)

            if not r.json().get("done"):
                sleep(1)
                continue

            break
