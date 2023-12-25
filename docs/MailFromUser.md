# MailFromUser

发送者的用户信息

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 用户ID | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**last_visit** | **datetime** |  | [optional] [readonly] 
**username** | **str** | 用户名 | [optional] [readonly] 
**nickname** | **str** | 用户昵称 | [optional] 
**bio** | **str** | 用户简介 | [optional] 
**avatar** | **str** | 用户头像 | [optional] 
**email** | **str** | 用户邮箱 | [optional] 
**credit** | **int** | 用户信用值，低于0将会被限制使用 | [optional] [readonly] [default to 5]
**translated** | **int** | 用户翻译的词条数量 | [optional] [readonly] 
**edited** | **int** | 用户编辑的词条数量 | [optional] [readonly] 
**reviewed** | **int** | 用户审核的词条数量 | [optional] [readonly] 
**commented** | **int** | 用户发布的评论数 | [optional] [readonly] 
**points** | **float** | 用户的贡献值（PP），计算公式为 1 * 翻译词条总词数 + 0.5 * 编辑词条总词数 + 0.2 * 审核词条总词数 | [optional] [readonly] 

## Example

```python
from paratranz_client.models.mail_from_user import MailFromUser

# TODO update the JSON string below
json = "{}"
# create an instance of MailFromUser from a JSON string
mail_from_user_instance = MailFromUser.from_json(json)
# print the JSON string representation of the object
print MailFromUser.to_json()

# convert the object into a dict
mail_from_user_dict = mail_from_user_instance.to_dict()
# create an instance of MailFromUser from a dict
mail_from_user_form_dict = mail_from_user.from_dict(mail_from_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


