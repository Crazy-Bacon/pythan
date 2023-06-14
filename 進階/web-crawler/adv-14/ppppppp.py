#######################模組#######################
import discord  # pip install -U py-cord
import os
from dotenv import load_dotenv  # pip install -U python-dotenv

#######################初始化#######################

# 載入環境變數
load_dotenv()

# 建立機器人
bot = discord.Bot()


#######################事件#######################
@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


#######################指令#######################
@bot.slash_command(name="a", description="Say hello to the bot")
async def a(ctx):
    """輸入hello, 會回傳Hey!"""
    await ctx.respond("..................................................")


@bot.slash_command(name="repeat", description="1")
@discord.option(name="times", description="1", required=False, default=1)
async def repeat(ctx, times: int):
    """輸入hello, 會回傳Hey!"""
    result = ""
    for i in range(times):
        result += f"{i +1}\n"
    await ctx.respond(result)


#######################啟動#######################
def main():
    # 讀取環境變數, 並啟動機器人
    bot.run(os.getenv('TOKEN'))


# 主程式, 這樣寫是為了讓程式碼更有模組化, 同時可以當作模組使用
if __name__ == "__main__":
    main()