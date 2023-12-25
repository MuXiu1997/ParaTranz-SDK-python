# Artifact

导出结果

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**project** | **int** | 项目ID | [optional] [readonly] 
**total** | **int** | 导出时项目词条总条数 | [optional] 
**translated** | **int** | 导出时项目词条已翻译的条数 | [optional] 
**disputed** | **int** | 导出时项目词条有疑问的条数 | [optional] 
**reviewed** | **int** | 导出时项目词条已审核的条数 | [optional] 
**hidden** | **int** | 导出时项目词条已隐藏的条数 | [optional] 
**duration** | **int** | 导出压缩包所用的时间 (ms) | [optional] 

## Example

```python
from paratranz_client.models.artifact import Artifact

# TODO update the JSON string below
json = "{}"
# create an instance of Artifact from a JSON string
artifact_instance = Artifact.from_json(json)
# print the JSON string representation of the object
print Artifact.to_json()

# convert the object into a dict
artifact_dict = artifact_instance.to_dict()
# create an instance of Artifact from a dict
artifact_form_dict = artifact.from_dict(artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


