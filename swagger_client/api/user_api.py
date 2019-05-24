# coding: utf-8

"""
    predictor_scoring

    Credit Score Predictor  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class UserApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def login(self, login_request, **kwargs):  # noqa: E501
        """Logs the user in  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.login(login_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LoginRequest login_request: (required)
        :return: AccessTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.login_with_http_info(login_request, **kwargs)  # noqa: E501
        else:
            (data) = self.login_with_http_info(login_request, **kwargs)  # noqa: E501
            return data

    def login_with_http_info(self, login_request, **kwargs):  # noqa: E501
        """Logs the user in  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.login_with_http_info(login_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LoginRequest login_request: (required)
        :return: AccessTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method login" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'login_request' is set
        if ('login_request' not in params or
                params['login_request'] is None):
            raise ValueError("Missing the required parameter `login_request` when calling `login`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'login_request' in params:
            body_params = params['login_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/login', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessTokenResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def renew_token(self, renew_token_request, **kwargs):  # noqa: E501
        """The user renews access token and refresh token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.renew_token(renew_token_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RenewTokenRequest renew_token_request: (required)
        :return: AccessTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.renew_token_with_http_info(renew_token_request, **kwargs)  # noqa: E501
        else:
            (data) = self.renew_token_with_http_info(renew_token_request, **kwargs)  # noqa: E501
            return data

    def renew_token_with_http_info(self, renew_token_request, **kwargs):  # noqa: E501
        """The user renews access token and refresh token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.renew_token_with_http_info(renew_token_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RenewTokenRequest renew_token_request: (required)
        :return: AccessTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['renew_token_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method renew_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'renew_token_request' is set
        if ('renew_token_request' not in params or
                params['renew_token_request'] is None):
            raise ValueError("Missing the required parameter `renew_token_request` when calling `renew_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'renew_token_request' in params:
            body_params = params['renew_token_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/login/refreshToken', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessTokenResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def revoke_refresh_token(self, refresh_token, **kwargs):  # noqa: E501
        """The user revokes a refresh token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revoke_refresh_token(refresh_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str refresh_token: The refresh token to be revoked (required)
        :return: AccessTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.revoke_refresh_token_with_http_info(refresh_token, **kwargs)  # noqa: E501
        else:
            (data) = self.revoke_refresh_token_with_http_info(refresh_token, **kwargs)  # noqa: E501
            return data

    def revoke_refresh_token_with_http_info(self, refresh_token, **kwargs):  # noqa: E501
        """The user revokes a refresh token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revoke_refresh_token_with_http_info(refresh_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str refresh_token: The refresh token to be revoked (required)
        :return: AccessTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['refresh_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method revoke_refresh_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'refresh_token' is set
        if ('refresh_token' not in params or
                params['refresh_token'] is None):
            raise ValueError("Missing the required parameter `refresh_token` when calling `revoke_refresh_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'refresh_token' in params:
            query_params.append(('refreshToken', params['refresh_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/login/refreshToken', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessTokenResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
