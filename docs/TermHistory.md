# TermHistory

术语历史记录

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**field** | **str** | 修改的字段 | [optional] 
**uid** | **int** | 用户ID | [optional] [readonly] 
**tid** | **int** | 术语ID | [optional] 
**var_from** | **str** | 修改前的值 | [optional] 
**to** | **str** | 修改后的值 | [optional] 
**target** | [**TermHistoryTarget**](TermHistoryTarget.md) |  | [optional] 
**operation** | **str** | 历史记录操作类型 | [optional] 

## Example

```python
from paratranz_client.models.term_history import TermHistory

# TODO update the JSON string below
json = "{}"
# create an instance of TermHistory from a JSON string
term_history_instance = TermHistory.from_json(json)
# print the JSON string representation of the object
print TermHistory.to_json()

# convert the object into a dict
term_history_dict = term_history_instance.to_dict()
# create an instance of TermHistory from a dict
term_history_form_dict = term_history.from_dict(term_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


