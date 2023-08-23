from pyrogram import Client
from pagermaid.listener import listener
from pagermaid.utils import Message, client


@listener(command="dxzp", description="提醒用户注意防范盗号诈骗之类的")
async def dxzp(client: Client, context: Message):
    msg = context.arguments
    if not msg:
        await context.edit("谨防盗号！谨防盗号！谨防盗号！\n\n仔细看: https://t.me/tgcnz/963\n\n仔细看: https://t.me/tgcnz/965")