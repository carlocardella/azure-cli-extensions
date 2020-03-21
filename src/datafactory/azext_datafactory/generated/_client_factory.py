# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def cf_datafactory(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.datafactory import DataFactoryManagementClient
    return get_mgmt_service_client(cli_ctx, DataFactoryManagementClient)


def cf_factory(cli_ctx, *_):
    return cf_datafactory(cli_ctx).factory


def cf_exposure_control(cli_ctx, *_):
    return cf_datafactory(cli_ctx).exposure_control


def cf_integration_runtime(cli_ctx, *_):
    return cf_datafactory(cli_ctx).integration_runtime


def cf_integration_runtime_object_metadata(cli_ctx, *_):
    return cf_datafactory(cli_ctx).integration_runtime_object_metadata


def cf_integration_runtime_node(cli_ctx, *_):
    return cf_datafactory(cli_ctx).integration_runtime_node


def cf_linked_service(cli_ctx, *_):
    return cf_datafactory(cli_ctx).linked_service


def cf_dataset(cli_ctx, *_):
    return cf_datafactory(cli_ctx).dataset


def cf_pipeline(cli_ctx, *_):
    return cf_datafactory(cli_ctx).pipeline


def cf_pipeline_run(cli_ctx, *_):
    return cf_datafactory(cli_ctx).pipeline_run


def cf_activity_run(cli_ctx, *_):
    return cf_datafactory(cli_ctx).activity_run


def cf_trigger(cli_ctx, *_):
    return cf_datafactory(cli_ctx).trigger


def cf_trigger_run(cli_ctx, *_):
    return cf_datafactory(cli_ctx).trigger_run


def cf_data_flow(cli_ctx, *_):
    return cf_datafactory(cli_ctx).data_flow


def cf_data_flow_debug_session(cli_ctx, *_):
    return cf_datafactory(cli_ctx).data_flow_debug_session
