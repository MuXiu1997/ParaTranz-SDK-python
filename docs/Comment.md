# Comment

评论

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**uid** | **int** |  | [optional] [readonly] 
**project** | **int** |  | [optional] 
**type** | **str** | 评论的相关条目类型 | [optional] 
**tid** | **int** | 条目ID | [optional] 
**content** | **str** | 评论内容，markdown 原始数据 | [optional] 
**html** | **str** | markdown 转换后的 html 数据 | [optional] [readonly] 
**images** | **List[str]** | 图片链接列表 | [optional] 
**reply_to** | **int** | 回复的评论ID | [optional] 
**refer** | **List[int]** | 评论中@的用户ID列表 | [optional] [readonly] 

## Example

```python
from paratranz_client.models.comment import Comment

# TODO update the JSON string below
json = "{}"
# create an instance of Comment from a JSON string
comment_instance = Comment.from_json(json)
# print the JSON string representation of the object
print Comment.to_json()

# convert the object into a dict
comment_dict = comment_instance.to_dict()
# create an instance of Comment from a dict
comment_form_dict = comment.from_dict(comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


