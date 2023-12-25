# paratranz_client.TermsApi

All URIs are relative to *https://paratranz.cn/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_term**](TermsApi.md#create_term) | **POST** /projects/{projectId}/terms | 创建术语
[**delete_term**](TermsApi.md#delete_term) | **DELETE** /projects/{projectId}/terms/{termId} | 删除术语
[**get_term**](TermsApi.md#get_term) | **GET** /projects/{projectId}/terms/{termId} | 术语信息
[**get_terms**](TermsApi.md#get_terms) | **GET** /projects/{projectId}/terms | 术语列表
[**import_terms**](TermsApi.md#import_terms) | **PUT** /projects/{projectId}/terms | 批量导入术语
[**save_term**](TermsApi.md#save_term) | **PUT** /projects/{projectId}/terms/{termId} | 修改术语


# **create_term**
> Term create_term(project_id, term, page=page, page_size=page_size)

创建术语

创建新术语，如果已存在相同术语会失败

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
from paratranz_client.models.term import Term
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
    api_instance = paratranz_client.TermsApi(api_client)
    project_id = 56 # int | 项目ID
    term = paratranz_client.Term() # Term | 
    page = 1 # int | 页码 (optional) (default to 1)
    page_size = 50 # int | 每页数量 (optional) (default to 50)

    try:
        # 创建术语
        api_response = await api_instance.create_term(project_id, term, page=page, page_size=page_size)
        print("The response of TermsApi->create_term:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermsApi->create_term: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **term** | [**Term**](Term.md)|  | 
 **page** | **int**| 页码 | [optional] [default to 1]
 **page_size** | **int**| 每页数量 | [optional] [default to 50]

### Return type

[**Term**](Term.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 术语信息 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_term**
> delete_term(project_id, term_id)

删除术语

通过ID删除术语，仅创建者及管理员可以删除

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
    api_instance = paratranz_client.TermsApi(api_client)
    project_id = 56 # int | 项目ID
    term_id = 56 # int | 术语ID

    try:
        # 删除术语
        await api_instance.delete_term(project_id, term_id)
    except Exception as e:
        print("Exception when calling TermsApi->delete_term: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **term_id** | **int**| 术语ID | 

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

# **get_term**
> Term get_term(project_id, term_id)

术语信息

通过ID获取项目术语信息

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
from paratranz_client.models.term import Term
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
    api_instance = paratranz_client.TermsApi(api_client)
    project_id = 56 # int | 项目ID
    term_id = 56 # int | 术语ID

    try:
        # 术语信息
        api_response = await api_instance.get_term(project_id, term_id)
        print("The response of TermsApi->get_term:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermsApi->get_term: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **term_id** | **int**| 术语ID | 

### Return type

[**Term**](Term.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 术语信息 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_terms**
> GetTerms200Response get_terms(project_id, page=page, page_size=page_size)

术语列表

获取项目术语列表

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
from paratranz_client.models.get_terms200_response import GetTerms200Response
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
    api_instance = paratranz_client.TermsApi(api_client)
    project_id = 56 # int | 项目ID
    page = 1 # int | 页码 (optional) (default to 1)
    page_size = 50 # int | 每页数量 (optional) (default to 50)

    try:
        # 术语列表
        api_response = await api_instance.get_terms(project_id, page=page, page_size=page_size)
        print("The response of TermsApi->get_terms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermsApi->get_terms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **page** | **int**| 页码 | [optional] [default to 1]
 **page_size** | **int**| 每页数量 | [optional] [default to 50]

### Return type

[**GetTerms200Response**](GetTerms200Response.md)

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

# **import_terms**
> ImportTerms200Response import_terms(project_id, page=page, page_size=page_size, file=file)

批量导入术语

上传JSON文件批量导入术语

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
from paratranz_client.models.import_terms200_response import ImportTerms200Response
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
    api_instance = paratranz_client.TermsApi(api_client)
    project_id = 56 # int | 项目ID
    page = 1 # int | 页码 (optional) (default to 1)
    page_size = 50 # int | 每页数量 (optional) (default to 50)
    file = None # bytearray | JSON文件数据，示例如下 ```  [     {       \\\"term\\\": \\\"apple\\\",       \\\"translation\\\": \\\"苹果\\\",       \\\"pos\\\": \\\"noun\\\",       \\\"note\\\": \\\"注释\\\",       \\\"variants\\\": [\\\"apples\\\"]     }   ] ```  (optional)

    try:
        # 批量导入术语
        api_response = await api_instance.import_terms(project_id, page=page, page_size=page_size, file=file)
        print("The response of TermsApi->import_terms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermsApi->import_terms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **page** | **int**| 页码 | [optional] [default to 1]
 **page_size** | **int**| 每页数量 | [optional] [default to 50]
 **file** | **bytearray**| JSON文件数据，示例如下 &#x60;&#x60;&#x60;  [     {       \\\&quot;term\\\&quot;: \\\&quot;apple\\\&quot;,       \\\&quot;translation\\\&quot;: \\\&quot;苹果\\\&quot;,       \\\&quot;pos\\\&quot;: \\\&quot;noun\\\&quot;,       \\\&quot;note\\\&quot;: \\\&quot;注释\\\&quot;,       \\\&quot;variants\\\&quot;: [\\\&quot;apples\\\&quot;]     }   ] &#x60;&#x60;&#x60;  | [optional] 

### Return type

[**ImportTerms200Response**](ImportTerms200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 术语导入成功 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_term**
> Term save_term(project_id, term_id, term)

修改术语

修改术语

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
from paratranz_client.models.term import Term
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
    api_instance = paratranz_client.TermsApi(api_client)
    project_id = 56 # int | 项目ID
    term_id = 56 # int | 术语ID
    term = paratranz_client.Term() # Term | 

    try:
        # 修改术语
        api_response = await api_instance.save_term(project_id, term_id, term)
        print("The response of TermsApi->save_term:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermsApi->save_term: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **term_id** | **int**| 术语ID | 
 **term** | [**Term**](Term.md)|  | 

### Return type

[**Term**](Term.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 术语信息 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

