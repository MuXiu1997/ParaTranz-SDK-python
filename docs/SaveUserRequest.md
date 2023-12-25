# SaveUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nickname** | **str** |  | [optional] 
**bio** | **str** | 个人介绍 | [optional] 
**avatar** | **str** | 头像图片链接 | [optional] 

## Example

```python
from paratranz_client.models.save_user_request import SaveUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveUserRequest from a JSON string
save_user_request_instance = SaveUserRequest.from_json(json)
# print the JSON string representation of the object
print SaveUserRequest.to_json()

# convert the object into a dict
save_user_request_dict = save_user_request_instance.to_dict()
# create an instance of SaveUserRequest from a dict
save_user_request_form_dict = save_user_request.from_dict(save_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


