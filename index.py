import logging

from grpc import RpcError

import yandex.cloud.mdb.mongodb.v1.cluster_pb2 as mongodb_cluster_pb
import yandex.cloud.mdb.mongodb.v1.cluster_service_pb2 as mongodb_cluster_service
import yandex.cloud.mdb.mongodb.v1.cluster_service_pb2_grpc as mongodb_cluster_service_grpc

import yandex.cloud.mdb.postgresql.v1.cluster_pb2 as postgresql_cluster_pb
import yandex.cloud.mdb.postgresql.v1.cluster_service_pb2 as postgresql_cluster_service
import yandex.cloud.mdb.postgresql.v1.cluster_service_pb2_grpc as postgresql_cluster_service_grpc

import yandex.cloud.mdb.mysql.v1.cluster_pb2 as mysql_cluster_pb
import yandex.cloud.mdb.mysql.v1.cluster_service_pb2 as mysql_cluster_service
import yandex.cloud.mdb.mysql.v1.cluster_service_pb2_grpc as mysql_cluster_service_grpc

import yandex.cloud.mdb.redis.v1.cluster_pb2 as redis_cluster_pb
import yandex.cloud.mdb.redis.v1.cluster_service_pb2 as redis_cluster_service
import yandex.cloud.mdb.redis.v1.cluster_service_pb2_grpc as redis_cluster_service_grpc

import yandex.cloud.mdb.clickhouse.v1.cluster_pb2 as clickhouse_cluster_pb
import yandex.cloud.mdb.clickhouse.v1.cluster_service_pb2 as clickhouse_cluster_service
import yandex.cloud.mdb.clickhouse.v1.cluster_service_pb2_grpc as clickhouse_cluster_service_grpc

import yandexcloud

import common
from mongo import restore_cluster as mongodb_restore
from postgresql import restore_cluster as postgresql_restore
from mysql import restore_cluster as mysql_restore
from redis import restore_cluster as redis_restore
from clickhouse import restore_cluster as clickhouse_restore

_restore_func = {
    "mongodb": mongodb_restore,
    "postgresql": postgresql_restore,
    "mysql": mysql_restore,
    "redis": redis_restore,
    "clickhouse": clickhouse_restore,
}

class GRPC():
    def __init__(self, cluster_pb, cluster_service, cluster_service_grpc):
        self.cluster_pb = cluster_pb
        self.cluster_service = cluster_service
        self.cluster_service_grpc = cluster_service_grpc


_cluster_types = {
    "mongodb": GRPC(mongodb_cluster_pb, mongodb_cluster_service, mongodb_cluster_service_grpc),
    "postgresql": GRPC(postgresql_cluster_pb, postgresql_cluster_service, postgresql_cluster_service_grpc),
    "mysql": GRPC(mysql_cluster_pb, mysql_cluster_service, mysql_cluster_service_grpc),
    "redis": GRPC(redis_cluster_pb, redis_cluster_service, redis_cluster_service_grpc),
    "clickhouse": GRPC(clickhouse_cluster_pb, clickhouse_cluster_service, clickhouse_cluster_service_grpc),
}


def _check_event(event):
    if not event.get("queryStringParameters"):
        raise Exception("No query parameters found")

    if not event["queryStringParameters"].get("cluster_id"):
        raise Exception("Function expects query parameter cluster_id")

    if not event["multiValueQueryStringParameters"].get("subnet_id"):
        raise Exception("Function expects query parameter subnet_id")


def main(event, context):
    _check_event(event)
    cluster_id = event["queryStringParameters"].get("cluster_id")
    name = event["queryStringParameters"].get("new_name")

    sdk = yandexcloud.SDK() #(token=token)
    subnets = []
    for subnet_id in event["multiValueQueryStringParameters"].get("subnet_id"):
        subnets.append(common.get_subnet(sdk, subnet_id))

    data_get_cluster = None
    for cluster_type, grpc in _cluster_types.items():
        try:
            data_get_cluster = common.get_cluster(sdk, grpc, cluster_id)
        except RpcError:
            continue
        else:
            logging.info('Found %s cluster %s', cluster_type, cluster_id)
            break

    if data_get_cluster is None:
        raise Exception("Cluster %s not found" % cluster_id)

    data_get_hosts = common.list_cluster_hosts(sdk, grpc, cluster_id)
    if len(data_get_hosts.hosts) != len(subnets):
        raise Exception("Unsupported: got %d hosts and %d subnets" % (len(data_get_hosts.hosts), len(subnets)))

    data_latest_backup = common.latest_backup(common.list_backups(sdk, grpc, cluster_id))
    common.change_cluster_name(sdk, grpc, cluster_id, name)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'isBase64Encoded': False,
        'body': _restore_func[cluster_type](
                sdk=sdk,
                backup_data=data_latest_backup,
                cluster_data=data_get_cluster,
                cluster_hosts_data=data_get_hosts,
                subnets=subnets,
            )
    }
