import discord, re
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
from fuzzywuzzy import fuzz
import traceback
import sys
import datetime
from subprocess import call
import random as rm
import Manager

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
client.remove_command("help")
phrases = ["Богатырь - это тот, кто тырит у богатых?", "Хотите сладких снов? - Усните в торте!",
           "Береги Enter смолоду.", "Пока семь раз мерил, другие отрезали.", "Один в поле не убежит.",
           "Рога быстрее всего вырастают на лысине!", "Нажатие на кнопку! По коням!",
           "Cookie#2899 заплатите чеканной монетой!", "Наташа, тут кто-то пришел...", "Здесь могла быть ваша реклама.",
           "X AE A-xii FKA X AE A-12", "Directed by Ro... USA Goverment!", "It is evolving, just backwards",
           "Эта корова еще не найдена, Сэр!", "Парю где хочу", "Я устал, я у... Но делать нечего"]
random = rm.SystemRandom()


@client.command()
@commands.has_any_role("XaCkeR")
async def latency(ctx):
    await ctx.send(client.latency)


@client.command()
@commands.has_any_role("XaCkeR")
async def shutdown(ctx):
    sys.exit()


@client.command()
@commands.has_any_role("XaCkeR")
async def restart(ctx):
    call(".\\RestartInit.bat")
    sys.exit()


@client.event
async def on_command_error(ctx, exception):
    channel = client.get_channel(925876335975481394)
    embed = discord.Embed(title=':x: Command Error', colour=0xe74c3c)
    embed.add_field(name='Command', value=ctx.command)
    embed.description = f"```py\n{traceback.format_exception(type(exception), exception, exception.__traceback__)}\n```"
    embed.timestamp = datetime.datetime.utcnow()
    await channel.send(embed=embed)


@client.event
async def on_error(event, *args, **kwargs):
    channel = client.get_channel(925876335975481394)
    embed = discord.Embed(title=':x: Event Error', colour=0xe74c3c)
    embed.add_field(name='Event', value=event)
    embed.description = f"```py\n{traceback.format_exc()}\n```"
    embed.timestamp = datetime.datetime.utcnow()
    await channel.send(embed=embed)


@client.event
async def on_ready():
    game = discord.Game(".help")
    await client.change_presence(activity=game)
    channel = client.get_channel(925876335975481394)
    await channel.send('Buildya was connected')
    DiscordComponents(client)


# clear
@client.command(Pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount + 1)


# helps
@client.command(Pass_context=True)
async def helps(ctx):
    msg = await ctx.send(
        embed = discord.Embed(title=phrases[rm.randint(0, len(phrases) - 1)], colour=discord.Color.red()),
        components = [
            Button(style = ButtonStyle.red, label = 'Поиск категорий', emoji = '🔎'),
            Button(style = ButtonStyle.blue, label = 'Создать пост', emoji = '📝'),
            Button(style = ButtonStyle.green, label = "Помощь Администрации", emoji = '📢')
        ])
    while (True):
        responce = await client.wait_for("button_click", check=lambda message: message.author == ctx.author)
        await responce.edit_origin()
        if (ctx.channel == responce.channel):
            if (responce.component.label == "Поиск категорий"):
                # await tempMessage.delete()
                message = await ctx.send(
                    embed=discord.Embed(title="Введите название категории", colour=discord.Color.red()))
                channelName = await client.wait_for("message", check=lambda message: message.author == ctx.author)
                while (channelName.channel != ctx.channel):
                    channelName = await client.wait_for("message", check=lambda message: message.author == ctx.author)
                result = re.sub("[$|@|&|!|\"|\'|\\|#|№|:|;|?|/|,|.|<|>|}|{|!|*|+|-|=|-|`|~|^|%|(|)|[|\]]", "",
                                channelName.content)
                channel = discord.utils.get(ctx.guild.channels,
                                            name=f"разговоры-in-{result.replace(' ', '-', 1).replace(' ', '')}")
                try:
                    await ctx.send(embed=discord.Embed(title="Найдена категория", colour=discord.Color.red()).add_field(
                        name="Перейти", value=f"https://discord.com/channels/906460947667882045/{channel.id}"))
                except AttributeError:
                    maximalRatio = 0
                    maximalRatioChannel = None
                    for guild in client.guilds:
                        for thisChannel in guild.text_channels:
                            ratio = fuzz.ratio(f"разговоры-in-{result.replace(' ', '-', 1).replace(' ', '')}",
                                               thisChannel.name)
                            if (ratio >= 85):
                                if (ratio > maximalRatio):
                                    maximalRatio = ratio
                                    maximalRatioChannel = thisChannel
                    if (maximalRatio < 85):
                        await ctx.send(embed=discord.Embed(title="Ничего не найдено ❌", colour=discord.Color.red()))
                    else:
                        await ctx.send(
                            embed=discord.Embed(title="Найдена категория ✔️", colour=discord.Color.red()).add_field(
                                name="Перейти",
                                value=f"https://discord.com/channels/906460947667882045/{maximalRatioChannel.id}"))

            elif (responce.component.label == "Создать пост"):
                # await tempMessage.delete()
                message = await ctx.send(embed=discord.Embed(title="Куда выложить пост?", colour=discord.Color.red()))
                channelName = await client.wait_for("message", check=lambda message: message.author == ctx.author)
                while (channelName.channel != ctx.channel):
                    channelName = await client.wait_for("message", check=lambda message: message.author == ctx.author)
                result = re.sub("[$|@|&|!|\"|\'|\\|#|№|:|;|?|/|,|.|<|>|}|{|!|*|+|-|=|-|`|~|^|%|(|)|[|\]]", "",
                                channelName.content)
                maximalRatio = 0
                maximalRatioChannel = None
                for guild in client.guilds:
                    for thisChannel in guild.text_channels:
                        ratio = fuzz.ratio(f"посты-in-{result.replace(' ', '-', 1).replace(' ', '').lower()}",
                                           thisChannel.name)
                        if (ratio >= 90):
                            if (ratio > maximalRatio):
                                maximalRatio = ratio
                                maximalRatioChannel = thisChannel
                if (maximalRatio < 90):
                    await ctx.send(embed=discord.Embed(title="Категория не найдена, воспользуйтесь поиском",
                                                       colour=discord.Color.red()))
                else:
                    messagesToPost = []
                    attachmentsToPost = []
                    await ctx.send(
                        embed=discord.Embed(title="Сколько сообщений читать? (1-10)", colour=discord.Color.red()))
                    howManyMessagesToRead = await client.wait_for('message',
                                                                  check=lambda message: message.author == ctx.author)
                    while (re.sub("\d+", "",
                                  howManyMessagesToRead.content) != "" or ctx.channel != howManyMessagesToRead.channel):
                        if (re.sub("\d+", "", howManyMessagesToRead.content) != ""):
                            await ctx.send(embed=discord.Embed(title="Сколько сообщений читать? (1-10)",
                                                               colour=discord.Color.red()))
                        howManyMessagesToRead = await client.wait_for('message', check=lambda
                            message: message.author == ctx.author)
                    if (int(howManyMessagesToRead.content) > 10):
                        howManyMessagesToRead = 10
                    elif (int(howManyMessagesToRead.content) < 1):
                        howManyMessagesToRead = 1
                    else:
                        howManyMessagesToRead = int(howManyMessagesToRead.content)
                    embed = discord.Embed(title="Голосование", colour=discord.Color.blue(), description="")
                    await ctx.send(
                        embed=discord.Embed(title=f"Следующие {howManyMessagesToRead} сообщения будут добавлены в пост",
                                            colour=discord.Color.red()))
                    i = 0
                    while (i < howManyMessagesToRead):
                        message = await client.wait_for("message", check=lambda message: message.author == ctx.author)
                        if (ctx.channel == message.channel and message.content != "⠀"):
                            await ctx.channel.purge(limit=1)
                            i += 1
                            messagesToPost.append(message)
                            for attach in message.attachments:
                                attachmentsToPost.append(attach)
                    postEmbed = discord.Embed(colour=discord.Color.red())
                    postEmbed.add_field(name="Индекс поста:", value="0")
                    postEmbed.add_field(name="Оценка поста:", value="0")
                    postEmbed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                    postDesription = ""
                    temp = ""
                    try:
                        for messageToPost in messagesToPost:
                            print(messageToPost.content)
                            temp = postDesription
                            postDesription = temp + messageToPost.content + '\n'
                    except Exception:
                        for attach in attachmentsToPost:
                            await maximalRatioChannel.send(attach.url)
                    postEmbed.description = postDesription
                    post = await maximalRatioChannel.send(embed=postEmbed)
                    await post.add_reaction("👍")
                    await post.add_reaction("👎")
                    adding = [post.id]
                    for attach in attachmentsToPost:
                        app = await maximalRatioChannel.send(attach.url)
                        adding.append(app.id)
                    emb = post.embeds[0].set_field_at(0, value=Manager.addPost(adding, ctx.author.id),
                                                      name="Индекс поста:")
                    await post.edit(embed=emb)
                    description = f"https://discord.com/channels/906460947667882045/{maximalRatioChannel.id}/{post.id}"
                    await ctx.send(embed=discord.Embed(
                        title="Пост выложен ✈️.\nДля удаления поста воспользуйтесь командой deletePost🗑️",
                        colour=discord.Color.red(), description=description))

            elif (responce.component.label == "Помощь Администрации"):
                messagesToPost = []
                attachmentsToPost = []
                await ctx.send(
                    embed=discord.Embed(title="Сколько сообщений читать? (1-10)", colour=discord.Color.red()))
                howManyMessagesToRead = await client.wait_for('message',
                                                              check=lambda message: message.author == ctx.author)
                while (re.sub("\d+", "",
                              howManyMessagesToRead.content) != "" or ctx.channel != howManyMessagesToRead.channel):
                    if (re.sub("\d+", "", howManyMessagesToRead.content) != ""):
                        await ctx.send(
                            embed=discord.Embed(title="Сколько сообщений читать? (1-10)", colour=discord.Color.red()))
                    howManyMessagesToRead = await client.wait_for('message',
                                                                  check=lambda message: message.author == ctx.author)
                if (int(howManyMessagesToRead.content) > 10):
                    howManyMessagesToRead = 10
                elif (int(howManyMessagesToRead.content) < 1):
                    howManyMessagesToRead = 1
                else:
                    howManyMessagesToRead = int(howManyMessagesToRead.content)
                await ctx.send(embed=discord.Embed(
                    title=f"Следующие {howManyMessagesToRead} сообщения будут отправлены Администрации",
                    colour=discord.Color.red()))
                i = 0
                while (i < howManyMessagesToRead):
                    message = await client.wait_for("message", check=lambda message: message.author == ctx.author)
                    if (ctx.channel == message.channel and message.content != "⠀"):
                        await ctx.channel.purge(limit=1)
                        i += 1
                        messagesToPost.append(message)
                        for attach in message.attachments:
                            attachmentsToPost.append(attach)
                postEmbed = discord.Embed(colour=discord.Color.red())
                postEmbed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                postDesription = ""
                temp = ""
                try:
                    for messageToPost in messagesToPost:
                        print(messageToPost.content)
                        temp = postDesription
                        postDesription = temp + messageToPost.content + '\n'
                except Exception:
                    for attach in attachmentsToPost:
                        await discord.utils.get(ctx.guild.channels, id=910974206131453973).send(attach.url)
                postEmbed.description = postDesription
                await discord.utils.get(ctx.guild.channels, id=910974206131453973).send(embed=postEmbed)
                for attach in attachmentsToPost:
                    await discord.utils.get(ctx.guild.channels, id=910974206131453973).send(attach.url)
                await ctx.send(embed=discord.Embed(title="Администрация оповещена ✈️", colour=discord.Color.red()))


@client.event
async def on_reaction_add(reaction, user):
    for embed in reaction.message.embeds:
        emb = embed
    if (user.name != "Buildya"):
        for field in emb.fields:
            if (field.name == "Оценка поста:"):
                if (reaction.emoji == "👎"):
                    emb.set_field_at(index=1, value=int(field.value) - 1, name="Оценка поста:")
                    await reaction.message.edit(embed=emb)
                if (reaction.emoji == "👍"):
                    emb.set_field_at(index=1, value=int(field.value) + 1, name="Оценка поста:")
                    await reaction.message.edit(embed=emb)


@client.event
async def on_reaction_remove(reaction, user):
    for embed in reaction.message.embeds:
        emb = embed
    if (user.name != "Buildya"):
        for field in emb.fields:
            if (field.name == "Оценка поста:"):
                if (reaction.emoji == "👎"):
                    emb.set_field_at(index=1, value=int(field.value) + 1, name="Оценка поста:")
                    await reaction.message.edit(embed=emb)
                if (reaction.emoji == "👍"):
                    emb.set_field_at(index=1, value=int(field.value) - 1, name="Оценка поста:")
                    await reaction.message.edit(embed=emb)


# deletePost
@client.command()
async def deletePost(ctx, indexOfPost: int, channelName: str ):
    cond = Manager.exist(indexOfPost, ctx.author.id)
    print(cond)
    possible = False
    if (cond == 1):
        possible = True
    elif (cond == 0):
        for role in ctx.author.roles:
            if (role.name == "aDmins" or role.name == "XaCkeR" or role.name == "helper"):
                possible = True
                target = ctx.guild.get_member((int(Manager.getAuthorId(indexOfPost))))
                for role in target.roles:
                    if (role.name == "aDmins" or role.name == "XaCkeR" or role.name == "helper"):
                        possible = False
        if (not possible):
            await ctx.send(embed=discord.Embed(title="Это не Ваш пост 🐧", colour=discord.Color.red()))
    elif (cond == -1):
        await ctx.send(embed=discord.Embed(title="Поста с таким индексом не существует 👻", colour=discord.Color.red()))
    if (possible == True):
        toDelete = Manager.getPostContent(indexOfPost)
        if (re.sub("<#\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d>", "", channelName) == ""):
            id = int(re.sub("[<|#|>]", "", channelName))
            channel = discord.utils.get(ctx.guild.channels, id=id)
        for idOfPost in toDelete:
            msg = await channel.fetch_message(idOfPost)
            await msg.delete()
        Manager.deletePost(indexOfPost)

@client.command()
async def test( ctx, test ):
	await ctx.send(test)

# help
@client.command()
async def help(ctx):
    emb = discord.Embed(title="Доступные команды", colour=discord.Color.red())
    for role in ctx.author.roles:
        if (role.name == "aDmins"):
            emb.add_field(name=".create",
                          value=":white_small_square: **Функция**: Создание новой категории\n:white_small_square: **Параметры**: Название категории  `String`\n:white_small_square: **Стандартые**: —",
                          inline=False)
            emb.add_field(name=".delete",
                          value=":white_small_square: **Функция**: Удаление категории и вложенных каналов\n:white_small_square: **Параметры**: Название категории  `String`\n:white_small_square: **Стандартые**: —",
                          inline=False)
            emb.add_field(name=".clear",
                          value=":white_small_square: **Функция**: Очистка чата\n:white_small_square: **Параметры**: Кол-во сообщений для очистки  `Integer`\n:white_small_square: **Стандартые**: 100",
                          inline=False)

    emb.add_field(name=".helps",
                  value=":white_small_square: **Функция**: Открытие интерактивного меню\n:white_small_square: **Параметры**: —\n:white_small_square: **Стандартые**: —",
                  inline=False)
    emb.add_field(name=".deletePost",
                  value=":white_small_square: **Функция**: Удаление поста\n:white_small_square: **Параметры**: Индекс поста `Integer`;\nКанал размещения поста `Channel` or `String`\n:white_small_square: **Стандартые**: —")

    await ctx.send(embed=emb)


# create
@client.command()
async def create(ctx, *, categoryName: str):
    if (re.sub("<@&\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d>", "", categoryName) == ""):
        id = int(re.sub("[<|@|&|>]", "", categoryName))
        role = discord.utils.get(ctx.guild.roles, id=id)
        categoryName = role.name
        result = re.sub("[$|@|&|!|\"|\'|\\|#|№|:|;|?|/|,|.|<|>|}|{|!|*|+|-|=|-|`|~|^|%|(|)|[|\]]", "", categoryName)
        channel = discord.utils.get(ctx.guild.channels,
                                    name=f"разговоры-{result.replace(' ', '-').replace(' ', '').lower()}")
        try:
            check = channel.id
            await ctx.send(embed=discord.Embed(title="Категория уже существует 📄", colour=discord.Color.red(),
                                               description=f"https://discord.com/channels/906460947667882045/{channel.id}"))
        except Exception:
            category = await ctx.guild.create_category(categoryName, overwrites=None, reason=None)
            channel = await ctx.guild.create_text_channel(f"разговоры-{categoryName}", overwrites=None,
                                                          category=category, reason=None)
            postChannel = await ctx.guild.create_text_channel(f"посты-{categoryName}", overwrites=None,
                                                              category=category, reason=None)
            await postChannel.set_permissions(ctx.guild.default_role, send_messages=False)
            await ctx.guild.create_text_channel(f"поиск-по-интересам", overwrites=None, category=category, reason=None)
            await ctx.guild.create_voice_channel(f"наместик", overwrites=None, category=category, reason=None)
            await ctx.guild.create_voice_channel(f"войс", overwrites=None, category=category, reason=None)
            await ctx.send(embed=discord.Embed(title="Категория успешно создана 🪄", colour=discord.Color.red(),
                                               description=f"https://discord.com/channels/906460947667882045/{channel.id}"))
    else:
        result = re.sub("[$|@|&|!|\"|\'|\\|#|№|:|;|?|/|,|.|<|>|}|{|!|*|+|-|=|-|`|~|^|%|(|)|[|\]]", "", categoryName)
        channel = discord.utils.get(ctx.guild.channels,
                                    name=f"разговоры-in-{result.replace(' ', '-').replace(' ', '').lower()}")
        try:
            check = channel.id
            await ctx.send(embed=discord.Embed(title="Категория уже существует 📄", colour=discord.Color.red(),
                                               description=f"https://discord.com/channels/906460947667882045/{channel.id}"))
        except Exception:
            category = await ctx.guild.create_category("in " + categoryName, overwrites=None, reason=None)
            channel = await ctx.guild.create_text_channel(f"разговоры-in-{categoryName}", overwrites=None,
                                                          category=category, reason=None)
            postChannel = await ctx.guild.create_text_channel(f"посты-{categoryName}", overwrites=None,
                                                              category=category, reason=None)
            await postChannel.set_permissions(ctx.guild.default_role, send_messages=False)
            await ctx.guild.create_text_channel(f"поиск-по-интересам", overwrites=None, category=category, reason=None)
            await ctx.guild.create_voice_channel(f"наместик", overwrites=None, category=category, reason=None)
            await ctx.guild.create_voice_channel(f"войс", overwrites=None, category=category, reason=None)
            await ctx.send(embed=discord.Embed(title="Категория успешно создана 🪄", colour=discord.Color.red(),
                                               description=f"https://discord.com/channels/906460947667882045/{channel.id}"))


# delete
@client.command()
async def delete(ctx, *, categoryName: str, condition=False):
    if (re.sub("<@&\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d>", "", categoryName) == ""):
        id = int(re.sub("[<|@|&|>]", "", categoryName))
        role = discord.utils.get(ctx.guild.roles, id=id)
        categoryName = role.name
        result = re.sub("[$|@|&|!|\"|\'|\\|#|№|:|;|?|/|,|.|<|>|}|{|!|*|+|-|=|-|`|~|^|%|(|)|[|\]]", "", categoryName)
        channel = discord.utils.get(ctx.guild.channels,
        name=f"разговоры-{result.replace(' ', '-').replace(' ', '').lower()}")
        try:
            check = channel.id
            category = channel.category
            for channel in category.channels:
                await channel.delete()
            await category.delete()
            await ctx.send(embed=discord.Embed(title="Категория успешно удалена 🗑", colour=discord.Color.red()))
        except Exception:
            await ctx.send(embed=discord.Embed(title="Категории не существует 👻", colour=discord.Color.red()))
    else:
        result = re.sub("[$|@|&|!|\"|\'|\\|#|№|:|;|?|/|,|.|<|>|}|{|!|*|+|-|=|-|`|~|^|%|(|)|[|\]]", "", categoryName)
        channel = discord.utils.get(ctx.guild.channels,
                                    name=f"разговоры-in-{result.replace(' ', '-').replace(' ', '').lower()}")
        try:
            check = channel.id
            category = channel.category
            for channel in category.channels:
                await channel.delete()
            await category.delete()
            await ctx.send(embed=discord.Embed(title="Категория успешно удалена 🗑", colour=discord.Color.red()))
        except Exception:
            await ctx.send(embed=discord.Embed(title="Категории не существует 👻", colour=discord.Color.red()))


token = open("./token.txt", "r").readline()

client.run(token)
