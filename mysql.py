import logging

import yandex.cloud.mdb.mysql.v1.cluster_service_pb2 as cluster_service
import yandex.cloud.mdb.mysql.v1.cluster_service_pb2_grpc as cluster_service_grpc

def restore_cluster(sdk, backup_data, cluster_data, cluster_hosts_data, network_id, subnet_id):
    logging.info('Restoring cluster from backup %s', backup_data.id)

    if cluster_data.config.version == "8.0":
        config_spec = cluster_service.ConfigSpec(
            access=cluster_data.config.access,
            backup_window_start=cluster_data.config.backup_window_start,
            version=cluster_data.config.version,
            mysql_config_8_0=cluster_data.config.mysql_config_8_0.effective_config,
            resources=cluster_data.config.resources,
        )
    elif cluster_data.config.version == "5.7":
        config_spec = cluster_service.ConfigSpec(
            access=cluster_data.config.access,
            backup_window_start=cluster_data.config.backup_window_start,
            version=cluster_data.config.version,
            mysql_config_5_7=cluster_data.config.mysql_config_5_7.effective_config,
            resources=cluster_data.config.resources,
        )

    host_specs = [
        cluster_service.HostSpec(
            assign_public_ip=host.assign_public_ip,
            subnet_id=subnet_id,
            zone_id=host.zone_id,
        )
        for host in cluster_hosts_data.hosts
    ]

    request = cluster_service.RestoreClusterRequest(
        backup_id=backup_data.id,
        config_spec=config_spec,
        description=cluster_data.description,
        environment=cluster_data.environment,
        folder_id=cluster_data.folder_id,
        host_specs=host_specs,
        labels=cluster_data.labels,
        name=cluster_data.name,
        network_id=network_id,
        time=backup_data.created_at,
    )

    operation = sdk.client(cluster_service_grpc.ClusterServiceStub).Restore(request)
    return operation.id
    # return sdk.wait_operation_and_get_result(
    #     operation,
    #     meta_type=cluster_service.RestoreClusterMetadata,
    # )
