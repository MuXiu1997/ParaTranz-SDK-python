# paratranz_client.ScoresApi

All URIs are relative to *https://paratranz.cn/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_scores**](ScoresApi.md#get_scores) | **GET** /projects/{projectId}/scores | 成员贡献


# **get_scores**
> GetScores200Response get_scores(project_id, page=page, page_size=page_size, uid=uid, operation=operation, start=start, end=end)

成员贡献

查看项目所有的贡献

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
from paratranz_client.models.get_scores200_response import GetScores200Response
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
    api_instance = paratranz_client.ScoresApi(api_client)
    project_id = 56 # int | 项目ID
    page = 1 # int | 页码 (optional) (default to 1)
    page_size = 50 # int | 每页数量 (optional) (default to 50)
    uid = 3.4 # float | 指定用户ID (optional)
    operation = 'operation_example' # str | 指定类型获取贡献 (optional)
    start = '2013-10-20T19:20:30+01:00' # datetime | 筛选开始时间 (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime | 筛选结束时间 (optional)

    try:
        # 成员贡献
        api_response = await api_instance.get_scores(project_id, page=page, page_size=page_size, uid=uid, operation=operation, start=start, end=end)
        print("The response of ScoresApi->get_scores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoresApi->get_scores: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **page** | **int**| 页码 | [optional] [default to 1]
 **page_size** | **int**| 每页数量 | [optional] [default to 50]
 **uid** | **float**| 指定用户ID | [optional] 
 **operation** | **str**| 指定类型获取贡献 | [optional] 
 **start** | **datetime**| 筛选开始时间 | [optional] 
 **end** | **datetime**| 筛选结束时间 | [optional] 

### Return type

[**GetScores200Response**](GetScores200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 返回贡献列表 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

