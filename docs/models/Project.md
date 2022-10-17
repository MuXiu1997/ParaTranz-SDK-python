# paratranz_client.model.project.Project

项目

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 项目 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**createdAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**updatedAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**uid** | decimal.Decimal, int,  | decimal.Decimal,  | 所有者用户ID | [optional] 
**name** | str,  | str,  |  | [optional] 
**logo** | str,  | str,  |  | [optional] 
**desc** | str,  | str,  |  | [optional] 
**source** | str,  | str,  | 源语言 | [optional] 
**dest** | str,  | str,  | 目标语言 | [optional] 
**members** | decimal.Decimal, int,  | decimal.Decimal,  | 成员数量 | [optional] 
**game** | decimal.Decimal, int,  | decimal.Decimal,  | 所属游戏 | [optional] 
**license** | str,  | str,  | 项目使用的许可证 | [optional] 
**activeLevel** | decimal.Decimal, int, float,  | decimal.Decimal,  | 项目活跃度 | [optional] 
**stage** | decimal.Decimal, int,  | decimal.Decimal,  | 项目状态 | [optional] 
**privacy** | decimal.Decimal, int,  | decimal.Decimal,  | 项目隐私状态 * 0 - 公开 * 1 - 内部（项目公开但动态及文件私密） * 2 - 私密  | [optional] 
**download** | decimal.Decimal, int,  | decimal.Decimal,  | 下载权限 * 0 - 公开 * 1 - 内部 * 2 - 私密  | [optional] 
**issueMode** | decimal.Decimal, int,  | decimal.Decimal,  | 讨论权限 * 0 - 公开（所有用户都可以创建及加入讨论） * 1 - 内部（仅项目成员可以创建讨论但所有用户都可以加入） * 2 - 私密（仅项目成员可以创建及加入讨论）  | [optional] 
**reviewMode** | decimal.Decimal, int,  | decimal.Decimal,  | 校对等级 * 0 - 无须校对 * 1 - 一次校对 * 2 - 二次校对  | [optional] 
**joinMode** | decimal.Decimal, int,  | decimal.Decimal,  | 加入方式 * 0 - 公开（所有用户都可以直接加入项目） * 1 - 申请（加入项目需提交申请） * 2 - 测试（加入项目需完成测试） * 3 - 私密（仅管理员可添加成员）  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

