# paratranz_client.FilesApi

All URIs are relative to *https://paratranz.cn/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file**](FilesApi.md#create_file) | **POST** /projects/{projectId}/files | 上传文件
[**delete_file**](FilesApi.md#delete_file) | **DELETE** /projects/{projectId}/files/{fileId} | 删除文件
[**get_file**](FilesApi.md#get_file) | **GET** /projects/{projectId}/files/{fileId} | 文件信息
[**get_file_translation**](FilesApi.md#get_file_translation) | **GET** /projects/{projectId}/files/{fileId}/translation | 文件翻译
[**get_files**](FilesApi.md#get_files) | **GET** /projects/{projectId}/files | 文件列表
[**save_file**](FilesApi.md#save_file) | **PUT** /projects/{projectId}/files/{fileId} | 修改文件
[**update_file**](FilesApi.md#update_file) | **POST** /projects/{projectId}/files/{fileId} | 更新文件
[**update_file_translation**](FilesApi.md#update_file_translation) | **POST** /projects/{projectId}/files/{fileId}/translation | 更新文件翻译


# **create_file**
> CreateFile200Response create_file(project_id, file=file, path=path)

上传文件

上传并创建文件，文件名不能与 path 指定的目录中的文件冲突

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
from paratranz_client.models.create_file200_response import CreateFile200Response
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
    api_instance = paratranz_client.FilesApi(api_client)
    project_id = 56 # int | 项目ID
    file = None # bytearray | 文件数据，文件名由此项的文件名决定 (optional)
    path = 'path_example' # str | 文件路径 (optional)

    try:
        # 上传文件
        api_response = await api_instance.create_file(project_id, file=file, path=path)
        print("The response of FilesApi->create_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->create_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **file** | **bytearray**| 文件数据，文件名由此项的文件名决定 | [optional] 
 **path** | **str**| 文件路径 | [optional] 

### Return type

[**CreateFile200Response**](CreateFile200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 文件上传成功 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> delete_file(project_id, file_id)

删除文件

通过ID删除文件

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
    api_instance = paratranz_client.FilesApi(api_client)
    project_id = 56 # int | 项目ID
    file_id = 56 # int | 文件ID

    try:
        # 删除文件
        await api_instance.delete_file(project_id, file_id)
    except Exception as e:
        print("Exception when calling FilesApi->delete_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **file_id** | **int**| 文件ID | 

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
**200** | 文件已删除 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> File get_file(project_id, file_id)

文件信息

通过ID获取文件信息

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
from paratranz_client.models.file import File
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
    api_instance = paratranz_client.FilesApi(api_client)
    project_id = 56 # int | 项目ID
    file_id = 56 # int | 文件ID

    try:
        # 文件信息
        api_response = await api_instance.get_file(project_id, file_id)
        print("The response of FilesApi->get_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **file_id** | **int**| 文件ID | 

### Return type

[**File**](File.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 完整文件信息 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_translation**
> get_file_translation(project_id, file_id)

文件翻译

通过ID获取文件翻译数据

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
    api_instance = paratranz_client.FilesApi(api_client)
    project_id = 56 # int | 项目ID
    file_id = 56 # int | 文件ID

    try:
        # 文件翻译
        await api_instance.get_file_translation(project_id, file_id)
    except Exception as e:
        print("Exception when calling FilesApi->get_file_translation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **file_id** | **int**| 文件ID | 

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
**200** | 返回JSON原始数据文件 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files**
> List[File] get_files(project_id)

文件列表

获取项目文件列表

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
from paratranz_client.models.file import File
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
    api_instance = paratranz_client.FilesApi(api_client)
    project_id = 56 # int | 项目ID

    try:
        # 文件列表
        api_response = await api_instance.get_files(project_id)
        print("The response of FilesApi->get_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 

### Return type

[**List[File]**](File.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 返回文件列表 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_file**
> File save_file(project_id, file_id, save_file_request)

修改文件

通过ID修改文件信息

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
from paratranz_client.models.file import File
from paratranz_client.models.save_file_request import SaveFileRequest
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
    api_instance = paratranz_client.FilesApi(api_client)
    project_id = 56 # int | 项目ID
    file_id = 56 # int | 文件ID
    save_file_request = paratranz_client.SaveFileRequest() # SaveFileRequest | 

    try:
        # 修改文件
        api_response = await api_instance.save_file(project_id, file_id, save_file_request)
        print("The response of FilesApi->save_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->save_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **file_id** | **int**| 文件ID | 
 **save_file_request** | [**SaveFileRequest**](SaveFileRequest.md)|  | 

### Return type

[**File**](File.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 完整文件信息 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file**
> File update_file(project_id, file_id, file=file)

更新文件

通过ID上传并更新文件

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
from paratranz_client.models.file import File
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
    api_instance = paratranz_client.FilesApi(api_client)
    project_id = 56 # int | 项目ID
    file_id = 56 # int | 文件ID
    file = None # bytearray | 文件数据，格式需与创建时的文件保持一致，也可上传标准JSON格式（文件名需为原文件名加.json） (optional)

    try:
        # 更新文件
        api_response = await api_instance.update_file(project_id, file_id, file=file)
        print("The response of FilesApi->update_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->update_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **file_id** | **int**| 文件ID | 
 **file** | **bytearray**| 文件数据，格式需与创建时的文件保持一致，也可上传标准JSON格式（文件名需为原文件名加.json） | [optional] 

### Return type

[**File**](File.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 完整文件信息 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file_translation**
> File update_file_translation(project_id, file_id, file=file, force=force)

更新文件翻译

通过ID上传并更新文件中的词条翻译

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
from paratranz_client.models.file import File
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
    api_instance = paratranz_client.FilesApi(api_client)
    project_id = 56 # int | 项目ID
    file_id = 56 # int | 文件ID
    file = None # bytearray | 文件数据，格式需与创建时的文件保持一致，也可上传标准JSON格式（文件名需为原文件名加.json） (optional)
    force = True # bool | 是否强制覆盖翻译，默认为 `false`，此时翻译仅会覆盖未人工编辑过的词条 (optional)

    try:
        # 更新文件翻译
        api_response = await api_instance.update_file_translation(project_id, file_id, file=file, force=force)
        print("The response of FilesApi->update_file_translation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->update_file_translation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 项目ID | 
 **file_id** | **int**| 文件ID | 
 **file** | **bytearray**| 文件数据，格式需与创建时的文件保持一致，也可上传标准JSON格式（文件名需为原文件名加.json） | [optional] 
 **force** | **bool**| 是否强制覆盖翻译，默认为 &#x60;false&#x60;，此时翻译仅会覆盖未人工编辑过的词条 | [optional] 

### Return type

[**File**](File.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 完整文件信息 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

