# paratranz_client.model.artifact.Artifact

导出结果

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 导出结果 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | [**Id**](Id.md) | [**Id**](Id.md) |  | [optional] 
**createdAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**project** | [**ProjectId**](ProjectId.md) | [**ProjectId**](ProjectId.md) |  | [optional] 
**total** | decimal.Decimal, int,  | decimal.Decimal,  | 导出时项目词条总条数 | [optional] 
**translated** | decimal.Decimal, int,  | decimal.Decimal,  | 导出时项目词条已翻译的条数 | [optional] 
**disputed** | decimal.Decimal, int,  | decimal.Decimal,  | 导出时项目词条有疑问的条数 | [optional] 
**reviewed** | decimal.Decimal, int,  | decimal.Decimal,  | 导出时项目词条已审核的条数 | [optional] 
**hidden** | decimal.Decimal, int,  | decimal.Decimal,  | 导出时项目词条已隐藏的条数 | [optional] 
**duration** | decimal.Decimal, int,  | decimal.Decimal,  | 导出压缩包所用的时间（ms) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

