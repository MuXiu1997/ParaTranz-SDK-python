# coding: utf-8

"""
    ParaTranz OpenAPI 文档

    本文档介绍 ParaTranz.cn 平台的 API ## 获取 Token 首先需要获取API Token，可以通过点击个人资料页面左侧的小钥匙图标获取API Token， 调用 API 时将 Token 直接放在请求头的 Authorization 中即可。  cURL 使用示例:      $ curl --header \"Authorization: XXXXXXXXX\" https://paratranz.cn/api/projects  ## 频率限制 每分钟120次调用，超出后将会降速（增加延迟），1分钟后自动恢复。 ## 错误处理 API 返回的错误格式如下      {       \"message\": \"ERROR MESSAGE\", // 错误消息       \"code\": 10000 // 5位错误代码，注意与下面的HTTP状态码区分，部分接口不返回     }  HTTP状态码有以下几种类型   * 400 - 调用参数错误   * 401 - Token 错误或过期   * 403 - 没有相关权限   * 404 - 资源不存在   * 405 - 没有相关HTTP方法，一般为调用方法错误   * 429 - 调用过于频繁，具体频率限制请看上一节   * 500 - 服务器错误，一般会提供具体出错的位置，请发送给站长方便定位问题   * 502 - 服务器无响应，部分用户被墙时可能会遇到   * 503 - 服务不可用   * 504 - 服务超时，访问量大时会出现  ## SDK 及 JSON 格式的 API 文档 本文档遵循 OpenAPI 规范，[点击此处](https://paratranz.cn/api-docs?raw=1) 获取 JSON 格式的文档，您可以使用 [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) 生成各种语言的 SDK ## 更新历史   * v0.3.5 - 2023.12.25 修复部分schema格式问题   * v0.3.4 - 2023.12.23 增加API调用频率限制说明   * v0.3.3 - 2023.08.11 增加项目成员相关接口说明   * v0.3.2 - 2022.11.04 增加文件翻译相关接口说明   * v0.3.1 - 2022.10.16 修改 tag 及 schema 以便生成 sdk   * v0.3.0 - 2022.10.16 增加术语历史记录接口说明，调整历史记录接口字段; 增加文档中 operationId 定义;                         修复项目信息相关接口格式定义; 增加 JSON 格式文档入口   * v0.2.1 - 2022.07.23 增加成员贡献接口文档; 完善列表接口数据结构   * v0.2.0 - 2022.06.15 增加讨论及私信相关接口文档   * v0.1.3 - 2022.03.10 增加历史记录相关接口文档   * v0.1.2 - 2022.02.07 完善词条搜索接口 query 参数说明   * v0.1.1 - 2022.01.17 增加文件历史相关接口文档   * v0.1.0 - 2022.01.12 初次发布 

    The version of the OpenAPI document: 0.3.4
    Contact: master@mail.paratranz.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Revision(BaseModel):
    """
    文件上传记录
    """ # noqa: E501
    id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    name: Optional[StrictStr] = Field(default=None, description="文件名")
    filename: Optional[StrictStr] = Field(default=None, description="上传文件的名称")
    type: Optional[StrictStr] = Field(default=None, description="操作方式 * create - 创建文件 * update - 更新文件 * import - 导入翻译 ")
    file: Optional[StrictInt] = Field(default=None, description="文件ID")
    uid: Optional[StrictInt] = Field(default=None, description="用户ID")
    project: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="项目ID")
    insert: Optional[StrictInt] = Field(default=None, description="新增的词条数量")
    update: Optional[StrictInt] = Field(default=None, description="更新的词条数量")
    remove: Optional[StrictInt] = Field(default=None, description="删除的词条数量")
    hash: Optional[StrictStr] = Field(default=None, description="文件内容哈希值（MD5）")
    force: Optional[StrictBool] = Field(default=None, description="是否是强制更新")
    incremental: Optional[StrictBool] = Field(default=None, description="是否是增量更新")
    __properties: ClassVar[List[str]] = ["id", "createdAt", "name", "filename", "type", "file", "uid", "project", "insert", "update", "remove", "hash", "force", "incremental"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('create', 'update', 'import'):
            raise ValueError("must be one of enum values ('create', 'update', 'import')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Revision from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "id",
                "created_at",
                "name",
                "filename",
                "uid",
                "project",
            },
            exclude_none=True,
        )
        # set to None if uid (nullable) is None
        # and model_fields_set contains the field
        if self.uid is None and "uid" in self.model_fields_set:
            _dict['uid'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Revision from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "createdAt": obj.get("createdAt"),
            "name": obj.get("name"),
            "filename": obj.get("filename"),
            "type": obj.get("type"),
            "file": obj.get("file"),
            "uid": obj.get("uid"),
            "project": obj.get("project"),
            "insert": obj.get("insert"),
            "update": obj.get("update"),
            "remove": obj.get("remove"),
            "hash": obj.get("hash"),
            "force": obj.get("force"),
            "incremental": obj.get("incremental")
        })
        return _obj


