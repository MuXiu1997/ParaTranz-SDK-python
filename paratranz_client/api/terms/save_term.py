from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    project_id: int,
    term_id: int,
    *,
    client: Client,
    json_body: Any,
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}/terms/{termId}".format(client.base_url, projectId=project_id, termId=term_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    term_id: int,
    *,
    client: Client,
    json_body: Any,
) -> Response[Any]:
    """修改术语

     修改术语

    Args:
        project_id (int):
        term_id (int):
        json_body (Any): 术语

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        term_id=term_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    project_id: int,
    term_id: int,
    *,
    client: Client,
    json_body: Any,
) -> Response[Any]:
    """修改术语

     修改术语

    Args:
        project_id (int):
        term_id (int):
        json_body (Any): 术语

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        term_id=term_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
