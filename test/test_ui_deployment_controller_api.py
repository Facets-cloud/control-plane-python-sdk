# coding: utf-8

"""
    Api Documentation

    Api Documentation  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.ui_deployment_controller_api import UiDeploymentControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUiDeploymentControllerApi(unittest.TestCase):
    """UiDeploymentControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.ui_deployment_controller_api.UiDeploymentControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_abort_automation_suite_using_delete1(self):
        """Test case for abort_automation_suite_using_delete1

        abortAutomationSuite  # noqa: E501
        """
        pass

    def test_approve_release_using_post(self):
        """Test case for approve_release_using_post

        approveRelease  # noqa: E501
        """
        pass

    def test_create_deployment_using_post(self):
        """Test case for create_deployment_using_post

        createDeployment  # noqa: E501
        """
        pass

    def test_destroy_cluster_using_delete(self):
        """Test case for destroy_cluster_using_delete

        destroyCluster  # noqa: E501
        """
        pass

    def test_get_cluster_state_using_get(self):
        """Test case for get_cluster_state_using_get

        getClusterState  # noqa: E501
        """
        pass

    def test_get_deployment_logs_using_get(self):
        """Test case for get_deployment_logs_using_get

        getDeploymentLogs  # noqa: E501
        """
        pass

    def test_get_deployment_stats_using_get(self):
        """Test case for get_deployment_stats_using_get

        getDeploymentStats  # noqa: E501
        """
        pass

    def test_get_deployment_using_get(self):
        """Test case for get_deployment_using_get

        getDeployment  # noqa: E501
        """
        pass

    def test_get_deployments_overview_using_get(self):
        """Test case for get_deployments_overview_using_get

        getDeploymentsOverview  # noqa: E501
        """
        pass

    def test_get_deployments_using_get1(self):
        """Test case for get_deployments_using_get1

        getDeployments  # noqa: E501
        """
        pass

    def test_get_latest_release_by_application_using_get(self):
        """Test case for get_latest_release_by_application_using_get

        getLatestReleaseByApplication  # noqa: E501
        """
        pass

    def test_get_latest_release_using_get(self):
        """Test case for get_latest_release_using_get

        getLatestRelease  # noqa: E501
        """
        pass

    def test_get_release_changes_using_get(self):
        """Test case for get_release_changes_using_get

        getReleaseChanges  # noqa: E501
        """
        pass

    def test_launch_cluster_using_put(self):
        """Test case for launch_cluster_using_put

        launchCluster  # noqa: E501
        """
        pass

    def test_reject_release_using_post(self):
        """Test case for reject_release_using_post

        rejectRelease  # noqa: E501
        """
        pass

    def test_release_using_put(self):
        """Test case for release_using_put

        release  # noqa: E501
        """
        pass

    def test_release_v2_using_put(self):
        """Test case for release_v2_using_put

        releaseV2  # noqa: E501
        """
        pass

    def test_run_hotfix_deployment_recipe_using_post(self):
        """Test case for run_hotfix_deployment_recipe_using_post

        runHotfixDeploymentRecipe  # noqa: E501
        """
        pass

    def test_search_deployments_using_get(self):
        """Test case for search_deployments_using_get

        searchDeployments  # noqa: E501
        """
        pass

    def test_sign_off_deployment_using_put(self):
        """Test case for sign_off_deployment_using_put

        signOffDeployment  # noqa: E501
        """
        pass

    def test_simulate_using_get(self):
        """Test case for simulate_using_get

        simulate  # noqa: E501
        """
        pass

    def test_state_unlock_using_put(self):
        """Test case for state_unlock_using_put

        stateUnlock  # noqa: E501
        """
        pass

    def test_stream_deployment_logs_using_get(self):
        """Test case for stream_deployment_logs_using_get

        streamDeploymentLogs  # noqa: E501
        """
        pass

    def test_trigger_maintenance_release_using_post(self):
        """Test case for trigger_maintenance_release_using_post

        triggerMaintenanceRelease  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
