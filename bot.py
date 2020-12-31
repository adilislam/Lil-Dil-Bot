# bot.py
import discord
import random
import nacl
import time
TOKEN = hidden
# GUILD = 'Social Distancing Squad'
GUILD = 'Minecraftingoons'

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

list_a = []
list_b = []
skill = {'ankit': 70, 'archit': 70, 'kenny': 100, 'daniel': 100, 'eric': 88, 'saad': 40, 'vin': 40, 'donny': 91, 'chris': 100, 'melissa': 30, 'derek': 72, 'nathan': 80, 'theo': 85,
         'sarah': 40, 'heli': 20, 'danielle': 20, 'vic': 10, 'jiani': 25, 'adil': 38, 'tej': 50, 'noah': 60, 'luca': 50, 'hannah': 50, 'elbert': 60, 'richard': 58, 'mikler': 62, 'kt': 41}


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(message.author)
    print(message.author == 'abhibeast#1356')
    print(type(message.author))

    if (message.author.name == 'abhibeast' or message.author.name == 'vicbu') and message.content.lower() == 'lil pp':
        response = 'you have lil pp'
        await message.channel.send(response)

    elif message.content.lower() == 'lil pp':
        response = '8'
        num = random.randint(0, 10)
        for i in range(num):
            response += '='
        response += 'D'
        await message.channel.send(response)

    if message.content.lower() == 'lil coin flip':
        num = random.randint(0, 1)
        if num == 0:
            await message.channel.send('heads')
        else:
            await message.channel.send('tails')

    if 'lil rps' in message.content.lower():
        rock = "rock"
        paper = "paper"
        scissors = "scissors"
        winmoves = {rock: scissors, paper: rock, scissors: paper}
        num = random.randint(0, 3)

        choice = ''
        if num == 0:
            choice += 'rock'
        elif num == 1:
            choice += 'paper'
        else:
            choice += 'scissors'

        parse = message.content.split(" ")
        opp = parse[2].lower()

        def findwinner(user_input, cpu_move):
            if user_input == cpu_move:
                return "computer played " + str(cpu_move) + "\ndraw!"
            elif cpu_move in winmoves[user_input]:
                return "computer played " + str(cpu_move) + "\nyou win, computer sad :("
            return "computer played " + str(cpu_move) + "\ncomputer wins, computer happy :)"

        await message.channel.send(findwinner(opp, choice))

    def fillteams(a, b, ppl, ascore, bscore, skill):
        diff = 50
        while diff >= 15:
            ascore = 0
            bscore = 0
            a = []
            b = []
            random.shuffle(ppl)
            for player in ppl:
                if ascore < bscore and len(a) < 5:
                    a.append(player)
                    ascore += skill[player]
                elif ascore >= bscore and len(b) < 5:
                    b.append(player)
                    bscore += skill[player]
                elif len(a) == 5:
                    b.append(player)
                    bscore += skill[player]
                else:
                    a.append(player)
                    ascore += skill[player]
            diff = abs(ascore - bscore)
        return [a, b, [ascore, bscore]]

    if 'lil teams' in message.content.lower():
        team_a = 0
        team_b = 0
        global list_a
        global list_b
        global skill
        list_a = []
        list_b = []
        message.content = message.content.lower()
        parse = message.content.split(" ")
        players = parse[2:]
        random.shuffle(players)
        teams = fillteams(list_a, list_b, players, team_a, team_b, skill)
        list_a = teams[0]
        list_b = teams[1]
        result = 'Team A: ' + str(teams[0]) + '\nelo level: ' + str(
            teams[2][0]) + '\nTeam B: ' + str(teams[1]) + '\nelo level: ' + str(teams[2][1])
        await message.channel.send(result)

    if message.content.lower() == 'lil join call':
        channel = message.author.voice.channel
        await channel.connect()

    if message.content.lower() == 'lil leave call':
        server = message.guild.voice_client
        await server.disconnect()

    def adjustelo(winner, loser, skill):
        for player in winner:
            skill[player] += 1
        for player in loser:
            skill[player] -= 1
        return skill

    if message.author.name == 'adil' and message.content.lower() == 'lil win a':
        skill = adjustelo(list_a, list_b, skill)
        await message.channel.send('elo ratings have been adjusted\n' + str(skill))

    if message.author.name == 'adil' and message.content.lower() == 'lil win b':
        skill = adjustelo(list_b, list_a, skill)
        await message.channel.send('elo ratings have been adjusted\n' + str(skill))

    if 'lil elo' in message.content.lower():
        parse = message.content.split(" ")
        if len(parse) == 2:
            sort_skill = dict(sorted(skill.items(), key=lambda item: item[1]))
            await message.channel.send(str(sort_skill))
        elif len(parse) == 3:
            player = parse[2].lower()
            if player in skill:
                elo = skill[player]
                await message.channel.send(player + ' elo is ' + str(elo))
            else:
                await message.channel.send('this player is not currently in our elo system')


client.run(TOKEN)
