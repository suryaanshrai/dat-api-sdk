# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dat_client.models.workspace_user_post_request import WorkspaceUserPostRequest

class TestWorkspaceUserPostRequest(unittest.TestCase):
    """WorkspaceUserPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkspaceUserPostRequest:
        """Test WorkspaceUserPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkspaceUserPostRequest`
        """
        model = WorkspaceUserPostRequest()
        if include_optional:
            return WorkspaceUserPostRequest(
                workspace_id = '',
                user_id = ''
            )
        else:
            return WorkspaceUserPostRequest(
                workspace_id = '',
                user_id = '',
        )
        """

    def testWorkspaceUserPostRequest(self):
        """Test WorkspaceUserPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()