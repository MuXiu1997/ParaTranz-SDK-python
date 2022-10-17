from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.get_history_type import GetHistoryType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page: int = 1,
    page_size: int = 50,
    project: Union[Unset, None, int] = UNSET,
    uid: Union[Unset, None, int] = UNSET,
    tid: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, GetHistoryType] = UNSET,
) -> Dict[str, Any]:
    url = "{}/history".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["pageSize"] = page_size

    params["project"] = project

    params["uid"] = uid

    params["tid"] = tid

    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value if type else None

    params["type"] = json_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: Client,
    page: int = 1,
    page_size: int = 50,
    project: Union[Unset, None, int] = UNSET,
    uid: Union[Unset, None, int] = UNSET,
    tid: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, GetHistoryType] = UNSET,
) -> Response[Any]:
    """获取历史记录

     获取项目或用户的历史记录，project、uid 与 tid 必须有一个存在，否则会返回 400

    Args:
        page (int):  Default: 1.
        page_size (int):  Default: 50.
        project (Union[Unset, None, int]):
        uid (Union[Unset, None, int]):
        tid (Union[Unset, None, int]):
        type (Union[Unset, None, GetHistoryType]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        page_size=page_size,
        project=project,
        uid=uid,
        tid=tid,
        type=type,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    page: int = 1,
    page_size: int = 50,
    project: Union[Unset, None, int] = UNSET,
    uid: Union[Unset, None, int] = UNSET,
    tid: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, GetHistoryType] = UNSET,
) -> Response[Any]:
    """获取历史记录

     获取项目或用户的历史记录，project、uid 与 tid 必须有一个存在，否则会返回 400

    Args:
        page (int):  Default: 1.
        page_size (int):  Default: 50.
        project (Union[Unset, None, int]):
        uid (Union[Unset, None, int]):
        tid (Union[Unset, None, int]):
        type (Union[Unset, None, GetHistoryType]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        page_size=page_size,
        project=project,
        uid=uid,
        tid=tid,
        type=type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
