import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@attr.s(auto_attribs=True)
class User:
    """用户

    Attributes:
        id (Union[Unset, int]):  Example: 1001.
        created_at (Union[Unset, None, datetime.datetime]):  Example: 2021-01-11T03:19:52.818Z.
        updated_at (Union[Unset, None, datetime.datetime]):  Example: 2021-01-11T03:19:52.818Z.
        last_visit (Union[Unset, datetime.datetime]):  Example: 2021-01-11T03:19:52.818Z.
        username (Union[Unset, str]): 用户名 Example: bruceczk.
        nickname (Union[Unset, str]): 用户昵称 Example: 机智的布鲁斯.
        bio (Union[Unset, str]): 用户简介 Example: 是站长.
        avatar (Union[Unset, str]): 用户头像
        email (Union[Unset, str]): 用户邮箱
        credit (Union[Unset, int]): 用户信用值，低于0将会被限制使用 Default: 5.
        translated (Union[Unset, int]): 用户翻译的词条数量
        edited (Union[Unset, int]): 用户编辑的词条数量
        reviewed (Union[Unset, int]): 用户审核的词条数量
        commented (Union[Unset, int]): 用户发布的评论数
        points (Union[Unset, float]): 用户的贡献值（PP），计算公式为
            1 * 翻译词条总词数 + 0.5 * 编辑词条总词数 + 0.2 * 审核词条总词数
    """

    id: Union[Unset, int] = UNSET
    created_at: Union[Unset, None, datetime.datetime] = UNSET
    updated_at: Union[Unset, None, datetime.datetime] = UNSET
    last_visit: Union[Unset, datetime.datetime] = UNSET
    username: Union[Unset, str] = UNSET
    nickname: Union[Unset, str] = UNSET
    bio: Union[Unset, str] = UNSET
    avatar: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    credit: Union[Unset, int] = 5
    translated: Union[Unset, int] = UNSET
    edited: Union[Unset, int] = UNSET
    reviewed: Union[Unset, int] = UNSET
    commented: Union[Unset, int] = UNSET
    points: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat() if self.created_at else None

        updated_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat() if self.updated_at else None

        last_visit: Union[Unset, str] = UNSET
        if not isinstance(self.last_visit, Unset):
            last_visit = self.last_visit.isoformat()

        username = self.username
        nickname = self.nickname
        bio = self.bio
        avatar = self.avatar
        email = self.email
        credit = self.credit
        translated = self.translated
        edited = self.edited
        reviewed = self.reviewed
        commented = self.commented
        points = self.points

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if last_visit is not UNSET:
            field_dict["lastVisit"] = last_visit
        if username is not UNSET:
            field_dict["username"] = username
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if bio is not UNSET:
            field_dict["bio"] = bio
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if email is not UNSET:
            field_dict["email"] = email
        if credit is not UNSET:
            field_dict["credit"] = credit
        if translated is not UNSET:
            field_dict["translated"] = translated
        if edited is not UNSET:
            field_dict["edited"] = edited
        if reviewed is not UNSET:
            field_dict["reviewed"] = reviewed
        if commented is not UNSET:
            field_dict["commented"] = commented
        if points is not UNSET:
            field_dict["points"] = points

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

        _last_visit = d.pop("lastVisit", UNSET)
        last_visit: Union[Unset, datetime.datetime]
        if isinstance(_last_visit, Unset):
            last_visit = UNSET
        else:
            last_visit = isoparse(_last_visit)

        username = d.pop("username", UNSET)

        nickname = d.pop("nickname", UNSET)

        bio = d.pop("bio", UNSET)

        avatar = d.pop("avatar", UNSET)

        email = d.pop("email", UNSET)

        credit = d.pop("credit", UNSET)

        translated = d.pop("translated", UNSET)

        edited = d.pop("edited", UNSET)

        reviewed = d.pop("reviewed", UNSET)

        commented = d.pop("commented", UNSET)

        points = d.pop("points", UNSET)

        user = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            last_visit=last_visit,
            username=username,
            nickname=nickname,
            bio=bio,
            avatar=avatar,
            email=email,
            credit=credit,
            translated=translated,
            edited=edited,
            reviewed=reviewed,
            commented=commented,
            points=points,
        )

        user.additional_properties = d
        return user

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
