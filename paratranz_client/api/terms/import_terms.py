from typing import Any, Dict

import httpx

from ...client import Client
from ...models.import_terms_multipart_data import ImportTermsMultipartData
from ...types import UNSET, Response


def _get_kwargs(
    project_id: int,
    *,
    client: Client,
    multipart_data: ImportTermsMultipartData,
    page: int = 1,
    page_size: int = 50,
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}/terms".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
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
    multipart_data: ImportTermsMultipartData,
    page: int = 1,
    page_size: int = 50,
) -> Response[Any]:
    """批量导入术语

     上传JSON文件批量导入术语

    Args:
        project_id (int):
        page (int):  Default: 1.
        page_size (int):  Default: 50.
        multipart_data (ImportTermsMultipartData):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        multipart_data=multipart_data,
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
    multipart_data: ImportTermsMultipartData,
    page: int = 1,
    page_size: int = 50,
) -> Response[Any]:
    """批量导入术语

     上传JSON文件批量导入术语

    Args:
        project_id (int):
        page (int):  Default: 1.
        page_size (int):  Default: 50.
        multipart_data (ImportTermsMultipartData):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        multipart_data=multipart_data,
        page=page,
        page_size=page_size,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
