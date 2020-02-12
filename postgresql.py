import logging

import yandex.cloud.mdb.postgresql.v1.cluster_service_pb2 as cluster_service
import yandex.cloud.mdb.postgresql.v1.cluster_service_pb2_grpc as cluster_service_grpc

def restore_cluster(sdk, backup_data, cluster_data, cluster_hosts_data, subnets):
    logging.info('Restoring cluster from backup %s', backup_data.id)

    if cluster_data.config.version == "12":
        config_spec = cluster_service.ConfigSpec(
            access=cluster_data.config.access,
            autofailover=cluster_data.config.autofailover,
            backup_window_start=cluster_data.config.backup_window_start,
            pooler_config=cluster_data.config.pooler_config,
            version=cluster_data.config.version,
            postgresql_config_12=cluster_data.config.postgresql_config_12.effective_config,
            resources=cluster_data.config.resources,
        )
    elif cluster_data.config.version == "11":
        config_spec = cluster_service.ConfigSpec(
            access=cluster_data.config.access,
            autofailover=cluster_data.config.autofailover,
            backup_window_start=cluster_data.config.backup_window_start,
            pooler_config=cluster_data.config.pooler_config,
            version=cluster_data.config.version,
            postgresql_config_11=cluster_data.config.postgresql_config_11.effective_config,
            resources=cluster_data.config.resources,
        )
    elif cluster_data.config.version == "10":
        config_spec = cluster_service.ConfigSpec(
            access=cluster_data.config.access,
            autofailover=cluster_data.config.autofailover,
            backup_window_start=cluster_data.config.backup_window_start,
            pooler_config=cluster_data.config.pooler_config,
            version=cluster_data.config.version,
            postgresql_config_10=cluster_data.config.postgresql_config_10.effective_config,
            resources=cluster_data.config.resources,
        )
    elif cluster_data.config.version == "10_1C":
        config_spec = cluster_service.ConfigSpec(
            access=cluster_data.config.access,
            autofailover=cluster_data.config.autofailover,
            backup_window_start=cluster_data.config.backup_window_start,
            pooler_config=cluster_data.config.pooler_config,
            version=cluster_data.config.version,
            postgresql_config_10_1c=cluster_data.config.postgresql_config_10_1c.effective_config,
            resources=cluster_data.config.resources,
        )
    elif cluster_data.config.version == "9_6":
        config_spec = cluster_service.ConfigSpec(
            access=cluster_data.config.access,
            autofailover=cluster_data.config.autofailover,
            backup_window_start=cluster_data.config.backup_window_start,
            pooler_config=cluster_data.config.pooler_config,
            version=cluster_data.config.version,
            postgresql_config_9_6=cluster_data.config.postgresql_config_9_6.effective_config,
            resources=cluster_data.config.resources,
        )

    host_specs = [
        cluster_service.HostSpec(
            assign_public_ip=host.assign_public_ip,
            config_spec=cluster_service.ConfigHostSpec(
                postgresql_config_10=host.config.postgresql_config_10,
                postgresql_config_10_1c=host.config.postgresql_config_10_1c,
                postgresql_config_11=host.config.postgresql_config_11,
                postgresql_config_12=host.config.postgresql_config_12,
                postgresql_config_9_6=host.config.postgresql_config_9_6,
            ),
            priority=host.priority,
            replication_source=host.replication_source,
            subnet_id=subnets[i].id,
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
        time=backup_data.created_at,
    )

    operation = sdk.client(cluster_service_grpc.ClusterServiceStub).Restore(request)
    return operation.id
    # return sdk.wait_operation_and_get_result(
    #     operation,
    #     meta_type=cluster_service.RestoreClusterMetadata,
    # )
