# coding: utf-8

"""
    Speech Services API v2.0

    Speech Services API v2.0.  # noqa: E501

    OpenAPI spec version: v2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class CustomSpeechAccuracyTestsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_accuracy_test(self, test_definition, **kwargs):  # noqa: E501
        """Creates a new accuracy test.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_accuracy_test(test_definition, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TestDefinition test_definition: The details of the new accuracy test. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_accuracy_test_with_http_info(test_definition, **kwargs)  # noqa: E501
        else:
            (data) = self.create_accuracy_test_with_http_info(test_definition, **kwargs)  # noqa: E501
            return data

    def create_accuracy_test_with_http_info(self, test_definition, **kwargs):  # noqa: E501
        """Creates a new accuracy test.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_accuracy_test_with_http_info(test_definition, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TestDefinition test_definition: The details of the new accuracy test. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['test_definition']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_accuracy_test" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'test_definition' is set
        if ('test_definition' not in params or
                params['test_definition'] is None):
            raise ValueError("Missing the required parameter `test_definition` when calling `create_accuracy_test`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'test_definition' in params:
            body_params = params['test_definition']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['subscription_key', 'token']  # noqa: E501

        return self.api_client.call_api(
            '/api/speechtotext/v2.0/accuracytests', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_accuracy_test(self, id, **kwargs):  # noqa: E501
        """Deletes the accuracy test identified by the given ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_accuracy_test(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the accuracy test. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_accuracy_test_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_accuracy_test_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_accuracy_test_with_http_info(self, id, **kwargs):  # noqa: E501
        """Deletes the accuracy test identified by the given ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_accuracy_test_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the accuracy test. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_accuracy_test" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_accuracy_test`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['subscription_key', 'token']  # noqa: E501

        return self.api_client.call_api(
            '/api/speechtotext/v2.0/accuracytests/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_accuracy_test(self, id, **kwargs):  # noqa: E501
        """Gets the accuracy test identified by the given ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_accuracy_test(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the accuracy test. (required)
        :return: Test
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_accuracy_test_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_accuracy_test_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_accuracy_test_with_http_info(self, id, **kwargs):  # noqa: E501
        """Gets the accuracy test identified by the given ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_accuracy_test_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the accuracy test. (required)
        :return: Test
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_accuracy_test" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_accuracy_test`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['subscription_key', 'token']  # noqa: E501

        return self.api_client.call_api(
            '/api/speechtotext/v2.0/accuracytests/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Test',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_accuracy_tests(self, **kwargs):  # noqa: E501
        """Gets the list of accuracy tests for the authenticated subscription.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_accuracy_tests(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Test]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_accuracy_tests_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_accuracy_tests_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_accuracy_tests_with_http_info(self, **kwargs):  # noqa: E501
        """Gets the list of accuracy tests for the authenticated subscription.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_accuracy_tests_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Test]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_accuracy_tests" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['subscription_key', 'token']  # noqa: E501

        return self.api_client.call_api(
            '/api/speechtotext/v2.0/accuracytests', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Test]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_accuracy_test(self, id, test_update, **kwargs):  # noqa: E501
        """Updates the mutable details of the test identified by its id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_accuracy_test(id, test_update, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the accuracy test. (required)
        :param TestUpdate test_update: The object containing the updated fields of the test. (required)
        :return: Test
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_accuracy_test_with_http_info(id, test_update, **kwargs)  # noqa: E501
        else:
            (data) = self.update_accuracy_test_with_http_info(id, test_update, **kwargs)  # noqa: E501
            return data

    def update_accuracy_test_with_http_info(self, id, test_update, **kwargs):  # noqa: E501
        """Updates the mutable details of the test identified by its id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_accuracy_test_with_http_info(id, test_update, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the accuracy test. (required)
        :param TestUpdate test_update: The object containing the updated fields of the test. (required)
        :return: Test
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'test_update']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_accuracy_test" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_accuracy_test`")  # noqa: E501
        # verify the required parameter 'test_update' is set
        if ('test_update' not in params or
                params['test_update'] is None):
            raise ValueError("Missing the required parameter `test_update` when calling `update_accuracy_test`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'test_update' in params:
            body_params = params['test_update']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['subscription_key', 'token']  # noqa: E501

        return self.api_client.call_api(
            '/api/speechtotext/v2.0/accuracytests/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Test',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)