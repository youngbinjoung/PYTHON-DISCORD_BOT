import discord, asyncio, datetime,pytz
import random
client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    await client.change_presence(status=discord.Status.online, activity=discord.Game("//help"))

@client.event
async def on_message(message):
    admin_jyb=["영빈","정영빈"]
    if message.content == "테스트": # 메세지 감지
        await message.channel.send ("{} 님 어서오세요!!".format(message.author.mention))
        # await message.author.send ("{} | {}, User, Hello".format(message.author, message.author.mention))

    elif message.content == "//help": # 메세지 감지
        embed = discord.Embed(title="도운봇 명령어",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
        embed.add_field(name="//홀짝", value="홀수 짝수중 랜덤으로 나와요!", inline=False)
        embed.add_field(name="//청소 []", value="[]에 값을 입력하면 숫자만큼의 메세지를 삭제해요! (관리자만 사용가능)", inline=False)
        embed.add_field(name="//랜덤숫자 []", value="[]에 숫자를 입력하면 1~[]숫자 무작위로 나와요! ", inline=False)
        embed.add_field(name="//랜덤이름", value="랜덤으로 이름이 만들어집니다!", inline=False)
        embed.set_thumbnail(url="https://postfiles.pstatic.net/MjAyMTEwMjZfNjAg/MDAxNjM1MjEwNzU2NzEz.0-GhZYujjVSHpwdePNFsb49uqPwt7_is_cfP-BkhNmkg.ddlqFrcnDoNujXrgPIdYbR9CLQACpSQzWZfc8MAfdEIg.PNG.aswer9124/%ED%8F%AC%ED%86%A0%EC%83%B5_%EB%8F%84%EC%9A%B4.png?type=w966")
        await message.channel.send (embed=embed)

    elif admin_jyb[0] in message.content:
        await message.channel.send ("저를 만들어주신 분이죠!")
    elif admin_jyb[1] in message.content:
        await message.channel.send ("저를 만들어주신 분이죠!")   

    elif message.content =="//홀짝":
        even=random.randrange(1,3)
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
        await message.channel.send("🎰 {} 🎰".format(random_num))
    elif message.content=="//랜덤이름":
        mid_name=["민","준","서","예","도","윤","시","우","주","원","하","지","호","후","현","훈","건","진","선","재","연","유","정","승","혁","은","환","찬","성","영","수","동","태","규","한","결","이","안","온","율","빈","람","석","양","희","완","강","채","운"]
        end_name=["민","준","서","예","도","윤","시","우","주","원","하","지","호","후","현","훈","건","진","선","재","연","유","정","승","혁","은","환","찬","성","영","수","동","태","규","한","결","이","안","온","율","빈","람","석","양","희","완","강","채","운"]
        mid_random_name=random.randrange(0,len(mid_name)+1)
        end_random_name=random.randrange(0,len(end_name)+1)
        
        await message.channel.send(mid_name[mid_random_name]+end_name[end_random_name])
        

# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('')