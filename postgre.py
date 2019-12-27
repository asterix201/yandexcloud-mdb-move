import requests
import logging
import json

from requests.exceptions import BaseHTTPError

from config import cfg

def cluster_postgres_restore(backup_data, cluster_data, cluster_hosts_data, network_id, subnet_id, options, headers):
    cluster_versions = options["versions"]
    version_get = cluster_versions["get"][cluster_data["config"]["version"]]
    effective_config = cluster_data["config"][version_get].get("effectiveConfig")
    version_post = cluster_versions["restore"][cluster_data["config"]["version"]]
    cluster_data["config"][version_post] = effective_config
    cluster_data["configSpec"] = cluster_data["config"]
    cluster_data.pop("config")

    cluster_host_spec = []
    for host in cluster_hosts_data["hosts"]:
        host_spec = {
            "resources": host["resources"],
            "zoneId": host["zoneId"],
            "subnetId": subnet_id,
            "assignPublicIp": host["assignPublicIp"]
        }

        # Optional features
        if host.get("replicationSource"):
            host_spec["replicationSource"] = host["replicationSource"]
        
        if host.get("config"):
            host_spec["configSpec"] = host["config"]

        if host.get("priority"):
            host_spec["priority"] = host["priority"]
        
        cluster_host_spec.append(host_spec)

    data = {
        "backupId": backup_data["id"],
        "time": backup_data["createdAt"],
        "name": cluster_data["name"],
        "environment": cluster_data["environment"],
        "networkId": network_id,
        "folderId": cluster_data["folderId"],
        "configSpec": cluster_data["configSpec"],
        "hostSpecs": cluster_host_spec,
        "description": cluster_data.get("description"),
        "labels": cluster_data.get("labels"),
    }


    url = f"{cfg['scheme']}://{cfg['mdb']['api_url']}/{options['path']}/clusters:restore"
    logging.info("Restoring cluster")
    with requests.Session() as s:
        s.headers.update(headers)
        try:
            r = s.post(url, data=json.dumps(data))
        except BaseHTTPError as e:
            logging.error("Network error: %s" % e)
            raise Exception("Network error: %s" % e)

        if r.status_code != 200:
            logging.error("Got status %s" % r.status_code)
            raise Exception("Got status %s. Details: %s" % (r.status_code, r.text))

        js = r.json()
        return js

