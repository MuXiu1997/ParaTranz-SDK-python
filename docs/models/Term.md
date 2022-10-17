# paratranz_client.model.term.Term

术语

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 术语 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**createdAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**updatedAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**updatedBy** | decimal.Decimal, int,  | decimal.Decimal,  | 最后修改用户的ID | [optional] 
**pos** | str,  | str,  | 术语词性 | [optional] must be one of ["noun", "verb", "adj", "adv", ] 
**uid** | decimal.Decimal, int,  | decimal.Decimal,  | 创建用户的ID | [optional] 
**term** | str,  | str,  | 术语原文 | [optional] 
**translation** | str,  | str,  | 术语译文 | [optional] 
**note** | str,  | str,  | 术语注释 | [optional] 
**project** | decimal.Decimal, int,  | decimal.Decimal,  | 术语所属项目ID | [optional] 
**[variants](#variants)** | list, tuple,  | tuple,  | 术语原文的其他形式（复数形式、其他时态等） | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# variants

术语原文的其他形式（复数形式、其他时态等）

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | 术语原文的其他形式（复数形式、其他时态等） | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

