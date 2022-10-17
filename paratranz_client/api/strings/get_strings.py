from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: int,
    *,
    client: Client,
    file: Union[Unset, None, int] = UNSET,
    stage: Union[Unset, None, int] = UNSET,
    page: int = 1,
    page_size: int = 50,
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}/strings".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["file"] = file

    params["stage"] = stage

    params["page"] = page

    params["pageSize"] = page_size

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
    file: Union[Unset, None, int] = UNSET,
    stage: Union[Unset, None, int] = UNSET,
    page: int = 1,
    page_size: int = 50,
) -> Response[Any]:
    """词条列表

     获取项目词条

    Args:
        project_id (int):
        file (Union[Unset, None, int]):
        stage (Union[Unset, None, int]):
        page (int):  Default: 1.
        page_size (int):  Default: 50.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        file=file,
        stage=stage,
        page=page,
        page_size=page_size,
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
    file: Union[Unset, None, int] = UNSET,
    stage: Union[Unset, None, int] = UNSET,
    page: int = 1,
    page_size: int = 50,
) -> Response[Any]:
    """词条列表

     获取项目词条

    Args:
        project_id (int):
        file (Union[Unset, None, int]):
        stage (Union[Unset, None, int]):
        page (int):  Default: 1.
        page_size (int):  Default: 50.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        file=file,
        stage=stage,
        page=page,
        page_size=page_size,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
