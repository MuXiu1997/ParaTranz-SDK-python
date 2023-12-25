# GetIssue200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activities** | [**List[Reply]**](Reply.md) | 讨论的回复及操作记录 | [optional] 
**subscribers** | [**List[User]**](User.md) | 订阅讨论的用户列表 | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**id** | **int** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**project** | **int** | 项目ID | [optional] [readonly] 
**uid** | **int** | 用户ID | [optional] [readonly] 
**parent** | **int** | 当前对话条目所属讨论ID，用是否有parent字段判断类型 | [optional] [readonly] 
**title** | **str** | 标题，仅主讨论中存在 | [optional] 
**content** | **str** | 原始内容（markdown） | [optional] 
**html** | **str** | content 的 markdown 转换之后的 html | [optional] [readonly] 
**status** | **int** | 主讨论的状态，0 - 讨论中，1 - 已关闭 | [optional] 
**last_edit** | **int** | 用户ID | [optional] [readonly] 
**refer** | **List[int]** | 在内容中提到（@）的用户的uid列表，如 &#x60;[1, 2, 3]&#x60; | [optional] [readonly] 

## Example

```python
from paratranz_client.models.get_issue200_response import GetIssue200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetIssue200Response from a JSON string
get_issue200_response_instance = GetIssue200Response.from_json(json)
# print the JSON string representation of the object
print GetIssue200Response.to_json()

# convert the object into a dict
get_issue200_response_dict = get_issue200_response_instance.to_dict()
# create an instance of GetIssue200Response from a dict
get_issue200_response_form_dict = get_issue200_response.from_dict(get_issue200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


