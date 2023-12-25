# StringItem

词条

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 词条ID | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**key** | **str** | 词条键值，文件内必须唯一 | [optional] 
**original** | **str** | 词条原文 | [optional] 
**translation** | **str** | 词条译文 | [optional] 
**file** | **int** | 词条所属的文件ID | [optional] 
**stage** | [**Stage**](Stage.md) |  | [optional] 
**project** | **int** | 词条所属项目ID | [optional] [readonly] 
**uid** | **int** | 词条最后编辑用户的ID | [optional] [readonly] 
**context** | **str** | 词条上下文，可通过上传文件或API添加 | [optional] 
**words** | **int** | 词条原文字数（暂不支持中日韩计数） | [optional] [readonly] 

## Example

```python
from paratranz_client.models.string_item import StringItem

# TODO update the JSON string below
json = "{}"
# create an instance of StringItem from a JSON string
string_item_instance = StringItem.from_json(json)
# print the JSON string representation of the object
print StringItem.to_json()

# convert the object into a dict
string_item_dict = string_item_instance.to_dict()
# create an instance of StringItem from a dict
string_item_form_dict = string_item.from_dict(string_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


