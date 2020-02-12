import logging

import yandex.cloud.mdb.clickhouse.v1.cluster_service_pb2 as cluster_service
import yandex.cloud.mdb.clickhouse.v1.cluster_service_pb2_grpc as cluster_service_grpc

def restore_cluster(sdk, backup_data, cluster_data, cluster_hosts_data, subnets):
    logging.info('Restoring cluster from backup %s', backup_data.id)

    config_spec = cluster_service.ConfigSpec(
        access=cluster_data.config.access,
        backup_window_start=cluster_data.config.backup_window_start,
        clickhouse=cluster_service.ConfigSpec.Clickhouse(
            config=cluster_data.config.clickhouse.config.effective_config,
            resources=cluster_data.config.clickhouse.resources,
        ),
        version=cluster_data.config.version,
        zookeeper=cluster_service.ConfigSpec.Zookeeper(
            resources=cluster_data.config.zookeeper.resources,
        )
    )

    host_specs = [
        cluster_service.HostSpec(
            assign_public_ip=host.assign_public_ip,
            shard_name=host.shard_name,
            subnet_id=subnets[i].id,
            type=host.type,
            zone_id=subnets[i].zone_id,
        )
        for i, host in enumerate(cluster_hosts_data.hosts)
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
        network_id=subnets[0].network_id,
    )

    operation = sdk.client(cluster_service_grpc.ClusterServiceStub).Restore(request)
    return operation.id
    # return sdk.wait_operation_and_get_result(
    #     operation,
    #     meta_type=cluster_service.RestoreClusterMetadata,
    # )
