# GetTerms200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** | 页码 | [optional] [default to 1]
**page_size** | **float** | 每页数量 | [optional] [default to 50]
**row_count** | **float** | 总条数 | [optional] [default to 0]
**page_count** | **float** | 总页数，通过总条数与每页数量计算得出 | [optional] [default to 0]
**results** | [**List[Term]**](Term.md) |  | [optional] 

## Example

```python
from paratranz_client.models.get_terms200_response import GetTerms200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTerms200Response from a JSON string
get_terms200_response_instance = GetTerms200Response.from_json(json)
# print the JSON string representation of the object
print GetTerms200Response.to_json()

# convert the object into a dict
get_terms200_response_dict = get_terms200_response_instance.to_dict()
# create an instance of GetTerms200Response from a dict
get_terms200_response_form_dict = get_terms200_response.from_dict(get_terms200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


