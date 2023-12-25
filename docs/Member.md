# Member

成员

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**uid** | **int** | 用户ID | [optional] 
**user** | [**User**](User.md) |  | [optional] [readonly] 
**project** | **int** | 项目ID | [optional] [readonly] 
**permission** | [**Permission**](Permission.md) |  | [optional] 
**total_points** | **float** | 成员PP值 | [optional] [readonly] 
**translated** | **int** | 翻译条数 | [optional] [readonly] 
**edited** | **int** | 编辑条数 | [optional] [readonly] 
**reviewed** | **int** | 审核条数 | [optional] [readonly] 
**note** | **str** | 成员备注 | [optional] 

## Example

```python
from paratranz_client.models.member import Member

# TODO update the JSON string below
json = "{}"
# create an instance of Member from a JSON string
member_instance = Member.from_json(json)
# print the JSON string representation of the object
print Member.to_json()

# convert the object into a dict
member_dict = member_instance.to_dict()
# create an instance of Member from a dict
member_form_dict = member.from_dict(member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


