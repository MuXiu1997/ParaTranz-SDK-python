from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    user_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/mails/conversations/{userId}".format(client.base_url, userId=user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
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
    user_id: int,
    *,
    client: Client,
) -> Response[Any]:
    """用户对话

     通过用户ID获取与某用户的对话

    Args:
        user_id (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    user_id: int,
    *,
    client: Client,
) -> Response[Any]:
    """用户对话

     通过用户ID获取与某用户的对话

    Args:
        user_id (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
