# Term

术语

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**updated_by** | **int** | 最后修改用户的ID | [optional] [readonly] 
**pos** | **str** | 术语词性 | [optional] 
**uid** | **int** | 创建用户的ID | [optional] [readonly] 
**term** | **str** | 术语原文 | [optional] 
**translation** | **str** | 术语译文 | [optional] 
**note** | **str** | 术语注释 | [optional] 
**project** | **int** | 术语所属项目ID | [optional] [readonly] 
**variants** | **List[str]** | 术语原文的其他形式（复数形式、其他时态等） | [optional] 

## Example

```python
from paratranz_client.models.term import Term

# TODO update the JSON string below
json = "{}"
# create an instance of Term from a JSON string
term_instance = Term.from_json(json)
# print the JSON string representation of the object
print Term.to_json()

# convert the object into a dict
term_dict = term_instance.to_dict()
# create an instance of Term from a dict
term_form_dict = term.from_dict(term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


