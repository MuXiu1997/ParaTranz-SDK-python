# Mail

私信

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**var_from** | **int** | 用户ID | [optional] [readonly] 
**from_user** | [**MailFromUser**](MailFromUser.md) |  | [optional] 
**to** | **int** | 用户ID | [optional] [readonly] 
**to_user** | [**MailFromUser**](MailFromUser.md) |  | [optional] 
**content** | **str** | 原始内容（markdown） | [optional] 
**html** | **str** | content 的 markdown 转换之后的 html | [optional] [readonly] 
**status** | **int** | 私信的状态，0 - 未读，1 - 已读 | [optional] 

## Example

```python
from paratranz_client.models.mail import Mail

# TODO update the JSON string below
json = "{}"
# create an instance of Mail from a JSON string
mail_instance = Mail.from_json(json)
# print the JSON string representation of the object
print Mail.to_json()

# convert the object into a dict
mail_dict = mail_instance.to_dict()
# create an instance of Mail from a dict
mail_form_dict = mail.from_dict(mail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


