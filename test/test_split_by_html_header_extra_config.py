# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dat_client.models.split_by_html_header_extra_config import SplitByHtmlHeaderExtraConfig

class TestSplitByHtmlHeaderExtraConfig(unittest.TestCase):
    """SplitByHtmlHeaderExtraConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SplitByHtmlHeaderExtraConfig:
        """Test SplitByHtmlHeaderExtraConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SplitByHtmlHeaderExtraConfig`
        """
        model = SplitByHtmlHeaderExtraConfig()
        if include_optional:
            return SplitByHtmlHeaderExtraConfig(
                headers_to_split_on = None
            )
        else:
            return SplitByHtmlHeaderExtraConfig(
        )
        """

    def testSplitByHtmlHeaderExtraConfig(self):
        """Test SplitByHtmlHeaderExtraConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()