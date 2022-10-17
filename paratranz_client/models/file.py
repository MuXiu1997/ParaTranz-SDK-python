import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="File")


@attr.s(auto_attribs=True)
class File:
    """文件

    Attributes:
        id (Union[Unset, int]):  Example: 421.
        created_at (Union[Unset, None, datetime.datetime]):  Example: 2021-01-11T03:19:52.818Z.
        updated_at (Union[Unset, None, datetime.datetime]):  Example: 2021-01-11T03:19:52.818Z.
        name (Union[Unset, str]):  Example: path/to/filename.csv.
        project (Union[Unset, int]):  Example: 1.
        format_ (Union[Unset, str]): 文件格式，由系统自动计算 Example: ssv.
        total (Union[Unset, int]): 文件总词条数 Example: 1453.
        translated (Union[Unset, int]): 已翻译词条数 Example: 1452.
        disputed (Union[Unset, int]): 有疑问的词条数 Example: 2.
        checked (Union[Unset, int]): 已检查的词条数 Example: 841.
        reviewed (Union[Unset, int]): 已审核的词条数 Example: 272.
        hidden (Union[Unset, int]): 已隐藏的词条数 Example: 2.
        locked (Union[Unset, int]): 已锁定的词条数 Example: 1.
        words (Union[Unset, int]): 总词数 Example: 6421.
    """

    id: Union[Unset, int] = UNSET
    created_at: Union[Unset, None, datetime.datetime] = UNSET
    updated_at: Union[Unset, None, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    project: Union[Unset, int] = UNSET
    format_: Union[Unset, str] = UNSET
    total: Union[Unset, int] = UNSET
    translated: Union[Unset, int] = UNSET
    disputed: Union[Unset, int] = UNSET
    checked: Union[Unset, int] = UNSET
    reviewed: Union[Unset, int] = UNSET
    hidden: Union[Unset, int] = UNSET
    locked: Union[Unset, int] = UNSET
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

        name = self.name
        project = self.project
        format_ = self.format_
        total = self.total
        translated = self.translated
        disputed = self.disputed
        checked = self.checked
        reviewed = self.reviewed
        hidden = self.hidden
        locked = self.locked
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
        if name is not UNSET:
            field_dict["name"] = name
        if project is not UNSET:
            field_dict["project"] = project
        if format_ is not UNSET:
            field_dict["format"] = format_
        if total is not UNSET:
            field_dict["total"] = total
        if translated is not UNSET:
            field_dict["translated"] = translated
        if disputed is not UNSET:
            field_dict["disputed"] = disputed
        if checked is not UNSET:
            field_dict["checked"] = checked
        if reviewed is not UNSET:
            field_dict["reviewed"] = reviewed
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if locked is not UNSET:
            field_dict["locked"] = locked
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

        name = d.pop("name", UNSET)

        project = d.pop("project", UNSET)

        format_ = d.pop("format", UNSET)

        total = d.pop("total", UNSET)

        translated = d.pop("translated", UNSET)

        disputed = d.pop("disputed", UNSET)

        checked = d.pop("checked", UNSET)

        reviewed = d.pop("reviewed", UNSET)

        hidden = d.pop("hidden", UNSET)

        locked = d.pop("locked", UNSET)

        words = d.pop("words", UNSET)

        file = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            project=project,
            format_=format_,
            total=total,
            translated=translated,
            disputed=disputed,
            checked=checked,
            reviewed=reviewed,
            hidden=hidden,
            locked=locked,
            words=words,
        )

        file.additional_properties = d
        return file

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
