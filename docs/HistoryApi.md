# paratranz_client.HistoryApi

All URIs are relative to *https://paratranz.cn/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_file_revisions**](HistoryApi.md#get_file_revisions) | **GET** /projects/{projectId}/files/revisions | 文件历史
[**get_history**](HistoryApi.md#get_history) | **GET** /history | 获取历史记录
[**get_term_history**](HistoryApi.md#get_term_history) | **GET** /projects/{projectId}/terms/{termId}/history | 术语历史


# **get_file_revisions**
> GetFileRevisions200Response get_file_revisions(project_id, page=page, page_size=page_size, file=file, type=type)

文件历史

查看项目所有文件上传、更新及删除历史

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
from paratranz_client.models.get_file_revisions200_response import GetFileRevisions200Response
from paratranz_client.rest import ApiException
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
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
async with paratranz_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paratranz_client.HistoryApi(api_client)
    project_id = 56 # int | 项目ID
    page = 1 # int | 页码 (optional) (default to 1)
    page_size = 50 # int | 每页数量 (optional) (default to 50)
    file = 3.4 # float | 指定文件获取历史 (optional)
    type = 'type_example' # str | 指定类型获取历史，同revision中的type定义 (optional)

    try:
        # 文件历史
        api_response = await api_instance.get_file_revisions(project_id, page=page, page_size=page_size, file=file, type=type)
        print("The response of HistoryApi->get_file_revisions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HistoryApi->get_file_revisions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **page** | **int**| 页码 | [optional] [default to 1]
 **page_size** | **int**| 每页数量 | [optional] [default to 50]
 **file** | **float**| 指定文件获取历史 | [optional] 
 **type** | **str**| 指定类型获取历史，同revision中的type定义 | [optional] 

### Return type

[**GetFileRevisions200Response**](GetFileRevisions200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 返回文件历史列表 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_history**
> GetHistory200Response get_history(page=page, page_size=page_size, project=project, uid=uid, tid=tid, type=type)

获取历史记录

获取项目或用户的历史记录，project、uid 与 tid 必须有一个存在，否则会返回 400

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
from paratranz_client.models.get_history200_response import GetHistory200Response
from paratranz_client.rest import ApiException
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
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
async with paratranz_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paratranz_client.HistoryApi(api_client)
    page = 1 # int | 页码 (optional) (default to 1)
    page_size = 50 # int | 每页数量 (optional) (default to 50)
    project = 56 # int | 项目ID (optional)
    uid = 56 # int | 用户ID (optional)
    tid = 56 # int | 词条ID，当 type 为 text 时指定，用于获取某一词条的全部历史记录，**指定后分页失效**  (optional)
    type = 'type_example' # str | 历史记录类型 - `text` 词条历史  - `import` 导入历史，同 project 一起使用  - `comment` 评论记录，同 project 或 uid 一起使用  (optional)

    try:
        # 获取历史记录
        api_response = await api_instance.get_history(page=page, page_size=page_size, project=project, uid=uid, tid=tid, type=type)
        print("The response of HistoryApi->get_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HistoryApi->get_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| 页码 | [optional] [default to 1]
 **page_size** | **int**| 每页数量 | [optional] [default to 50]
 **project** | **int**| 项目ID | [optional] 
 **uid** | **int**| 用户ID | [optional] 
 **tid** | **int**| 词条ID，当 type 为 text 时指定，用于获取某一词条的全部历史记录，**指定后分页失效**  | [optional] 
 **type** | **str**| 历史记录类型 - &#x60;text&#x60; 词条历史  - &#x60;import&#x60; 导入历史，同 project 一起使用  - &#x60;comment&#x60; 评论记录，同 project 或 uid 一起使用  | [optional] 

### Return type

[**GetHistory200Response**](GetHistory200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 返回词条历史列表 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_term_history**
> GetTermHistory200Response get_term_history(project_id, term_id)

术语历史

通过ID获取项目术语修改历史记录

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
from paratranz_client.models.get_term_history200_response import GetTermHistory200Response
from paratranz_client.rest import ApiException
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
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
async with paratranz_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paratranz_client.HistoryApi(api_client)
    project_id = 56 # int | 项目ID
    term_id = 56 # int | 术语ID

    try:
        # 术语历史
        api_response = await api_instance.get_term_history(project_id, term_id)
        print("The response of HistoryApi->get_term_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HistoryApi->get_term_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **term_id** | **int**| 术语ID | 

### Return type

[**GetTermHistory200Response**](GetTermHistory200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 术语列表 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

