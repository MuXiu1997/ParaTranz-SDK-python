from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.file import File
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateFileResponse200")


@attr.s(auto_attribs=True)
class CreateFileResponse200:
    """
    Attributes:
        file (Union[Unset, File]): 文件
        revision (Union[Unset, Any]): 文件上传记录
    """

    file: Union[Unset, File] = UNSET
    revision: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        revision = self.revision

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file is not UNSET:
            field_dict["file"] = file
        if revision is not UNSET:
            field_dict["revision"] = revision

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _file = d.pop("file", UNSET)
        file: Union[Unset, File]
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = File.from_dict(_file)

        revision = d.pop("revision", UNSET)

        create_file_response_200 = cls(
            file=file,
            revision=revision,
        )

        create_file_response_200.additional_properties = d
        return create_file_response_200

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
