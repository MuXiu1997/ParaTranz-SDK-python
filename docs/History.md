# History

词条历史记录

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**field** | **str** | 修改的字段 | [optional] 
**uid** | **int** | 用户ID | [optional] [readonly] 
**user** | **object** | 操作者用户详情 | [optional] [readonly] 
**tid** | **int** | 词条ID | [optional] 
**var_from** | **str** | 修改前的值 | [optional] 
**to** | **str** | 修改后的值 | [optional] 
**target** | [**HistoryTarget**](HistoryTarget.md) |  | [optional] 
**operation** | **str** | 历史记录操作类型 | [optional] 

## Example

```python
from paratranz_client.models.history import History

# TODO update the JSON string below
json = "{}"
# create an instance of History from a JSON string
history_instance = History.from_json(json)
# print the JSON string representation of the object
print History.to_json()

# convert the object into a dict
history_dict = history_instance.to_dict()
# create an instance of History from a dict
history_form_dict = history.from_dict(history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


