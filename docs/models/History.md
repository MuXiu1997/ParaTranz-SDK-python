# paratranz_client.model.history.History

词条历史记录

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 词条历史记录 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**createdAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**field** | str,  | str,  | 修改的字段 | [optional] 
**uid** | [**UserId**](UserId.md) | [**UserId**](UserId.md) |  | [optional] 
**tid** | decimal.Decimal, int,  | decimal.Decimal,  | 词条ID | [optional] 
**from** | str,  | str,  | 修改前的值 | [optional] 
**to** | str,  | str,  | 修改后的值 | [optional] 
**[target](#target)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 修改后词条的完整数据 | [optional] 
**operation** | str,  | str,  | 历史记录操作类型 | [optional] must be one of ["translate", "edit", "reset", "dispute", "review", "rollback", "lock", "hide", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# target

修改后词条的完整数据

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 修改后词条的完整数据 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**key** | str,  | str,  |  | [optional] 
**original** | str,  | str,  |  | [optional] 
**translation** | str,  | str,  |  | [optional] 
**stage** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
