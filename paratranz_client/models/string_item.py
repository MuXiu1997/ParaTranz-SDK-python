import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.stage import Stage
from ..types import UNSET, Unset

T = TypeVar("T", bound="StringItem")


@attr.s(auto_attribs=True)
class StringItem:
    """词条

    Attributes:
        id (Union[Unset, int]): 词条ID
        created_at (Union[Unset, None, datetime.datetime]):  Example: 2021-01-11T03:19:52.818Z.
        updated_at (Union[Unset, None, datetime.datetime]):  Example: 2021-01-11T03:19:52.818Z.
        key (Union[Unset, str]): 词条键值，文件内必须唯一
        original (Union[Unset, str]): 词条原文
        translation (Union[Unset, str]): 词条译文
        file (Union[Unset, int]): 词条所属的文件ID
        stage (Union[Unset, Stage]): 词条状态
              * `0` - 未翻译

              * `1` - 已翻译

              * `2` - 有疑问

              * `3` - 已检查

              * `5` - 已审核（二校）

              * `9` - 已锁定，此状态下仅管理员可解锁，词条强制按译文导出

              * `-1` - 已隐藏，此状态下词条强制按原文导出
             Default: Stage.VALUE_0.
        project (Union[Unset, int]): 词条所属项目ID
        uid (Union[Unset, int]): 词条最后编辑用户的ID
        context (Union[Unset, str]): 词条上下文，可通过上传文件或API添加
        words (Union[Unset, int]): 词条原文字数（暂不支持中日韩计数）
    """

    id: Union[Unset, int] = UNSET
    created_at: Union[Unset, None, datetime.datetime] = UNSET
    updated_at: Union[Unset, None, datetime.datetime] = UNSET
    key: Union[Unset, str] = UNSET
    original: Union[Unset, str] = UNSET
    translation: Union[Unset, str] = UNSET
    file: Union[Unset, int] = UNSET
    stage: Union[Unset, Stage] = Stage.VALUE_0
    project: Union[Unset, int] = UNSET
    uid: Union[Unset, int] = UNSET
    context: Union[Unset, str] = UNSET
    words: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat() if self.created_at else None

        updated_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat() if self.updated_at else None

        key = self.key
        original = self.original
        translation = self.translation
        file = self.file
        stage: Union[Unset, int] = UNSET
        if not isinstance(self.stage, Unset):
            stage = self.stage.value

        project = self.project
        uid = self.uid
        context = self.context
        words = self.words

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if key is not UNSET:
            field_dict["key"] = key
        if original is not UNSET:
            field_dict["original"] = original
        if translation is not UNSET:
            field_dict["translation"] = translation
        if file is not UNSET:
            field_dict["file"] = file
        if stage is not UNSET:
            field_dict["stage"] = stage
        if project is not UNSET:
            field_dict["project"] = project
        if uid is not UNSET:
            field_dict["uid"] = uid
        if context is not UNSET:
            field_dict["context"] = context
        if words is not UNSET:
            field_dict["words"] = words

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, None, datetime.datetime]
        if _created_at is None:
            created_at = None
        elif isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, None, datetime.datetime]
        if _updated_at is None:
            updated_at = None
        elif isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        key = d.pop("key", UNSET)

        original = d.pop("original", UNSET)

        translation = d.pop("translation", UNSET)

        file = d.pop("file", UNSET)

        _stage = d.pop("stage", UNSET)
        stage: Union[Unset, Stage]
        if isinstance(_stage, Unset):
            stage = UNSET
        else:
            stage = Stage(_stage)

        project = d.pop("project", UNSET)

        uid = d.pop("uid", UNSET)

        context = d.pop("context", UNSET)

        words = d.pop("words", UNSET)

        string_item = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            key=key,
            original=original,
            translation=translation,
            file=file,
            stage=stage,
            project=project,
            uid=uid,
            context=context,
            words=words,
        )

        string_item.additional_properties = d
        return string_item

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
