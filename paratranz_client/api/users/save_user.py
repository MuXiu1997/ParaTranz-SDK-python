from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.save_user_json_body import SaveUserJsonBody
from ...models.user import User
from ...types import Response


def _get_kwargs(
    user_id: int,
    *,
    client: Client,
    json_body: SaveUserJsonBody,
) -> Dict[str, Any]:
    url = "{}/users/{userId}".format(client.base_url, userId=user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[User]:
    if response.status_code == 200:
        response_200 = User.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[User]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    user_id: int,
    *,
    client: Client,
    json_body: SaveUserJsonBody,
) -> Response[User]:
    """更新用户

     更改用户信息（仅支持修改自己的信息）

    Args:
        user_id (int):
        json_body (SaveUserJsonBody):

    Returns:
        Response[User]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_id: int,
    *,
    client: Client,
    json_body: SaveUserJsonBody,
) -> Optional[User]:
    """更新用户

     更改用户信息（仅支持修改自己的信息）

    Args:
        user_id (int):
        json_body (SaveUserJsonBody):

    Returns:
        Response[User]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: Client,
    json_body: SaveUserJsonBody,
) -> Response[User]:
    """更新用户

     更改用户信息（仅支持修改自己的信息）

    Args:
        user_id (int):
        json_body (SaveUserJsonBody):

    Returns:
        Response[User]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: int,
    *,
    client: Client,
    json_body: SaveUserJsonBody,
) -> Optional[User]:
    """更新用户

     更改用户信息（仅支持修改自己的信息）

    Args:
        user_id (int):
        json_body (SaveUserJsonBody):

    Returns:
        Response[User]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
