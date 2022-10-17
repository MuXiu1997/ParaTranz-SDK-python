import datetime
from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.get_scores_operation import GetScoresOperation
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: int,
    *,
    client: Client,
    page: int = 1,
    page_size: int = 50,
    uid: Union[Unset, None, float] = UNSET,
    operation: Union[Unset, None, GetScoresOperation] = UNSET,
    start: Union[Unset, None, datetime.datetime] = UNSET,
    end: Union[Unset, None, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}/scores".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["pageSize"] = page_size

    params["uid"] = uid

    json_operation: Union[Unset, None, str] = UNSET
    if not isinstance(operation, Unset):
        json_operation = operation.value if operation else None

    params["operation"] = json_operation

    json_start: Union[Unset, None, str] = UNSET
    if not isinstance(start, Unset):
        json_start = start.isoformat() if start else None

    params["start"] = json_start

    json_end: Union[Unset, None, str] = UNSET
    if not isinstance(end, Unset):
        json_end = end.isoformat() if end else None

    params["end"] = json_end

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
    uid: Union[Unset, None, float] = UNSET,
    operation: Union[Unset, None, GetScoresOperation] = UNSET,
    start: Union[Unset, None, datetime.datetime] = UNSET,
    end: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[Any]:
    """成员贡献

     查看项目所有的贡献

    Args:
        project_id (int):
        page (int):  Default: 1.
        page_size (int):  Default: 50.
        uid (Union[Unset, None, float]):
        operation (Union[Unset, None, GetScoresOperation]):
        start (Union[Unset, None, datetime.datetime]):
        end (Union[Unset, None, datetime.datetime]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        page=page,
        page_size=page_size,
        uid=uid,
        operation=operation,
        start=start,
        end=end,
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
    uid: Union[Unset, None, float] = UNSET,
    operation: Union[Unset, None, GetScoresOperation] = UNSET,
    start: Union[Unset, None, datetime.datetime] = UNSET,
    end: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[Any]:
    """成员贡献

     查看项目所有的贡献

    Args:
        project_id (int):
        page (int):  Default: 1.
        page_size (int):  Default: 50.
        uid (Union[Unset, None, float]):
        operation (Union[Unset, None, GetScoresOperation]):
        start (Union[Unset, None, datetime.datetime]):
        end (Union[Unset, None, datetime.datetime]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        page=page,
        page_size=page_size,
        uid=uid,
        operation=operation,
        start=start,
        end=end,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
