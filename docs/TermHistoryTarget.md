# TermHistoryTarget

修改后术语的完整数据

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pos** | **str** |  | [optional] 
**term** | **str** |  | [optional] 
**translation** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**variants** | **List[str]** |  | [optional] 

## Example

```python
from paratranz_client.models.term_history_target import TermHistoryTarget

# TODO update the JSON string below
json = "{}"
# create an instance of TermHistoryTarget from a JSON string
term_history_target_instance = TermHistoryTarget.from_json(json)
# print the JSON string representation of the object
print TermHistoryTarget.to_json()

# convert the object into a dict
term_history_target_dict = term_history_target_instance.to_dict()
# create an instance of TermHistoryTarget from a dict
term_history_target_form_dict = term_history_target.from_dict(term_history_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


