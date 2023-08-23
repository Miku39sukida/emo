from pyrogram import Client
from pagermaid.listener import listener
from pagermaid.utils import Message, client


@listener(command="msg1", description="就一个无聊的插件回复而已，可以用`,apt install msg1`上传插件查看。")
async def msg1(client: Client, context: Message):
    msg = context.arguments
    if not msg:
        await context.edit("自定义消息测试")