# Revision

文件上传记录

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**name** | **str** | 文件名 | [optional] [readonly] 
**filename** | **str** | 上传文件的名称 | [optional] [readonly] 
**type** | **str** | 操作方式 * create - 创建文件 * update - 更新文件 * import - 导入翻译  | [optional] 
**file** | **int** | 文件ID | [optional] 
**uid** | **int** | 用户ID | [optional] [readonly] 
**project** | **int** | 项目ID | [optional] [readonly] 
**insert** | **int** | 新增的词条数量 | [optional] 
**update** | **int** | 更新的词条数量 | [optional] 
**remove** | **int** | 删除的词条数量 | [optional] 
**hash** | **str** | 文件内容哈希值（MD5） | [optional] 
**force** | **bool** | 是否是强制更新 | [optional] 
**incremental** | **bool** | 是否是增量更新 | [optional] 

## Example

```python
from paratranz_client.models.revision import Revision

# TODO update the JSON string below
json = "{}"
# create an instance of Revision from a JSON string
revision_instance = Revision.from_json(json)
# print the JSON string representation of the object
print Revision.to_json()

# convert the object into a dict
revision_dict = revision_instance.to_dict()
# create an instance of Revision from a dict
revision_form_dict = revision.from_dict(revision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


