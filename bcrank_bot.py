import discord,requests
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="BCRank.us"))

@bot.command()
async def user(ctx,name):
    try:
        req = requests.get(f"https://bcrank.us/?q={name}")
        soup = BeautifulSoup(req.content,'html.parser')
        images = soup.find('img',class_="avatar-image")
        avatar_img = images['data-src']
        desc = soup.find("div",class_="results-item-troop-info-table-cell-right")
        level = soup.find("span",class_="muted")
        get_ltxt = level.get_text()
        replace = get_ltxt.replace("L","")
        images2 = soup.find('img',class_="results-avatar-image")
        clan_img = images2['data-src']
        pvp_rating = soup.find("span",class_="results-rank-x-small")
        troop_name = soup.find("span",class_="results-troop-name")
        last_online = soup.find("span",class_="results-date-num")
        pr = soup.find("span",class_="results-tier-reward-details-pr")
        sum_pool = soup.find("div",class_="results-summary-prizepool")
        embed=discord.Embed(title=f"IGN: {name}",description=f"Description: {desc.get_text()}",color=0xa26709)
        embed.set_author(name="BC Rank", url=f"https://bcrank.us/?q={name}", icon_url="https://cdn.bcrank.us/226/img/bcrank.png")
        embed.set_thumbnail(url=clan_img)
        embed.set_image(url=avatar_img)
        embed.add_field(name="Level", value=replace, inline=True)
        embed.add_field(name="Troop Name", value=troop_name.get_text(), inline=True)
        embed.add_field(name="Last Online",value=last_online.get_text(),inline=True)
        embed.add_field(name="Power Rating",value=pr.get_text(),inline=True)
        embed.add_field(name="Prize Pool Summary",value=sum_pool.get_text(),inline=True)
        embed.set_footer(text="Bot Made By Droid#1366",icon_url="https://cdn.bcrank.us/226/img/bc-tips-avatar.png")
        await ctx.send(embed=embed)
    except Exception:
        err_embed=discord.Embed(title=f"User Not Found Error",color=0xa26709)
        err_embed.set_author(name="BC Rank", url=f"https://bcrank.us/?q={name}", icon_url="https://cdn.bcrank.us/226/img/bcrank.png")
        err_embed.set_thumbnail(url="https://cdn.bcrank.us/226/img/catalog/monsters/large/coralrex_3.png")
        err_embed.set_image(url="https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/4a09aa14589265.5628657ca1ad5.jpg")
        err_embed.set_footer(text="Bot Made By Droid#1366")
        await ctx.send(embed=err_embed)
@bot.command()
async def clan(ctx,clan_name): 
    try:
        req = requests.get(f"https://bcrank.us/?q={clan_name}")
        soup = BeautifulSoup(req.content,'html.parser')
        leader = soup.find("span",class_ = "results-date-num")
        leader_name = leader.get_text()
        req_ = requests.get(f"https://bcrank.us/?q={leader_name}")
        newsoup = BeautifulSoup(req_.content,'html.parser')
        avatar = newsoup.find("img",class_="avatar-image")
        desc = soup.find(id="results-item-troop-info-more")
        pr = soup.find("span",class_="results-rank-record").get_text()
        troop_members = soup.find("span",class_="results-troop-name").get_text()
        troop_flag = soup.find("img",class_="results-avatar-image")
        sum_prizepool = soup.find("div",class_="results-summary-prizepool").get_text()
        embed=discord.Embed(title=f"Clan Name: {clan_name}",color=0xa26709)
        embed.set_author(name="BC Rank", url=f"https://bcrank.us/?q={clan_name}", icon_url="https://cdn.bcrank.us/226/img/bcrank.png")
        embed.set_thumbnail(url=troop_flag['data-src'])
        embed.set_image(url=avatar['data-src'])
        embed.add_field(name="Description",value=f"Description: {desc.get_text()}",inline=False)
        embed.add_field(name="Average Power Rating",value=pr.replace("pr avg:",""),inline=True)
        embed.add_field(name="Members",value=troop_members,inline=True)
        embed.add_field(name="Prize Pool Summary",value=sum_prizepool,inline=True)
        embed.add_field(name="Leader",value=leader_name,inline=True)
        embed.set_footer(text="Bot Made By Droid#1366")
        await ctx.send(embed=embed)
    except Exception:
            err_embed=discord.Embed(title=f"Clan Not Found Error",color=0xa26709)
            err_embed.set_author(name="BC Rank", url=f"https://bcrank.us/?q={clan_name}", icon_url="https://cdn.bcrank.us/226/img/bcrank.png")
            err_embed.set_thumbnail(url="https://cdn.bcrank.us/226/img/catalog/monsters/kaioyo_1.png")
            err_embed.set_image(url="https://pbs.twimg.com/media/DVD_0JmV4AARBat.jpg")
            err_embed.set_footer(text="Bot Made By Droid#1366")
            await ctx.send(embed=err_embed)

@bot.command()
async def monster(ctx,monster_name):
    try:
        req = requests.get(f"https://bcrank.us/catalog/?q={monster_name}")
        soup = BeautifulSoup(req.content,'html.parser')
        monster_img = soup.find("img",class_="catalog-image-main")
        rarity = soup.find("span",class_="image-item-no-border-mobile").get_text()
        desc = soup.find("em").get_text()
        element_img = soup.find("img",class_="element")
        pr = soup.find("span",class_="power-rating").get_text()
        lvl = soup.find("span",class_="level").get_text()
        new_lvl = []
        if len(lvl) > 2:
            substring = str(lvl)[0:5]
            new_lvl.append(substring)
        atk = soup.find("span",class_="attack").get_text()
        hp = soup.find("span",class_="hp").get_text()
        rcv = soup.find("span",class_="recovery").get_text()
        crit = soup.find("span",class_="crit").get_text()
        defense = soup.find("span",class_="defense").get_text()
        feed = soup.find("span",class_="feed").get_text()
        embed = discord.Embed(title=f"{monster_name}".capitalize(),color=0xa26709)
        embed.set_author(name="BC Rank", url=f"https://bcrank.us/catalog?q={monster_name}", icon_url="https://cdn.bcrank.us/226/img/bcrank.png")
        embed.set_thumbnail(url=element_img['src'])
        embed.set_image(url=monster_img['data-src'])
        embed.add_field(name="Description",value=desc.capitalize(),inline=False)
        embed.add_field(name="Rarity",value=rarity.capitalize(),inline=True)
        embed.add_field(name="Power Level",value=pr,inline=True)
        embed.add_field(name="Level",value=new_lvl[0],inline=True)
        embed.add_field(name="Attack",value=atk,inline=True)
        embed.add_field(name="Health",value=hp,inline=True)
        embed.add_field(name="Recovery",value=rcv,inline=True)
        embed.add_field(name="Crit-Chance",value=crit,inline=True)
        embed.add_field(name="Defense",value=defense,inline=True)
        embed.add_field(name="Feed Value",value=feed,inline=True)
        embed.set_footer(text="Bot Made By Droid#1366")
        await ctx.send(embed=embed)
    except Exception:
        err_embed=discord.Embed(title=f"Monster Not Found Error",color=0xa26709)
        err_embed.set_author(name="BC Rank", url=f"https://bcrank.us/catalog?q={monster_name}", icon_url="https://cdn.bcrank.us/226/img/bcrank.png")
        err_embed.set_thumbnail(url="https://cdn.bcrank.us/226/img/catalog/monsters/large/e7liondog.png")
        err_embed.set_image(url="https://games.lol/wp-content/uploads/2019/07/battle-camp-download-PC-free-1024x572.jpg")
        err_embed.set_footer(text="Bot Made By Droid#1366")

bot.run("")
