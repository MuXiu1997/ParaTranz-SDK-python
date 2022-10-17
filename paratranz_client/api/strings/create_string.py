from typing import Any, Dict

import httpx

from ...client import Client
from ...models.string_item import StringItem
from ...types import UNSET, Response


def _get_kwargs(
    project_id: int,
    *,
    client: Client,
    json_body: StringItem,
    page: int = 1,
    page_size: int = 50,
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}/strings".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    json_body: StringItem,
    page: int = 1,
    page_size: int = 50,
) -> Response[Any]:
    """创建词条

     创建词条

    Args:
        project_id (int):
        page (int):  Default: 1.
        page_size (int):  Default: 50.
        json_body (StringItem): 词条

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        json_body=json_body,
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
    json_body: StringItem,
    page: int = 1,
    page_size: int = 50,
) -> Response[Any]:
    """创建词条

     创建词条

    Args:
        project_id (int):
        page (int):  Default: 1.
        page_size (int):  Default: 50.
        json_body (StringItem): 词条

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        json_body=json_body,
        page=page,
        page_size=page_size,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
