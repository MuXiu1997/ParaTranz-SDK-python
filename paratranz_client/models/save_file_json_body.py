from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.save_file_json_body_extra import SaveFileJsonBodyExtra
from ..types import UNSET, Unset

T = TypeVar("T", bound="SaveFileJsonBody")


@attr.s(auto_attribs=True)
class SaveFileJsonBody:
    """
    Attributes:
        name (Union[Unset, str]): 文件名，需填写完整路径
        extra (Union[Unset, SaveFileJsonBodyExtra]): JSON 格式，可随意填写需要的保存的其他信息
    """

    name: Union[Unset, str] = UNSET
    extra: Union[Unset, SaveFileJsonBodyExtra] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        extra: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.extra, Unset):
            extra = self.extra.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if extra is not UNSET:
            field_dict["extra"] = extra

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _extra = d.pop("extra", UNSET)
        extra: Union[Unset, SaveFileJsonBodyExtra]
        if isinstance(_extra, Unset):
            extra = UNSET
        else:
            extra = SaveFileJsonBodyExtra.from_dict(_extra)

        save_file_json_body = cls(
            name=name,
            extra=extra,
        )

        save_file_json_body.additional_properties = d
        return save_file_json_body

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
