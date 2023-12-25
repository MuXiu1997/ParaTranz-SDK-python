# coding: utf-8

"""
    ParaTranz OpenAPI 文档

    本文档介绍 ParaTranz.cn 平台的 API ## 获取 Token 首先需要获取API Token，可以通过点击个人资料页面左侧的小钥匙图标获取API Token， 调用 API 时将 Token 直接放在请求头的 Authorization 中即可。  cURL 使用示例:      $ curl --header \"Authorization: XXXXXXXXX\" https://paratranz.cn/api/projects  ## 频率限制 每分钟120次调用，超出后将会降速（增加延迟），1分钟后自动恢复。 ## 错误处理 API 返回的错误格式如下      {       \"message\": \"ERROR MESSAGE\", // 错误消息       \"code\": 10000 // 5位错误代码，注意与下面的HTTP状态码区分，部分接口不返回     }  HTTP状态码有以下几种类型   * 400 - 调用参数错误   * 401 - Token 错误或过期   * 403 - 没有相关权限   * 404 - 资源不存在   * 405 - 没有相关HTTP方法，一般为调用方法错误   * 429 - 调用过于频繁，具体频率限制请看上一节   * 500 - 服务器错误，一般会提供具体出错的位置，请发送给站长方便定位问题   * 502 - 服务器无响应，部分用户被墙时可能会遇到   * 503 - 服务不可用   * 504 - 服务超时，访问量大时会出现  ## SDK 及 JSON 格式的 API 文档 本文档遵循 OpenAPI 规范，[点击此处](https://paratranz.cn/api-docs?raw=1) 获取 JSON 格式的文档，您可以使用 [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) 生成各种语言的 SDK ## 更新历史   * v0.3.5 - 2023.12.25 修复部分schema格式问题   * v0.3.4 - 2023.12.23 增加API调用频率限制说明   * v0.3.3 - 2023.08.11 增加项目成员相关接口说明   * v0.3.2 - 2022.11.04 增加文件翻译相关接口说明   * v0.3.1 - 2022.10.16 修改 tag 及 schema 以便生成 sdk   * v0.3.0 - 2022.10.16 增加术语历史记录接口说明，调整历史记录接口字段; 增加文档中 operationId 定义;                         修复项目信息相关接口格式定义; 增加 JSON 格式文档入口   * v0.2.1 - 2022.07.23 增加成员贡献接口文档; 完善列表接口数据结构   * v0.2.0 - 2022.06.15 增加讨论及私信相关接口文档   * v0.1.3 - 2022.03.10 增加历史记录相关接口文档   * v0.1.2 - 2022.02.07 完善词条搜索接口 query 参数说明   * v0.1.1 - 2022.01.17 增加文件历史相关接口文档   * v0.1.0 - 2022.01.12 初次发布 

    The version of the OpenAPI document: 0.3.4
    Contact: master@mail.paratranz.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from paratranz_client.models.get_issue200_response import GetIssue200Response

class TestGetIssue200Response(unittest.TestCase):
    """GetIssue200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetIssue200Response:
        """Test GetIssue200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetIssue200Response`
        """
        model = GetIssue200Response()
        if include_optional:
            return GetIssue200Response(
                activities = [
                    paratranz_client.models.reply.Reply(
                        id = 1001, 
                        created_at = '2021-01-11T03:19:52.818Z', 
                        updated_at = null, 
                        project = 1453, 
                        uid = 18, 
                        parent = 58, 
                        content = '回复内容 [链接](https://paratranz.cn)', 
                        html = '回复内容 <a href="https://paratranz.cn">链接</a>', 
                        last_edit = null, 
                        refer = [1, 2, 3], )
                    ],
                subscribers = [
                    paratranz_client.models.user.User(
                        id = 18, 
                        created_at = '2021-01-11T03:19:52.818Z', 
                        updated_at = '2021-01-11T03:19:52.818Z', 
                        last_visit = null, 
                        username = 'bruceczk', 
                        nickname = '机智的布鲁斯', 
                        bio = '是站长', 
                        avatar = '', 
                        email = '', 
                        credit = 56, 
                        translated = 56, 
                        edited = 56, 
                        reviewed = 56, 
                        commented = 56, 
                        points = 1.337, )
                    ],
                user = paratranz_client.models.user.User(
                    id = 18, 
                    created_at = '2021-01-11T03:19:52.818Z', 
                    updated_at = '2021-01-11T03:19:52.818Z', 
                    last_visit = null, 
                    username = 'bruceczk', 
                    nickname = '机智的布鲁斯', 
                    bio = '是站长', 
                    avatar = '', 
                    email = '', 
                    credit = 56, 
                    translated = 56, 
                    edited = 56, 
                    reviewed = 56, 
                    commented = 56, 
                    points = 1.337, ),
                id = 1001,
                created_at = '2021-01-11T03:19:52.818Z',
                updated_at = '2021-01-11T03:19:52.818Z',
                project = 1453,
                uid = 18,
                parent = 56,
                title = '讨论标题',
                content = '讨论内容 [链接](https://paratranz.cn)',
                html = '讨论内容 <a href="https://paratranz.cn">链接</a>',
                status = 56,
                last_edit = 18,
                refer = [1, 2, 3]
            )
        else:
            return GetIssue200Response(
        )
        """

    def testGetIssue200Response(self):
        """Test GetIssue200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
