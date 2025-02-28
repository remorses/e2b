# coding: utf-8

"""
    Devbook

    Devbook API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated
from typing import overload, Optional, Union, Awaitable

from pydantic import StrictStr

from typing import List, Optional

from e2b.api.v1.client.models.new_session import NewSession
from e2b.api.v1.client.models.session import Session
from e2b.api.v1.client.models.sessions_get200_response_inner import (
    SessionsGet200ResponseInner,
)

from e2b.api.v1.client.api_client import ApiClient
from e2b.api.v1.client.api_response import ApiResponse
from e2b.api.v1.client.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class SessionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @overload
    async def sessions_get(
        self, api_key: StrictStr, **kwargs
    ) -> List[SessionsGet200ResponseInner]:  # noqa: E501
        ...

    @overload
    def sessions_get(
        self, api_key: StrictStr, async_req: Optional[bool] = True, **kwargs
    ) -> List[SessionsGet200ResponseInner]:  # noqa: E501
        ...

    @validate_arguments
    def sessions_get(
        self, api_key: StrictStr, async_req: Optional[bool] = None, **kwargs
    ) -> Union[
        List[SessionsGet200ResponseInner], Awaitable[List[SessionsGet200ResponseInner]]
    ]:  # noqa: E501
        """sessions_get  # noqa: E501

        List all sessions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.sessions_get(api_key, async_req=True)
        >>> result = thread.get()

        :param api_key: (required)
        :type api_key: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[SessionsGet200ResponseInner]
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            raise ValueError(
                "Error! Please call the sessions_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        if async_req is not None:
            kwargs["async_req"] = async_req
        return self.sessions_get_with_http_info(api_key, **kwargs)  # noqa: E501

    @validate_arguments
    def sessions_get_with_http_info(
        self, api_key: StrictStr, **kwargs
    ) -> ApiResponse:  # noqa: E501
        """sessions_get  # noqa: E501

        List all sessions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.sessions_get_with_http_info(api_key, async_req=True)
        >>> result = thread.get()

        :param api_key: (required)
        :type api_key: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[SessionsGet200ResponseInner], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["api_key"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sessions_get" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get("api_key") is not None:  # noqa: E501
            _query_params.append(("api_key", _params["api_key"]))

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            "200": "List[SessionsGet200ResponseInner]",
            "401": "Error",
            "500": "Error",
        }

        return self.api_client.call_api(
            "/sessions",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @overload
    async def sessions_post(
        self, new_session: NewSession, api_key: Optional[StrictStr] = None, **kwargs
    ) -> Session:  # noqa: E501
        ...

    @overload
    def sessions_post(
        self,
        new_session: NewSession,
        api_key: Optional[StrictStr] = None,
        async_req: Optional[bool] = True,
        **kwargs
    ) -> Session:  # noqa: E501
        ...

    @validate_arguments
    def sessions_post(
        self,
        new_session: NewSession,
        api_key: Optional[StrictStr] = None,
        async_req: Optional[bool] = None,
        **kwargs
    ) -> Union[Session, Awaitable[Session]]:  # noqa: E501
        """sessions_post  # noqa: E501

        Create a session on the server  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.sessions_post(new_session, api_key, async_req=True)
        >>> result = thread.get()

        :param new_session: (required)
        :type new_session: NewSession
        :param api_key:
        :type api_key: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Session
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            raise ValueError(
                "Error! Please call the sessions_post_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        if async_req is not None:
            kwargs["async_req"] = async_req
        return self.sessions_post_with_http_info(
            new_session, api_key, **kwargs
        )  # noqa: E501

    @validate_arguments
    def sessions_post_with_http_info(
        self, new_session: NewSession, api_key: Optional[StrictStr] = None, **kwargs
    ) -> ApiResponse:  # noqa: E501
        """sessions_post  # noqa: E501

        Create a session on the server  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.sessions_post_with_http_info(new_session, api_key, async_req=True)
        >>> result = thread.get()

        :param new_session: (required)
        :type new_session: NewSession
        :param api_key:
        :type api_key: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Session, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["new_session", "api_key"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sessions_post" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get("api_key") is not None:  # noqa: E501
            _query_params.append(("api_key", _params["api_key"]))

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params["new_session"] is not None:
            _body_params = _params["new_session"]

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(["application/json"]),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            "201": "Session",
            "401": "Error",
            "400": "Error",
            "500": "Error",
        }

        return self.api_client.call_api(
            "/sessions",
            "POST",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @overload
    async def sessions_session_id_delete(
        self, api_key: StrictStr, session_id: StrictStr, **kwargs
    ) -> None:  # noqa: E501
        ...

    @overload
    def sessions_session_id_delete(
        self,
        api_key: StrictStr,
        session_id: StrictStr,
        async_req: Optional[bool] = True,
        **kwargs
    ) -> None:  # noqa: E501
        ...

    @validate_arguments
    def sessions_session_id_delete(
        self,
        api_key: StrictStr,
        session_id: StrictStr,
        async_req: Optional[bool] = None,
        **kwargs
    ) -> Union[None, Awaitable[None]]:  # noqa: E501
        """sessions_session_id_delete  # noqa: E501

        Delete a session on the server  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.sessions_session_id_delete(api_key, session_id, async_req=True)
        >>> result = thread.get()

        :param api_key: (required)
        :type api_key: str
        :param session_id: (required)
        :type session_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            raise ValueError(
                "Error! Please call the sessions_session_id_delete_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        if async_req is not None:
            kwargs["async_req"] = async_req
        return self.sessions_session_id_delete_with_http_info(
            api_key, session_id, **kwargs
        )  # noqa: E501

    @validate_arguments
    def sessions_session_id_delete_with_http_info(
        self, api_key: StrictStr, session_id: StrictStr, **kwargs
    ) -> ApiResponse:  # noqa: E501
        """sessions_session_id_delete  # noqa: E501

        Delete a session on the server  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.sessions_session_id_delete_with_http_info(api_key, session_id, async_req=True)
        >>> result = thread.get()

        :param api_key: (required)
        :type api_key: str
        :param session_id: (required)
        :type session_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = ["api_key", "session_id"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sessions_session_id_delete" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["session_id"]:
            _path_params["sessionID"] = _params["session_id"]

        # process the query parameters
        _query_params = []
        if _params.get("api_key") is not None:  # noqa: E501
            _query_params.append(("api_key", _params["api_key"]))

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            "/sessions/{sessionID}",
            "DELETE",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @overload
    async def sessions_session_id_refresh_post(
        self, session_id: StrictStr, api_key: Optional[StrictStr] = None, **kwargs
    ) -> None:  # noqa: E501
        ...

    @overload
    def sessions_session_id_refresh_post(
        self,
        session_id: StrictStr,
        api_key: Optional[StrictStr] = None,
        async_req: Optional[bool] = True,
        **kwargs
    ) -> None:  # noqa: E501
        ...

    @validate_arguments
    def sessions_session_id_refresh_post(
        self,
        session_id: StrictStr,
        api_key: Optional[StrictStr] = None,
        async_req: Optional[bool] = None,
        **kwargs
    ) -> Union[None, Awaitable[None]]:  # noqa: E501
        """sessions_session_id_refresh_post  # noqa: E501

        Refresh the session extending its time to live  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.sessions_session_id_refresh_post(session_id, api_key, async_req=True)
        >>> result = thread.get()

        :param session_id: (required)
        :type session_id: str
        :param api_key:
        :type api_key: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            raise ValueError(
                "Error! Please call the sessions_session_id_refresh_post_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        if async_req is not None:
            kwargs["async_req"] = async_req
        return self.sessions_session_id_refresh_post_with_http_info(
            session_id, api_key, **kwargs
        )  # noqa: E501

    @validate_arguments
    def sessions_session_id_refresh_post_with_http_info(
        self, session_id: StrictStr, api_key: Optional[StrictStr] = None, **kwargs
    ) -> ApiResponse:  # noqa: E501
        """sessions_session_id_refresh_post  # noqa: E501

        Refresh the session extending its time to live  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.sessions_session_id_refresh_post_with_http_info(session_id, api_key, async_req=True)
        >>> result = thread.get()

        :param session_id: (required)
        :type session_id: str
        :param api_key:
        :type api_key: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = ["session_id", "api_key"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sessions_session_id_refresh_post" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["session_id"]:
            _path_params["sessionID"] = _params["session_id"]

        # process the query parameters
        _query_params = []
        if _params.get("api_key") is not None:  # noqa: E501
            _query_params.append(("api_key", _params["api_key"]))

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            "/sessions/{sessionID}/refresh",
            "POST",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )
