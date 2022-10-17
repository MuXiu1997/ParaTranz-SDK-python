# paratranz_client.model.stage.Stage

词条状态   * `0` - 未翻译    * `1` - 已翻译    * `2` - 有疑问    * `3` - 已检查    * `5` - 已审核（二校）    * `9` - 已锁定，此状态下仅管理员可解锁，词条强制按译文导出    * `-1` - 已隐藏，此状态下词条强制按原文导出 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | 词条状态   * &#x60;0&#x60; - 未翻译    * &#x60;1&#x60; - 已翻译    * &#x60;2&#x60; - 有疑问    * &#x60;3&#x60; - 已检查    * &#x60;5&#x60; - 已审核（二校）    * &#x60;9&#x60; - 已锁定，此状态下仅管理员可解锁，词条强制按译文导出    * &#x60;-1&#x60; - 已隐藏，此状态下词条强制按原文导出  | must be one of [0, 1, 2, 3, 5, 9, -1, ] if omitted the server will use the default value of 0

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

