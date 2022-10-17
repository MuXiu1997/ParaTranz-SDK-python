from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.create_file_multipart_data import CreateFileMultipartData
from ...models.create_file_response_200 import CreateFileResponse200
from ...types import Response


def _get_kwargs(
    project_id: int,
    *,
    client: Client,
    multipart_data: CreateFileMultipartData,
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}/files".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(*, response: httpx.Response) -> Optional[CreateFileResponse200]:
    if response.status_code == 200:
        response_200 = CreateFileResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CreateFileResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    project_id: int,
    *,
    client: Client,
    multipart_data: CreateFileMultipartData,
) -> Response[CreateFileResponse200]:
    """上传文件

     上传并创建文件，文件名不能与 path 指定的目录中的文件冲突

    Args:
        project_id (int):
        multipart_data (CreateFileMultipartData):

    Returns:
        Response[CreateFileResponse200]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    project_id: int,
    *,
    client: Client,
    multipart_data: CreateFileMultipartData,
) -> Optional[CreateFileResponse200]:
    """上传文件

     上传并创建文件，文件名不能与 path 指定的目录中的文件冲突

    Args:
        project_id (int):
        multipart_data (CreateFileMultipartData):

    Returns:
        Response[CreateFileResponse200]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    *,
    client: Client,
    multipart_data: CreateFileMultipartData,
) -> Response[CreateFileResponse200]:
    """上传文件

     上传并创建文件，文件名不能与 path 指定的目录中的文件冲突

    Args:
        project_id (int):
        multipart_data (CreateFileMultipartData):

    Returns:
        Response[CreateFileResponse200]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    project_id: int,
    *,
    client: Client,
    multipart_data: CreateFileMultipartData,
) -> Optional[CreateFileResponse200]:
    """上传文件

     上传并创建文件，文件名不能与 path 指定的目录中的文件冲突

    Args:
        project_id (int):
        multipart_data (CreateFileMultipartData):

    Returns:
        Response[CreateFileResponse200]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
