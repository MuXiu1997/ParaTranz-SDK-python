# ImportTerms200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inserted** | **int** | 新创建的术语数量 | [optional] 
**updated** | **int** | 已更新的术语数量 | [optional] 
**deleted** | **int** | 已删除的术语数量 | [optional] 

## Example

```python
from paratranz_client.models.import_terms200_response import ImportTerms200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ImportTerms200Response from a JSON string
import_terms200_response_instance = ImportTerms200Response.from_json(json)
# print the JSON string representation of the object
print ImportTerms200Response.to_json()

# convert the object into a dict
import_terms200_response_dict = import_terms200_response_instance.to_dict()
# create an instance of ImportTerms200Response from a dict
import_terms200_response_form_dict = import_terms200_response.from_dict(import_terms200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


