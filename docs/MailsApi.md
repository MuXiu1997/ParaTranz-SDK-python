# paratranz_client.MailsApi

All URIs are relative to *https://paratranz.cn/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mail**](MailsApi.md#create_mail) | **POST** /mails | 发送私信
[**get_conversation**](MailsApi.md#get_conversation) | **GET** /mails/conversations/{userId} | 用户对话
[**get_mails**](MailsApi.md#get_mails) | **GET** /mails | 私信列表


# **create_mail**
> Mail create_mail(mail)

发送私信

向其他用户发送私信

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
from paratranz_client.models.mail import Mail
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
    api_instance = paratranz_client.MailsApi(api_client)
    mail = paratranz_client.Mail() # Mail | 

    try:
        # 发送私信
        api_response = await api_instance.create_mail(mail)
        print("The response of MailsApi->create_mail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailsApi->create_mail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail** | [**Mail**](Mail.md)|  | 

### Return type

[**Mail**](Mail.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 返回私信 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversation**
> List[Mail] get_conversation(user_id)

用户对话

通过用户ID获取与某用户的对话

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
from paratranz_client.models.mail import Mail
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
    api_instance = paratranz_client.MailsApi(api_client)
    user_id = 56 # int | 用户ID

    try:
        # 用户对话
        api_response = await api_instance.get_conversation(user_id)
        print("The response of MailsApi->get_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailsApi->get_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| 用户ID | 

### Return type

[**List[Mail]**](Mail.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 返回私信会话 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mails**
> GetMails200Response get_mails(page=page, page_size=page_size)

私信列表

获取私信列表

### Example

* Api Key Authentication (Token):

```python
import time
import os
import paratranz_client
from paratranz_client.models.get_mails200_response import GetMails200Response
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
    api_instance = paratranz_client.MailsApi(api_client)
    page = 1 # int | 页码 (optional) (default to 1)
    page_size = 50 # int | 每页数量 (optional) (default to 50)

    try:
        # 私信列表
        api_response = await api_instance.get_mails(page=page, page_size=page_size)
        print("The response of MailsApi->get_mails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailsApi->get_mails: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| 页码 | [optional] [default to 1]
 **page_size** | **int**| 每页数量 | [optional] [default to 50]

### Return type

[**GetMails200Response**](GetMails200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 返回私信列表 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

