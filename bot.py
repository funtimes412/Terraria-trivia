import discord
from discord.ext import commands
import time
from logic import *
import asyncio

bot = commands.Bot(command_prefix="!", self_bot=True)
alternate = 0

# match answers and start gathering data on bot accuracy

@bot.event
async def on_message(message):
    global alternate
    response = ["idk",
                "forgot",
                "dunno"]
    channel = bot.get_channel(578675563301044234)

    if message.channel.id != 578675563301044234:
        return
    
    if message.author == bot.user:
        return

    try:
        if message.author.id == 578640960045580288 and message.embeds:
            for embed in message.embeds:
                triviaTitle = embed.title
                triviaDescription = embed.description
                if triviaTitle == "Trivia Question":
                    alternate += 1
                    count = 0
                    filenames = getFileNames()
                    if random.randint(0, 1) == 1:
                        filenames = filenames[::-1] # random variety bs here
                    if alternate%2:
                        while True:
                            answer = None
                            file = readFile(filenames[count])
                            count += 1
                            questionIndex = findQuestionIndex(file, triviaDescription)
                            if questionIndex:
                                winnerName = findWinnerName(file, questionIndex)
                                answer = findWinningAnswer(file, questionIndex, winnerName)
                            if answer:
                                break
                        await asyncio.sleep(random.uniform(0.50,1.25)) # artificial delay
                        await channel.send(answer)
                # print("done reading")
    except IndexError:
        await channel.send(response[random.randint(0, 2)])
    except Exception as e:
        print(f"Error{e}")
    await bot.process_commands(message)

bot.run("<bottokenhere>")


