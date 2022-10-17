# paratranz_client.model.string.String

词条

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 词条 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | 词条ID | [optional] 
**createdAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**updatedAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**key** | str,  | str,  | 词条键值，文件内必须唯一 | [optional] 
**original** | str,  | str,  | 词条原文 | [optional] 
**translation** | str,  | str,  | 词条译文 | [optional] 
**file** | decimal.Decimal, int,  | decimal.Decimal,  | 词条所属的文件ID | [optional] 
**stage** | [**Stage**](Stage.md) | [**Stage**](Stage.md) |  | [optional] 
**project** | decimal.Decimal, int,  | decimal.Decimal,  | 词条所属项目ID | [optional] 
**uid** | decimal.Decimal, int,  | decimal.Decimal,  | 词条最后编辑用户的ID | [optional] 
**context** | str,  | str,  | 词条上下文，可通过上传文件或API添加 | [optional] 
**words** | decimal.Decimal, int,  | decimal.Decimal,  | 词条原文字数（暂不支持中日韩计数） | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

