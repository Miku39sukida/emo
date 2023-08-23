from pyrogram import Client
from pagermaid.listener import listener
from pagermaid.utils import Message, client


@listener(command="alsc", description="没啥用的帮助")
async def alsc(client: Client, context: Message):
    msg = context.arguments
    if not msg:
        await context.edit("您好，请使用下面指令搜索\n/s 关键词\n\n指令和关键词之间都有空格，例如：\n/s 最终幻想")