# Score

贡献

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**project** | **int** | 项目ID | [optional] [readonly] 
**uid** | **int** | 用户ID | [optional] [readonly] 
**base** | **int** | 贡献值基准，翻译为1，编辑为0.5，审核为0.2 | [optional] [readonly] 
**multiplier** | **int** | 贡献值乘数，公式为 1 + (词数 - 1) * 0.1 | [optional] 
**value** | **int** | 基准乘以乘数得到的最终值 | [optional] 

## Example

```python
from paratranz_client.models.score import Score

# TODO update the JSON string below
json = "{}"
# create an instance of Score from a JSON string
score_instance = Score.from_json(json)
# print the JSON string representation of the object
print Score.to_json()

# convert the object into a dict
score_dict = score_instance.to_dict()
# create an instance of Score from a dict
score_form_dict = score.from_dict(score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


