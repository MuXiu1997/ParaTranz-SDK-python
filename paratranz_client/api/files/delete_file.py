from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    project_id: int,
    file_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}/files/{fileId}".format(client.base_url, projectId=project_id, fileId=file_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
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
    file_id: int,
    *,
    client: Client,
) -> Response[Any]:
    """删除文件

     通过ID删除文件

    Args:
        project_id (int):
        file_id (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        file_id=file_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    project_id: int,
    file_id: int,
    *,
    client: Client,
) -> Response[Any]:
    """删除文件

     通过ID删除文件

    Args:
        project_id (int):
        file_id (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        file_id=file_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
