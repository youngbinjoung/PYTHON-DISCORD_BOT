import discord, asyncio
import random
client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    await client.change_presence(status=discord.Status.online, activity=discord.Game("//help"))

@client.event
async def on_message(message):
    admin_jyb=["영빈","정영빈"]
    even=random.randrange(1,3)
    if message.content == "테스트": # 메세지 감지
        await message.channel.send ("{} 님 어서오세요!!".format(message.author.mention))
        # await message.author.send ("{} | {}, User, Hello".format(message.author, message.author.mention))
    elif message.content == "//help":
        await message.channel.send ("{}님 안녕하세요!".format(message.author.mention))
        await message.channel.send ("========= 도운봇 Command =========")
        await message.channel.send ("//홀짝 : 홀수짝수 무작위로 나와요!")
        await message.channel.send ("//청소 [] : ")
        await message.channel.send ("==================================")
    elif admin_jyb[0] in message.content:
        await message.channel.send ("저를 만들어주신 분이죠!")
    elif admin_jyb[1] in message.content:
        await message.channel.send ("저를 만들어주신 분이죠!")   
    elif message.content=="숫자100":
        for a in range(1,100):
            await message.channel.send(a) 
    elif message.content =="//홀짝":
        blank=chr(32)
        if even==1:
            even="홀"
        elif even==2:
            even="짝"
        await message.channel.send("🎲{}{}{}🎲 이걸로 가자".format(blank,even,blank)) 
    
    elif message.content.startswith ("//청소"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0x000000)
            embed.set_footer(text="Bot Made by. 영빈 #8494", icon_url="https://discordapp.com/channels/691615852620939274/703908401381376000/711859989177958410")
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))
    elif message.content.startswith ("//랜덤숫자"):
        amount2= message.content[7:]
        abc=int(amount2)
        random_num=random.randrange(1,abc+1)
        await message.channel.send(random_num)
        

# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('OTAxOTgyMTEwMDYyMTA0NjQ5.YXXyTQ.oALSUDbyDmvCNaz1DCLMRIc7RKI')