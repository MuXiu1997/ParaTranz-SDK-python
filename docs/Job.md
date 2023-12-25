# Job

导出任务信息

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**started_at** | **datetime** |  | [optional] [readonly] 
**finished_at** | **datetime** |  | [optional] [readonly] 
**scheduled_at** | **datetime** |  | [optional] [readonly] 
**params** | **object** | 任务执行参数 | [optional] 
**project** | **int** | 项目ID | [optional] [readonly] 
**uid** | **int** | 创建者用户ID | [optional] 
**type** | **str** | 任务类型 | [optional] 
**status** | **int** | 任务状态，0 - 未开始，1 - 正在执行，2 - 执行成功，-1 - 执行失败 | [optional] 
**result** | **object** | 任务结果 | [optional] 

## Example

```python
from paratranz_client.models.job import Job

# TODO update the JSON string below
json = "{}"
# create an instance of Job from a JSON string
job_instance = Job.from_json(json)
# print the JSON string representation of the object
print Job.to_json()

# convert the object into a dict
job_dict = job_instance.to_dict()
# create an instance of Job from a dict
job_form_dict = job.from_dict(job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


