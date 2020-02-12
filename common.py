import logging
import uuid

from google.protobuf.field_mask_pb2 import FieldMask

import yandex.cloud.vpc.v1.subnet_service_pb2 as subnet_service
import yandex.cloud.vpc.v1.subnet_service_pb2_grpc as subnet_service_grpc

def get_subnet(sdk, subnet_id):
    request = subnet_service.GetSubnetRequest(
        subnet_id=subnet_id,
    )
    return sdk.client(subnet_service_grpc.SubnetServiceStub).Get(request)

def change_cluster_name(sdk, grpc, cluster_id, name=None):
    logging.info('Updating cluster {}'.format(cluster_id))
    mask = FieldMask(paths=['name'])
    request = grpc.cluster_service.UpdateClusterRequest(
        cluster_id=cluster_id,
        update_mask=mask,
        name=name or uuid.uuid4().hex
    )

    operation = sdk.client(grpc.cluster_service_grpc.ClusterServiceStub).Update(request)
    return sdk.wait_operation_and_get_result(
        operation,
        response_type=grpc.cluster_pb.Cluster,
        meta_type=grpc.cluster_service.UpdateClusterMetadata,
    )


def list_backups(sdk, grpc, cluster_id):
    logging.info('Getting backups for cluster {}'.format(cluster_id))
    request = grpc.cluster_service.ListClusterBackupsRequest(
        cluster_id=cluster_id,
        page_size=1000
    )
    return sdk.client(grpc.cluster_service_grpc.ClusterServiceStub).ListBackups(request)


def latest_backup(backup_response):
    if len(backup_response.backups) > 0:
        return backup_response.backups[0]
    else:
        raise Exception("No actual backups found")


def get_cluster(sdk, grpc, cluster_id):
    request = grpc.cluster_service.GetClusterRequest(cluster_id=cluster_id)
    return sdk.client(grpc.cluster_service_grpc.ClusterServiceStub).Get(request)


def list_cluster_hosts(sdk, grpc, cluster_id):
    request = grpc.cluster_service.ListClusterHostsRequest(cluster_id=cluster_id)
    return sdk.client(grpc.cluster_service_grpc.ClusterServiceStub).ListHosts(request)
