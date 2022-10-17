import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Project")


@attr.s(auto_attribs=True)
class Project:
    """项目

    Attributes:
        id (Union[Unset, int]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        uid (Union[Unset, int]): 所有者用户ID
        name (Union[Unset, str]):
        logo (Union[Unset, str]):
        desc (Union[Unset, str]):
        source (Union[Unset, str]): 源语言
        dest (Union[Unset, str]): 目标语言
        members (Union[Unset, int]): 成员数量
        game (Union[Unset, int]): 所属游戏
        license_ (Union[Unset, str]): 项目使用的许可证
        active_level (Union[Unset, float]): 项目活跃度
        stage (Union[Unset, int]): 项目状态
        privacy (Union[Unset, int]): 项目隐私状态 * 0 - 公开 * 1 - 内部（项目公开但动态及文件私密） * 2 - 私密
        download (Union[Unset, int]): 下载权限 * 0 - 公开 * 1 - 内部 * 2 - 私密
        issue_mode (Union[Unset, int]): 讨论权限 * 0 - 公开（所有用户都可以创建及加入讨论） * 1 - 内部（仅项目成员可以创建讨论但所有用户都可以加入） * 2 -
            私密（仅项目成员可以创建及加入讨论）
        review_mode (Union[Unset, int]): 校对等级 * 0 - 无须校对 * 1 - 一次校对 * 2 - 二次校对
        join_mode (Union[Unset, int]): 加入方式 * 0 - 公开（所有用户都可以直接加入项目） * 1 - 申请（加入项目需提交申请） * 2 - 测试（加入项目需完成测试） * 3 -
            私密（仅管理员可添加成员）
    """

    id: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    uid: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    logo: Union[Unset, str] = UNSET
    desc: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    dest: Union[Unset, str] = UNSET
    members: Union[Unset, int] = UNSET
    game: Union[Unset, int] = UNSET
    license_: Union[Unset, str] = UNSET
    active_level: Union[Unset, float] = UNSET
    stage: Union[Unset, int] = UNSET
    privacy: Union[Unset, int] = UNSET
    download: Union[Unset, int] = UNSET
    issue_mode: Union[Unset, int] = UNSET
    review_mode: Union[Unset, int] = UNSET
    join_mode: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        uid = self.uid
        name = self.name
        logo = self.logo
        desc = self.desc
        source = self.source
        dest = self.dest
        members = self.members
        game = self.game
        license_ = self.license_
        active_level = self.active_level
        stage = self.stage
        privacy = self.privacy
        download = self.download
        issue_mode = self.issue_mode
        review_mode = self.review_mode
        join_mode = self.join_mode

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if uid is not UNSET:
            field_dict["uid"] = uid
        if name is not UNSET:
            field_dict["name"] = name
        if logo is not UNSET:
            field_dict["logo"] = logo
        if desc is not UNSET:
            field_dict["desc"] = desc
        if source is not UNSET:
            field_dict["source"] = source
        if dest is not UNSET:
            field_dict["dest"] = dest
        if members is not UNSET:
            field_dict["members"] = members
        if game is not UNSET:
            field_dict["game"] = game
        if license_ is not UNSET:
            field_dict["license"] = license_
        if active_level is not UNSET:
            field_dict["activeLevel"] = active_level
        if stage is not UNSET:
            field_dict["stage"] = stage
        if privacy is not UNSET:
            field_dict["privacy"] = privacy
        if download is not UNSET:
            field_dict["download"] = download
        if issue_mode is not UNSET:
            field_dict["issueMode"] = issue_mode
        if review_mode is not UNSET:
            field_dict["reviewMode"] = review_mode
        if join_mode is not UNSET:
            field_dict["joinMode"] = join_mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        uid = d.pop("uid", UNSET)

        name = d.pop("name", UNSET)

        logo = d.pop("logo", UNSET)

        desc = d.pop("desc", UNSET)

        source = d.pop("source", UNSET)

        dest = d.pop("dest", UNSET)

        members = d.pop("members", UNSET)

        game = d.pop("game", UNSET)

        license_ = d.pop("license", UNSET)

        active_level = d.pop("activeLevel", UNSET)

        stage = d.pop("stage", UNSET)

        privacy = d.pop("privacy", UNSET)

        download = d.pop("download", UNSET)

        issue_mode = d.pop("issueMode", UNSET)

        review_mode = d.pop("reviewMode", UNSET)

        join_mode = d.pop("joinMode", UNSET)

        project = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            uid=uid,
            name=name,
            logo=logo,
            desc=desc,
            source=source,
            dest=dest,
            members=members,
            game=game,
            license_=license_,
            active_level=active_level,
            stage=stage,
            privacy=privacy,
            download=download,
            issue_mode=issue_mode,
            review_mode=review_mode,
            join_mode=join_mode,
        )

        project.additional_properties = d
        return project

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
