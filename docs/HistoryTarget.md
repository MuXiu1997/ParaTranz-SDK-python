# HistoryTarget

修改后词条的完整数据

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**original** | **str** |  | [optional] 
**translation** | **str** |  | [optional] 
**stage** | **int** |  | [optional] 

## Example

```python
from paratranz_client.models.history_target import HistoryTarget

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryTarget from a JSON string
history_target_instance = HistoryTarget.from_json(json)
# print the JSON string representation of the object
print HistoryTarget.to_json()

# convert the object into a dict
history_target_dict = history_target_instance.to_dict()
# create an instance of HistoryTarget from a dict
history_target_form_dict = history_target.from_dict(history_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


