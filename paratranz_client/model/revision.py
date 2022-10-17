# coding: utf-8

"""
    ParaTranz OpenAPI 文档

    本文档介绍 ParaTranz.cn 平台的 API ## 获取 Token 首先需要获取API Token，可以通过点击个人资料页面左侧的小钥匙图标获取API Token， 调用 API 时将 Token 直接放在请求头的 Authorization 中即可。  cURL 使用示例:      $ curl --header \"Authorization: XXXXXXXXX\" https://paratranz.cn/api/projects  ## 错误处理 API 返回的错误格式如下      {       \"message\": \"ERROR MESSAGE\", // 错误消息       \"code\": 10000 // 5位错误代码，注意与下面的HTTP状态码区分，部分接口不返回     }  HTTP状态码有以下几种类型   * 400 - 调用参数错误   * 401 - Token 错误或过期   * 403 - 没有相关权限   * 404 - 资源不存在   * 405 - 没有相关HTTP方法，一般为调用方法错误   * 500 - 服务器错误，一般会提供具体出错的位置，请发送给站长方便定位问题   * 502 - 服务器无响应，部分用户被墙时可能会遇到   * 503 - 服务不可用   * 504 - 服务超时，访问量大时会出现  ## 获取 JSON 格式的 API 文档 本文档遵循 OpenAPI 规范，如果您希望获取 JSON 格式的文档，可[点击此处](/api-docs?raw=1) ## 更新历史   * v0.3.1 - 2022.10.17 更改 tag 为英语，便于生成 SDK   * v0.3.0 - 2022.10.16 增加术语历史记录接口说明，调整历史记录接口字段; 增加文档中 operationId 定义;                         修复项目信息相关接口格式定义; 增加 JSON 格式文档入口   * v0.2.1 - 2022.07.23 增加成员贡献接口文档; 完善列表接口数据结构   * v0.2.0 - 2022.06.15 增加讨论及私信相关接口文档   * v0.1.3 - 2022.03.10 增加历史记录相关接口文档   * v0.1.2 - 2022.02.07 完善词条搜索接口 query 参数说明   * v0.1.1 - 2022.01.17 增加文件历史相关接口文档   * v0.1.0 - 2022.01.12 初次发布   # noqa: E501

    The version of the OpenAPI document: 0.3.1
    Contact: master@mail.paratranz.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from paratranz_client import schemas  # noqa: F401


class Revision(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    文件上传记录
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def id() -> typing.Type['Id']:
                return Id
            createdAt = schemas.DateTimeSchema
            name = schemas.StrSchema
            filename = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "create": "CREATE",
                        "update": "UPDATE",
                        "import": "IMPORT",
                    }
                
                @schemas.classproperty
                def CREATE(cls):
                    return cls("create")
                
                @schemas.classproperty
                def UPDATE(cls):
                    return cls("update")
                
                @schemas.classproperty
                def IMPORT(cls):
                    return cls("import")
            file = schemas.IntSchema
        
            @staticmethod
            def uid() -> typing.Type['UserId']:
                return UserId
        
            @staticmethod
            def project() -> typing.Type['ProjectId']:
                return ProjectId
            insert = schemas.IntSchema
            update = schemas.IntSchema
            remove = schemas.IntSchema
            hash = schemas.StrSchema
            force = schemas.BoolSchema
            incremental = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "createdAt": createdAt,
                "name": name,
                "filename": filename,
                "type": type,
                "file": file,
                "uid": uid,
                "project": project,
                "insert": insert,
                "update": update,
                "remove": remove,
                "hash": hash,
                "force": force,
                "incremental": incremental,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'Id': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filename"]) -> MetaOapg.properties.filename: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file"]) -> MetaOapg.properties.file: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uid"]) -> 'UserId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["project"]) -> 'ProjectId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["insert"]) -> MetaOapg.properties.insert: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["update"]) -> MetaOapg.properties.update: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["remove"]) -> MetaOapg.properties.remove: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hash"]) -> MetaOapg.properties.hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["force"]) -> MetaOapg.properties.force: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["incremental"]) -> MetaOapg.properties.incremental: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "createdAt", "name", "filename", "type", "file", "uid", "project", "insert", "update", "remove", "hash", "force", "incremental", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union['Id', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> typing.Union[MetaOapg.properties.createdAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filename"]) -> typing.Union[MetaOapg.properties.filename, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file"]) -> typing.Union[MetaOapg.properties.file, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uid"]) -> typing.Union['UserId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["project"]) -> typing.Union['ProjectId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["insert"]) -> typing.Union[MetaOapg.properties.insert, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["update"]) -> typing.Union[MetaOapg.properties.update, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["remove"]) -> typing.Union[MetaOapg.properties.remove, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hash"]) -> typing.Union[MetaOapg.properties.hash, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["force"]) -> typing.Union[MetaOapg.properties.force, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["incremental"]) -> typing.Union[MetaOapg.properties.incremental, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "createdAt", "name", "filename", "type", "file", "uid", "project", "insert", "update", "remove", "hash", "force", "incremental", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        id: typing.Union['Id', schemas.Unset] = schemas.unset,
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, datetime, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        filename: typing.Union[MetaOapg.properties.filename, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        file: typing.Union[MetaOapg.properties.file, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        uid: typing.Union['UserId', schemas.Unset] = schemas.unset,
        project: typing.Union['ProjectId', schemas.Unset] = schemas.unset,
        insert: typing.Union[MetaOapg.properties.insert, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        update: typing.Union[MetaOapg.properties.update, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        remove: typing.Union[MetaOapg.properties.remove, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        hash: typing.Union[MetaOapg.properties.hash, str, schemas.Unset] = schemas.unset,
        force: typing.Union[MetaOapg.properties.force, bool, schemas.Unset] = schemas.unset,
        incremental: typing.Union[MetaOapg.properties.incremental, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Revision':
        return super().__new__(
            cls,
            *args,
            id=id,
            createdAt=createdAt,
            name=name,
            filename=filename,
            type=type,
            file=file,
            uid=uid,
            project=project,
            insert=insert,
            update=update,
            remove=remove,
            hash=hash,
            force=force,
            incremental=incremental,
            _configuration=_configuration,
            **kwargs,
        )

from paratranz_client.model.id import Id
from paratranz_client.model.project_id import ProjectId
from paratranz_client.model.user_id import UserId
