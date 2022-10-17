from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SaveUserJsonBody")


@attr.s(auto_attribs=True)
class SaveUserJsonBody:
    """
    Attributes:
        nickname (Union[Unset, str]):  Example: 机智的布鲁斯.
        bio (Union[Unset, str]): 个人介绍 Example: 24岁，是站长.
        avatar (Union[Unset, str]): 头像图片链接 Example: https://static.paratranz.cn/media/xxxxxaaaaabbbbb.
    """

    nickname: Union[Unset, str] = UNSET
    bio: Union[Unset, str] = UNSET
    avatar: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nickname = self.nickname
        bio = self.bio
        avatar = self.avatar

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if bio is not UNSET:
            field_dict["bio"] = bio
        if avatar is not UNSET:
            field_dict["avatar"] = avatar

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nickname = d.pop("nickname", UNSET)

        bio = d.pop("bio", UNSET)

        avatar = d.pop("avatar", UNSET)

        save_user_json_body = cls(
            nickname=nickname,
            bio=bio,
            avatar=avatar,
        )

        save_user_json_body.additional_properties = d
        return save_user_json_body

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
