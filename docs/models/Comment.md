# paratranz_client.model.comment.Comment

评论

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 评论 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**createdAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**uid** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**project** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**type** | str,  | str,  | 评论的相关条目类型 | [optional] must be one of ["text", "announcement", "term", ] 
**tid** | decimal.Decimal, int,  | decimal.Decimal,  | 条目ID | [optional] 
**content** | str,  | str,  | 评论内容，markdown 原始数据 | [optional] 
**html** | str,  | str,  | markdown 转换后的 html 数据 | [optional] 
**[images](#images)** | list, tuple,  | tuple,  | 图片链接列表 | [optional] 
**replyTo** | decimal.Decimal, int,  | decimal.Decimal,  | 回复的评论ID | [optional] 
**[refer](#refer)** | list, tuple,  | tuple,  | 评论中@的用户ID列表 | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# images

图片链接列表

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | 图片链接列表 | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# refer

评论中@的用户ID列表

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | 评论中@的用户ID列表 | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | 用户ID | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

