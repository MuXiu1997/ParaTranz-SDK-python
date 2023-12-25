# SaveFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 文件名，需填写完整路径 | [optional] 
**extra** | **object** | JSON 格式，可随意填写需要的保存的其他信息 | [optional] 

## Example

```python
from paratranz_client.models.save_file_request import SaveFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveFileRequest from a JSON string
save_file_request_instance = SaveFileRequest.from_json(json)
# print the JSON string representation of the object
print SaveFileRequest.to_json()

# convert the object into a dict
save_file_request_dict = save_file_request_instance.to_dict()
# create an instance of SaveFileRequest from a dict
save_file_request_form_dict = save_file_request.from_dict(save_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


