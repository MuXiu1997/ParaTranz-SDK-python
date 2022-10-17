# paratranz_client.model.file.File

文件

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 文件 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**createdAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**updatedAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**name** | str,  | str,  |  | [optional] 
**project** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**format** | str,  | str,  | 文件格式，由系统自动计算 | [optional] 
**total** | decimal.Decimal, int,  | decimal.Decimal,  | 文件总词条数 | [optional] 
**translated** | decimal.Decimal, int,  | decimal.Decimal,  | 已翻译词条数 | [optional] 
**disputed** | decimal.Decimal, int,  | decimal.Decimal,  | 有疑问的词条数 | [optional] 
**checked** | decimal.Decimal, int,  | decimal.Decimal,  | 已检查的词条数 | [optional] 
**reviewed** | decimal.Decimal, int,  | decimal.Decimal,  | 已审核的词条数 | [optional] 
**hidden** | decimal.Decimal, int,  | decimal.Decimal,  | 已隐藏的词条数 | [optional] 
**locked** | decimal.Decimal, int,  | decimal.Decimal,  | 已锁定的词条数 | [optional] 
**words** | decimal.Decimal, int,  | decimal.Decimal,  | 总词数 | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

