# CreateFile200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | [**File**](File.md) |  | [optional] 
**revision** | [**Revision**](Revision.md) |  | [optional] 

## Example

```python
from paratranz_client.models.create_file200_response import CreateFile200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFile200Response from a JSON string
create_file200_response_instance = CreateFile200Response.from_json(json)
# print the JSON string representation of the object
print CreateFile200Response.to_json()

# convert the object into a dict
create_file200_response_dict = create_file200_response_instance.to_dict()
# create an instance of CreateFile200Response from a dict
create_file200_response_form_dict = create_file200_response.from_dict(create_file200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


