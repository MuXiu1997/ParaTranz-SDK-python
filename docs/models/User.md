# paratranz_client.model.user.User

用户

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 用户 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | [**UserId**](UserId.md) | [**UserId**](UserId.md) |  | [optional] 
**createdAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**updatedAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**[lastVisit](#lastVisit)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 用户最近访问时间 | [optional] 
**username** | str,  | str,  | 用户名 | [optional] 
**nickname** | str,  | str,  | 用户昵称 | [optional] 
**bio** | str,  | str,  | 用户简介 | [optional] 
**avatar** | str,  | str,  | 用户头像 | [optional] 
**email** | str,  | str,  | 用户邮箱 | [optional] 
**credit** | decimal.Decimal, int,  | decimal.Decimal,  | 用户信用值，低于0将会被限制使用 | [optional] if omitted the server will use the default value of 5
**translated** | decimal.Decimal, int,  | decimal.Decimal,  | 用户翻译的词条数量 | [optional] 
**edited** | decimal.Decimal, int,  | decimal.Decimal,  | 用户编辑的词条数量 | [optional] 
**reviewed** | decimal.Decimal, int,  | decimal.Decimal,  | 用户审核的词条数量 | [optional] 
**commented** | decimal.Decimal, int,  | decimal.Decimal,  | 用户发布的评论数 | [optional] 
**points** | decimal.Decimal, int, float,  | decimal.Decimal,  | 用户的贡献值（PP），计算公式为 1 * 翻译词条总词数 + 0.5 * 编辑词条总词数 + 0.2 * 审核词条总词数 | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# lastVisit

用户最近访问时间

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 用户最近访问时间 | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# all_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

