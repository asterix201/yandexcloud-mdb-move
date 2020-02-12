import logging

import yandex.cloud.mdb.mongodb.v1.cluster_service_pb2 as cluster_service
import yandex.cloud.mdb.mongodb.v1.cluster_service_pb2_grpc as cluster_service_grpc

def restore_cluster(sdk, backup_data, cluster_data, cluster_hosts_data, subnets):
    logging.info('Restoring cluster from backup %s', backup_data.id)

    if cluster_data.config.version == "4.2":
        config_spec = cluster_service.ConfigSpec(
            access=cluster_data.config.access,
            backup_window_start=cluster_data.config.backup_window_start,
            feature_compatibility_version=cluster_data.config.feature_compatibility_version,
            mongodb_spec_4_2=cluster_service.MongodbSpec4_2(
                mongod=cluster_service.MongodbSpec4_2.Mongod(
                    config=cluster_data.config.mongodb_4_2.mongod.config.effective_config,
                    resources=cluster_data.config.mongodb_4_2.mongod.resources,
                ),
                mongocfg=cluster_service.MongodbSpec4_2.MongoCfg(
                    config=cluster_data.config.mongodb_4_2.mongocfg.config.effective_config,
                    resources=cluster_data.config.mongodb_4_2.mongocfg.resources,
                ),
                mongos=cluster_service.MongodbSpec4_2.Mongos(
                    config=cluster_data.config.mongodb_4_2.mongos.config.effective_config,
                    resources=cluster_data.config.mongodb_4_2.mongos.resources,
                )
            ),
            version=cluster_data.config.version,
        )
    elif cluster_data.config.version == "4.0":
        config_spec = cluster_service.ConfigSpec(
            access=cluster_data.config.access,
            backup_window_start=cluster_data.config.backup_window_start,
            feature_compatibility_version=cluster_data.config.feature_compatibility_version,
            mongodb_spec_4_0=cluster_service.MongodbSpec4_0(
                mongod=cluster_service.MongodbSpec4_0.Mongod(
                    config=cluster_data.config.mongodb_4_0.mongod.config.effective_config,
                    resources=cluster_data.config.mongodb_4_0.mongod.resources,
                ),
                mongocfg=cluster_service.MongodbSpec4_0.MongoCfg(
                    config=cluster_data.config.mongodb_4_0.mongocfg.config.effective_config,
                    resources=cluster_data.config.mongodb_4_0.mongocfg.resources,
                ),
                mongos=cluster_service.MongodbSpec4_0.Mongos(
                    config=cluster_data.config.mongodb_4_0.mongos.config.effective_config,
                    resources=cluster_data.config.mongodb_4_0.mongos.resources,
                )
            ),
            version=cluster_data.config.version,
        )
    elif cluster_data.config.version == "3.6":
        config_spec = cluster_service.ConfigSpec(
            access=cluster_data.config.access,
            backup_window_start=cluster_data.config.backup_window_start,
            feature_compatibility_version=cluster_data.config.feature_compatibility_version,
            mongodb_spec_3_6=cluster_service.MongodbSpec3_6(
                mongod=cluster_service.MongodbSpec3_6.Mongod(
                    config=cluster_data.config.mongodb_3_6.mongod.config.effective_config,
                    resources=cluster_data.config.mongodb_3_6.mongod.resources,
                ),
                mongocfg=cluster_service.MongodbSpec3_6.MongoCfg(
                    config=cluster_data.config.mongodb_3_6.mongocfg.config.effective_config,
                    resources=cluster_data.config.mongodb_3_6.mongocfg.resources,
                ),
                mongos=cluster_service.MongodbSpec3_6.Mongos(
                    config=cluster_data.config.mongodb_3_6.mongos.config.effective_config,
                    resources=cluster_data.config.mongodb_3_6.mongos.resources,
                )
            ),
            version=cluster_data.config.version,
        )

    host_specs = [
        cluster_service.HostSpec(
            assign_public_ip=host.assign_public_ip,
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
    )

    operation = sdk.client(cluster_service_grpc.ClusterServiceStub).Restore(request)
    return operation.id
    # return sdk.wait_operation_and_get_result(
    #     operation,
    #     meta_type=cluster_service.RestoreClusterMetadata,
    # )
