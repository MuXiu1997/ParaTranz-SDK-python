# GetIssues200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** | 页码 | [optional] [default to 1]
**page_size** | **float** | 每页数量 | [optional] [default to 50]
**row_count** | **float** | 总条数 | [optional] [default to 0]
**page_count** | **float** | 总页数，通过总条数与每页数量计算得出 | [optional] [default to 0]
**closed_count** | **int** | 已关闭的讨论数量 | [optional] 
**open_count** | **int** | 讨论中的讨论数量 | [optional] 
**results** | [**List[GetIssues200ResponseResultsInner]**](GetIssues200ResponseResultsInner.md) |  | [optional] 

## Example

```python
from paratranz_client.models.get_issues200_response import GetIssues200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetIssues200Response from a JSON string
get_issues200_response_instance = GetIssues200Response.from_json(json)
# print the JSON string representation of the object
print GetIssues200Response.to_json()

# convert the object into a dict
get_issues200_response_dict = get_issues200_response_instance.to_dict()
# create an instance of GetIssues200Response from a dict
get_issues200_response_form_dict = get_issues200_response.from_dict(get_issues200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


