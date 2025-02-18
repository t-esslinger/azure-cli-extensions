# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class CatalogItemsOperations:
    """CatalogItemOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~dev_center_dataplane_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_by_project(
        self,
        top: Optional[int] = None,
        **kwargs
    ) -> AsyncIterable["models.CatalogItemListResult"]:
        """Lists latest version of all catalog items available for a project.

        :param top: The maximum number of resources to return from the operation. Example: 'top=10'.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CatalogItemListResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~dev_center_dataplane_client.models.CatalogItemListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CatalogItemListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2022-11-11-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_by_project.metadata['url']  # type: ignore
                path_format_arguments = {
                    'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                    'projectName': self._serialize.url("self._config.project_name", self._config.project_name, 'str', max_length=63, min_length=3, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9-_.]{2,62}$'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
                if top is not None:
                    query_parameters['top'] = self._serialize.query("top", top, 'int')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                    'projectName': self._serialize.url("self._config.project_name", self._config.project_name, 'str', max_length=63, min_length=3, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9-_.]{2,62}$'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('CatalogItemListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_project.metadata = {'url': '/projects/{projectName}/catalogItems'}  # type: ignore

    async def get(
        self,
        catalog_item_id: str,
        **kwargs
    ) -> "models.CatalogItem":
        """Get a catalog item from a project.

        :param catalog_item_id: The unique id of the catalog item.
        :type catalog_item_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CatalogItem, or the result of cls(response)
        :rtype: ~dev_center_dataplane_client.models.CatalogItem
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CatalogItem"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2022-11-11-preview"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'projectName': self._serialize.url("self._config.project_name", self._config.project_name, 'str', max_length=63, min_length=3, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9-_.]{2,62}$'),
            'catalogItemId': self._serialize.url("catalog_item_id", catalog_item_id, 'str', max_length=216, min_length=3, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9-_.:]{2,216}$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('CatalogItem', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/projects/{projectName}/catalogItems/{catalogItemId}'}  # type: ignore
