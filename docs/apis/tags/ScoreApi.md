<a name="__pageTop"></a>
# paratranz_client.apis.tags.score_api.ScoreApi

All URIs are relative to *https://paratranz.cn/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_scores**](#get_scores) | **get** /projects/{projectId}/scores | 成员贡献

# **get_scores**
<a name="get_scores"></a>
> bool, date, datetime, dict, float, int, list, str, none_type get_scores(project_id)

成员贡献

查看项目所有的贡献

### Example

* Api Key Authentication (Token):
```python
import paratranz_client
from paratranz_client.apis.tags import score_api
from paratranz_client.model.score import Score
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': 1,
    }
    query_params = {
    }
    try:
        # 成员贡献
        api_response = api_instance.get_scores(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except paratranz_client.ApiException as e:
        print("Exception when calling ScoreApi->get_scores: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectId': 1,
    }
    query_params = {
        'page': 1,
        'pageSize': 50,
        'uid': 1,
        'operation': "translate",
        'start': "1970-01-01T00:00:00.00Z",
        'end': "1970-01-01T00:00:00.00Z",
    }
    try:
        # 成员贡献
        api_response = api_instance.get_scores(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except paratranz_client.ApiException as e:
        print("Exception when calling ScoreApi->get_scores: %s\n" % e)
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
uid | UidSchema | | optional
operation | OperationSchema | | optional
start | StartSchema | | optional
end | EndSchema | | optional


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

# UidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# OperationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["translate", "edit", "review", ] 

# StartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EndSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

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
200 | [ApiResponseFor200](#get_scores.ApiResponseFor200) | 返回贡献列表

#### get_scores.ApiResponseFor200
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
[**Score**]({{complexTypePrefix}}Score.md) | [**Score**]({{complexTypePrefix}}Score.md) | [**Score**]({{complexTypePrefix}}Score.md) |  | 

### Authorization

[Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

