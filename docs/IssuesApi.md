# paratranz_client.IssuesApi

All URIs are relative to *https://paratranz.cn/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_issue**](IssuesApi.md#create_issue) | **POST** /projects/{projectId}/issues | 发起讨论
[**delete_issue**](IssuesApi.md#delete_issue) | **DELETE** /projects/{projectId}/issues/{issueId} | 删除讨论
[**get_issue**](IssuesApi.md#get_issue) | **GET** /projects/{projectId}/issues/{issueId} | 讨论信息
[**get_issues**](IssuesApi.md#get_issues) | **GET** /projects/{projectId}/issues | 讨论列表
[**operate_issue**](IssuesApi.md#operate_issue) | **POST** /projects/{projectId}/issues/{issueId} | 操作讨论
[**save_issue**](IssuesApi.md#save_issue) | **PUT** /projects/{projectId}/issues/{issueId} | 修改讨论


# **create_issue**
> Issue create_issue(project_id, create_issue_request)

发起讨论

创建一条新的讨论，权限可通过设置页面调整

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
from paratranz_client.models.create_issue_request import CreateIssueRequest
from paratranz_client.models.issue import Issue
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
    api_instance = paratranz_client.IssuesApi(api_client)
    project_id = 56 # int | 项目ID
    create_issue_request = paratranz_client.CreateIssueRequest() # CreateIssueRequest | 

    try:
        # 发起讨论
        api_response = await api_instance.create_issue(project_id, create_issue_request)
        print("The response of IssuesApi->create_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->create_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **create_issue_request** | [**CreateIssueRequest**](CreateIssueRequest.md)|  | 

### Return type

[**Issue**](Issue.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 返回新创建的讨论 |  -  |
**403** | 没有权限创建讨论 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_issue**
> delete_issue(project_id, issue_id)

删除讨论

通过ID删除讨论及对话

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
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
    api_instance = paratranz_client.IssuesApi(api_client)
    project_id = 56 # int | 项目ID
    issue_id = 56 # int | 讨论ID

    try:
        # 删除讨论
        await api_instance.delete_issue(project_id, issue_id)
    except Exception as e:
        print("Exception when calling IssuesApi->delete_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **issue_id** | **int**| 讨论ID | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 删除成功 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issue**
> GetIssue200Response get_issue(project_id, issue_id)

讨论信息

通过ID获取讨论信息

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
from paratranz_client.models.get_issue200_response import GetIssue200Response
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
    api_instance = paratranz_client.IssuesApi(api_client)
    project_id = 56 # int | 项目ID
    issue_id = 56 # int | 讨论ID

    try:
        # 讨论信息
        api_response = await api_instance.get_issue(project_id, issue_id)
        print("The response of IssuesApi->get_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->get_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **issue_id** | **int**| 讨论ID | 

### Return type

[**GetIssue200Response**](GetIssue200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 返回讨论信息 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issues**
> GetIssues200Response get_issues(project_id, status=status)

讨论列表

获取讨论列表

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
from paratranz_client.models.get_issues200_response import GetIssues200Response
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
    api_instance = paratranz_client.IssuesApi(api_client)
    project_id = 56 # int | 项目ID
    status = 3.4 # float | 按状态筛选讨论（0 - 讨论中，1 - 已关闭） (optional)

    try:
        # 讨论列表
        api_response = await api_instance.get_issues(project_id, status=status)
        print("The response of IssuesApi->get_issues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->get_issues: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **status** | **float**| 按状态筛选讨论（0 - 讨论中，1 - 已关闭） | [optional] 

### Return type

[**GetIssues200Response**](GetIssues200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 讨论列表 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operate_issue**
> operate_issue(project_id, issue_id, operate_issue_request)

操作讨论

回复/订阅/取消订阅某个讨论

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
from paratranz_client.models.operate_issue_request import OperateIssueRequest
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
    api_instance = paratranz_client.IssuesApi(api_client)
    project_id = 56 # int | 项目ID
    issue_id = 56 # int | 讨论ID
    operate_issue_request = paratranz_client.OperateIssueRequest() # OperateIssueRequest | 

    try:
        # 操作讨论
        await api_instance.operate_issue(project_id, issue_id, operate_issue_request)
    except Exception as e:
        print("Exception when calling IssuesApi->operate_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **issue_id** | **int**| 讨论ID | 
 **operate_issue_request** | [**OperateIssueRequest**](OperateIssueRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 返回操作结果 |  -  |
**201** | 返回新创建回复信息 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_issue**
> Issue save_issue(project_id, issue_id, issue=issue)

修改讨论

修改讨论内容

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
from paratranz_client.models.issue import Issue
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
    api_instance = paratranz_client.IssuesApi(api_client)
    project_id = 56 # int | 项目ID
    issue_id = 56 # int | 讨论ID
    issue = paratranz_client.Issue() # Issue |  (optional)

    try:
        # 修改讨论
        api_response = await api_instance.save_issue(project_id, issue_id, issue=issue)
        print("The response of IssuesApi->save_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->save_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **issue_id** | **int**| 讨论ID | 
 **issue** | [**Issue**](Issue.md)|  | [optional] 

### Return type

[**Issue**](Issue.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 返回已修改的讨论信息 |  -  |
**403** | 没有权限修改讨论 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

