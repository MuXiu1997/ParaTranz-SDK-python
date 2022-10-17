<a name="__pageTop"></a>
# paratranz_client.apis.tags.string_api.StringApi

All URIs are relative to *https://paratranz.cn/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_string**](#create_string) | **post** /projects/{projectId}/strings | 创建词条
[**delete_string**](#delete_string) | **delete** /projects/{projectId}/strings/{stringId} | 删除词条
[**get_string**](#get_string) | **get** /projects/{projectId}/strings/{stringId} | 获取词条
[**get_strings**](#get_strings) | **get** /projects/{projectId}/strings | 词条列表
[**save_string**](#save_string) | **put** /projects/{projectId}/strings/{stringId} | 更新词条

# **create_string**
<a name="create_string"></a>
> String create_string(project_idstring)

创建词条

创建词条

### Example

* Api Key Authentication (Token):
```python
import paratranz_client
from paratranz_client.apis.tags import string_api
from pprint import pprint
# Defining the host is optional and defaults to https://paratranz.cn/api
# See configuration.py for a list of all supported configuration parameters.
configuration = paratranz_client.Configuration(
    host = "https://paratranz.cn/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'
# Enter a context with an instance of the API client
with paratranz_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = string_api.StringApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': 1,
    }
    query_params = {
    }
    body = String(
        id=1,
        created_at="2021-01-11T03:19:52.818Z",
        updated_at="2021-01-11T03:19:52.818Z",
        key="key_example",
        original="original_example",
        translation="translation_example",
        file=1,
        stage=Stage(0),
        project=1,
        uid=1,
        context="context_example",
        words=1,
    )
    try:
        # 创建词条
        api_response = api_instance.create_string(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except paratranz_client.ApiException as e:
        print("Exception when calling StringApi->create_string: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectId': 1,
    }
    query_params = {
        'page': 1,
        'pageSize': 50,
    }
    body = String(
        id=1,
        created_at="2021-01-11T03:19:52.818Z",
        updated_at="2021-01-11T03:19:52.818Z",
        key="key_example",
        original="original_example",
        translation="translation_example",
        file=1,
        stage=Stage(0),
        project=1,
        uid=1,
        context="context_example",
        words=1,
    )
    try:
        # 创建词条
        api_response = api_instance.create_string(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except paratranz_client.ApiException as e:
        print("Exception when calling StringApi->create_string: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**String**](../../models/String.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page | PageSchema | | optional
pageSize | PageSizeSchema | | optional


# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 50

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectId | ProjectIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_string.ApiResponseFor200) | 返回词条信息

#### create_string.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**String**](../../models/String.md) |  | 


### Authorization

[Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_string**
<a name="delete_string"></a>
> delete_string(project_idstring_id)

删除词条

通过ID删除词条，仅管理员可用

### Example

* Api Key Authentication (Token):
```python
import paratranz_client
from paratranz_client.apis.tags import string_api
from pprint import pprint
# Defining the host is optional and defaults to https://paratranz.cn/api
# See configuration.py for a list of all supported configuration parameters.
configuration = paratranz_client.Configuration(
    host = "https://paratranz.cn/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'
# Enter a context with an instance of the API client
with paratranz_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = string_api.StringApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': 1,
        'stringId': 1,
    }
    try:
        # 删除词条
        api_response = api_instance.delete_string(
            path_params=path_params,
        )
    except paratranz_client.ApiException as e:
        print("Exception when calling StringApi->delete_string: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectId | ProjectIdSchema | | 
stringId | StringIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StringIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_string.ApiResponseFor200) | 删除成功

#### delete_string.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_string**
<a name="get_string"></a>
> String get_string(project_idstring_id)

获取词条

通过ID获取词条信息

### Example

* Api Key Authentication (Token):
```python
import paratranz_client
from paratranz_client.apis.tags import string_api
from pprint import pprint
# Defining the host is optional and defaults to https://paratranz.cn/api
# See configuration.py for a list of all supported configuration parameters.
configuration = paratranz_client.Configuration(
    host = "https://paratranz.cn/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'
# Enter a context with an instance of the API client
with paratranz_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = string_api.StringApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': 1,
        'stringId': 1,
    }
    try:
        # 获取词条
        api_response = api_instance.get_string(
            path_params=path_params,
        )
        pprint(api_response)
    except paratranz_client.ApiException as e:
        print("Exception when calling StringApi->get_string: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectId | ProjectIdSchema | | 
stringId | StringIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StringIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_string.ApiResponseFor200) | 返回词条信息

#### get_string.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**String**](../../models/String.md) |  | 


### Authorization

[Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_strings**
<a name="get_strings"></a>
> bool, date, datetime, dict, float, int, list, str, none_type get_strings(project_id)

词条列表

获取项目词条

### Example

* Api Key Authentication (Token):
```python
import paratranz_client
from paratranz_client.apis.tags import string_api
from pprint import pprint
# Defining the host is optional and defaults to https://paratranz.cn/api
# See configuration.py for a list of all supported configuration parameters.
configuration = paratranz_client.Configuration(
    host = "https://paratranz.cn/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'
# Enter a context with an instance of the API client
with paratranz_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = string_api.StringApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': 1,
    }
    query_params = {
    }
    try:
        # 词条列表
        api_response = api_instance.get_strings(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except paratranz_client.ApiException as e:
        print("Exception when calling StringApi->get_strings: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectId': 1,
    }
    query_params = {
        'page': 1,
        'pageSize': 50,
        'file': 1,
        'stage': 1,
    }
    try:
        # 词条列表
        api_response = api_instance.get_strings(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except paratranz_client.ApiException as e:
        print("Exception when calling StringApi->get_strings: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page | PageSchema | | optional
pageSize | PageSizeSchema | | optional
file | FileSchema | | optional
stage | StageSchema | | optional


# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 50

# FileSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectId | ProjectIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_strings.ApiResponseFor200) | 返回词条列表

#### get_strings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**page** | decimal.Decimal, int, float,  | decimal.Decimal,  | 页码 | [optional] if omitted the server will use the default value of 1
**pageSize** | decimal.Decimal, int, float,  | decimal.Decimal,  | 每页数量 | [optional] if omitted the server will use the default value of 50
**rowCount** | decimal.Decimal, int, float,  | decimal.Decimal,  | 总条数 | [optional] if omitted the server will use the default value of 0
**pageCount** | decimal.Decimal, int, float,  | decimal.Decimal,  | 总页数，通过总条数与每页数量计算得出 | [optional] if omitted the server will use the default value of 0
**[results](#results)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# results

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**String**]({{complexTypePrefix}}String.md) | [**String**]({{complexTypePrefix}}String.md) | [**String**]({{complexTypePrefix}}String.md) |  | 

### Authorization

[Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **save_string**
<a name="save_string"></a>
> String save_string(project_idstring_idstring)

更新词条

通过ID更新词条信息

### Example

* Api Key Authentication (Token):
```python
import paratranz_client
from paratranz_client.apis.tags import string_api
from pprint import pprint
# Defining the host is optional and defaults to https://paratranz.cn/api
# See configuration.py for a list of all supported configuration parameters.
configuration = paratranz_client.Configuration(
    host = "https://paratranz.cn/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'
# Enter a context with an instance of the API client
with paratranz_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = string_api.StringApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': 1,
        'stringId': 1,
    }
    body = String(
        id=1,
        created_at="2021-01-11T03:19:52.818Z",
        updated_at="2021-01-11T03:19:52.818Z",
        key="key_example",
        original="original_example",
        translation="translation_example",
        file=1,
        stage=Stage(0),
        project=1,
        uid=1,
        context="context_example",
        words=1,
    )
    try:
        # 更新词条
        api_response = api_instance.save_string(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except paratranz_client.ApiException as e:
        print("Exception when calling StringApi->save_string: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**String**](../../models/String.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectId | ProjectIdSchema | | 
stringId | StringIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StringIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#save_string.ApiResponseFor200) | 返回词条信息

#### save_string.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**String**](../../models/String.md) |  | 


### Authorization

[Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

