from config import cfg

from common import cluster_get, cluster_backup, cluster_rename, backup_get_latest, cluster_get_hosts, wait_for_operation
from postgre import cluster_postgres_restore
from mongodb import cluster_mongodb_restore
from mysql import cluster_mysql_restore
from redis import cluster_redis_restore

_headers = {
    "Content-Type": "application/json"
}

_restore_func = {
      "postgresql": cluster_postgres_restore,
      "mongodb": cluster_mongodb_restore,
      "mysql": cluster_mysql_restore,
      "redis": cluster_redis_restore
}

def _check_event(event):
    if not event.get("queryStringParameters"):
        raise Exception("No query parameters found")

    if not event["queryStringParameters"].get("cluster_id"):
        raise Exception("Function expects query parameter cluster_id")

    if not event["queryStringParameters"].get("network_id"):
        raise Exception("Function expects query parameter network_id")

    if not event["queryStringParameters"].get("subnet_id"):
        raise Exception("Function expects query parameter subnet_id")


def main(event, context):
    _check_event(event)
    _headers["Authorization"] = "Bearer {}".format(context['token']["access_token"]) # TODO: .token

    cluster_id = event["queryStringParameters"].get("cluster_id")
    network_id = event["queryStringParameters"].get("network_id")
    subnet_id = event["queryStringParameters"].get("subnet_id")
    new_name = event["queryStringParameters"].get("new_name")
    redis_password = event["queryStringParameters"].get("redis_password")

    for cluster_type, options in cfg["mdb"]["types"].items():
        data_get = cluster_get(cluster_id, options["path"], _headers)
        if data_get:
            break
    
    if not data_get:
        raise Exception("Cluster %s not found" % cluster_id)

    # data_backup = cluster_backup(cluster_id, options["path"], _headers)
    # if "error" in data_backup:
    #     raise Exception(data_backup["error"])

    # wait_for_operation(data_backup["id"], _headers)

    data_upate = cluster_rename(cluster_id, options["path"], new_name, _headers)
    wait_for_operation(data_upate["id"], _headers)

    data_latest_backup = backup_get_latest(cluster_id, options["path"], _headers)
    cluster_hosts_data = cluster_get_hosts(cluster_id, options["path"], _headers)

    kwargs = {
        "backup_data": data_latest_backup,
        "cluster_data": data_get,
        "cluster_hosts_data": cluster_hosts_data,
        "network_id": network_id,
        "subnet_id": subnet_id,
        "options": options,
        "headers": _headers
    }

    if redis_password:
        kwargs["password"] = redis_password

    data_restore = _restore_func[cluster_type](**kwargs)
    # wait_for_operation(data_restore["id"], _headers)
    
    return data_restore
