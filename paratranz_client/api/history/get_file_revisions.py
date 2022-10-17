from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.get_file_revisions_type import GetFileRevisionsType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: int,
    *,
    client: Client,
    page: int = 1,
    page_size: int = 50,
    file: Union[Unset, None, float] = UNSET,
    type: Union[Unset, None, GetFileRevisionsType] = UNSET,
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}/files/revisions".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["pageSize"] = page_size

    params["file"] = file

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
    project_id: int,
    *,
    client: Client,
    page: int = 1,
    page_size: int = 50,
    file: Union[Unset, None, float] = UNSET,
    type: Union[Unset, None, GetFileRevisionsType] = UNSET,
) -> Response[Any]:
    """文件历史

     查看项目所有文件上传、更新及删除历史

    Args:
        project_id (int):
        page (int):  Default: 1.
        page_size (int):  Default: 50.
        file (Union[Unset, None, float]):
        type (Union[Unset, None, GetFileRevisionsType]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        page=page,
        page_size=page_size,
        file=file,
        type=type,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    project_id: int,
    *,
    client: Client,
    page: int = 1,
    page_size: int = 50,
    file: Union[Unset, None, float] = UNSET,
    type: Union[Unset, None, GetFileRevisionsType] = UNSET,
) -> Response[Any]:
    """文件历史

     查看项目所有文件上传、更新及删除历史

    Args:
        project_id (int):
        page (int):  Default: 1.
        page_size (int):  Default: 50.
        file (Union[Unset, None, float]):
        type (Union[Unset, None, GetFileRevisionsType]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        page=page,
        page_size=page_size,
        file=file,
        type=type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
