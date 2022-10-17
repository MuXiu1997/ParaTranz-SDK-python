# paratranz_client.model.score.Score

贡献

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 贡献 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | [**Id**](Id.md) | [**Id**](Id.md) |  | [optional] 
**createdAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**project** | [**ProjectId**](ProjectId.md) | [**ProjectId**](ProjectId.md) |  | [optional] 
**uid** | [**UserId**](UserId.md) | [**UserId**](UserId.md) |  | [optional] 
**base** | decimal.Decimal, int,  | decimal.Decimal,  | 贡献值基准，翻译为1，编辑为0.5，审核为0.2 | [optional] value must be a 64 bit float
**multiplier** | decimal.Decimal, int,  | decimal.Decimal,  | 贡献值乘数，公式为 1 + (词数 - 1) * 0.1 | [optional] value must be a 64 bit float
**value** | decimal.Decimal, int,  | decimal.Decimal,  | 基准乘以乘数得到的最终值 | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

