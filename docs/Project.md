# Project

项目

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**uid** | **int** | 所有者用户ID | [optional] [readonly] 
**user** | **object** | 所有者用户信息 | [optional] [readonly] 
**name** | **str** | 项目名称 | [optional] 
**logo** | **str** | 项目LOGO链接 | [optional] 
**desc** | **str** | 项目说明 | [optional] 
**source** | **str** | 源语言 | [optional] 
**dest** | **str** | 目标语言 | [optional] 
**members** | **int** | 成员数量 | [optional] [readonly] 
**game** | **str** | 所属游戏 | [optional] 
**license** | **str** | 项目使用的许可证 | [optional] [readonly] 
**active_level** | **float** | 项目活跃度 | [optional] [readonly] 
**stage** | **int** | 项目状态 | [optional] [readonly] 
**privacy** | **int** | 项目隐私状态 * 0 - 公开 * 1 - 内部（项目公开但动态及文件私密） * 2 - 私密  | [optional] 
**download** | **int** | 下载权限 * 0 - 公开 * 1 - 内部 * 2 - 私密  | [optional] 
**issue_mode** | **int** | 讨论权限 * 0 - 公开（所有用户都可以创建及加入讨论） * 1 - 内部（仅项目成员可以创建讨论但所有用户都可以加入） * 2 - 私密（仅项目成员可以创建及加入讨论）  | [optional] 
**review_mode** | **int** | 校对等级 * 0 - 无须校对 * 1 - 一次校对 * 2 - 二次校对  | [optional] 
**join_mode** | **int** | 加入方式 * 0 - 公开（所有用户都可以直接加入项目） * 1 - 申请（加入项目需提交申请） * 2 - 测试（加入项目需完成测试） * 3 - 私密（仅管理员可添加成员）  | [optional] 

## Example

```python
from paratranz_client.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print Project.to_json()

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_form_dict = project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


