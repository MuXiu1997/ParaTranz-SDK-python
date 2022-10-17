# paratranz_client.model.revision.Revision

文件上传记录

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 文件上传记录 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | [**Id**](Id.md) | [**Id**](Id.md) |  | [optional] 
**createdAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**name** | str,  | str,  | 文件名 | [optional] 
**filename** | str,  | str,  | 上传文件的名称 | [optional] 
**type** | str,  | str,  | 操作方式 * create - 创建文件 * update - 更新文件 * import - 导入翻译  | [optional] must be one of ["create", "update", "import", ] 
**file** | decimal.Decimal, int,  | decimal.Decimal,  | 文件ID | [optional] 
**uid** | [**UserId**](UserId.md) | [**UserId**](UserId.md) |  | [optional] 
**project** | [**ProjectId**](ProjectId.md) | [**ProjectId**](ProjectId.md) |  | [optional] 
**insert** | decimal.Decimal, int,  | decimal.Decimal,  | 新增的词条数量 | [optional] 
**update** | decimal.Decimal, int,  | decimal.Decimal,  | 更新的词条数量 | [optional] 
**remove** | decimal.Decimal, int,  | decimal.Decimal,  | 删除的词条数量 | [optional] 
**hash** | str,  | str,  | 文件内容哈希值（MD5） | [optional] 
**force** | bool,  | BoolClass,  | 是否是强制更新 | [optional] 
**incremental** | bool,  | BoolClass,  | 是否是增量更新 | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

