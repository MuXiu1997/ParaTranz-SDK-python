# OperateIssueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | 操作类型，回复为 &#x60;reply&#x60;，订阅为 &#x60;subscribe&#x60;，取消订阅为 &#x60;unsubscribe&#x60; | 
**content** | **str** | 回复内容，支持markdown，仅 op 为 reply 时需要传入 | [optional] 

## Example

```python
from paratranz_client.models.operate_issue_request import OperateIssueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OperateIssueRequest from a JSON string
operate_issue_request_instance = OperateIssueRequest.from_json(json)
# print the JSON string representation of the object
print OperateIssueRequest.to_json()

# convert the object into a dict
operate_issue_request_dict = operate_issue_request_instance.to_dict()
# create an instance of OperateIssueRequest from a dict
operate_issue_request_form_dict = operate_issue_request.from_dict(operate_issue_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


