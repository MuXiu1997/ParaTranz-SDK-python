# Issue

讨论

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from paratranz_client.models.issue import Issue

# TODO update the JSON string below
json = "{}"
# create an instance of Issue from a JSON string
issue_instance = Issue.from_json(json)
# print the JSON string representation of the object
print Issue.to_json()

# convert the object into a dict
issue_dict = issue_instance.to_dict()
# create an instance of Issue from a dict
issue_form_dict = issue.from_dict(issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


