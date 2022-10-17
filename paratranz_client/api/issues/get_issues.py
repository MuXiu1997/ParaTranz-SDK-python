from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.get_issues_status import GetIssuesStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: int,
    *,
    client: Client,
    status: Union[Unset, None, GetIssuesStatus] = UNSET,
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}/issues".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_status: Union[Unset, None, int] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

    params["status"] = json_status

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
    status: Union[Unset, None, GetIssuesStatus] = UNSET,
) -> Response[Any]:
    """讨论列表

     获取讨论列表

    Args:
        project_id (int):
        status (Union[Unset, None, GetIssuesStatus]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        status=status,
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
    status: Union[Unset, None, GetIssuesStatus] = UNSET,
) -> Response[Any]:
    """讨论列表

     获取讨论列表

    Args:
        project_id (int):
        status (Union[Unset, None, GetIssuesStatus]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        status=status,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
