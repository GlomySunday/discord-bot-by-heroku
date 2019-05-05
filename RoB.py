import random
import requests
import asyncio
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")


client = Bot(command_prefix=BOT_PREFIX)
@client.command(name = 'Vicc',
                description = 'Kiír egy viccet.',
                brief = 'Nagyon jó vicc',
                aliases = ['Joke' , 'vicc'],
                pass_context = True)
async def Vicc(context):
	possible_responses = [
		'Bence egy b@zi',
		'Botond is az'
	]
	await client.say(random.choice(possible_responses) + ", " +  context.message.author.mention) //'Megemlíti a parancs íróját'
	pass
	
	
	
@client.command(name = 'Spoiler',
                description = 'Le spoilerez egy filmet.',
                brief = 'SPOILER ALERT',
                aliases = ['spoiler' ],
                pass_context = True)
async def Spoiler(context):
	possible_responses = [
		'Darth Vader Luke apja (Star Wars)',
		'Meghal Vasember, miután használja a köveket (Endgame)',
		'Theaon Greyjoy meghal (Game of Thrones)',
		'Az Éjkirályt Arya megölte (Game of Thrones)',
		'Az egyik sárkány átváltoztatja az éjkirály (Game of Thrones)',
		'Han Solot megöli a fia (Star Wars)',
		'Cobb haza megy (Eredet)',
		'Hannibal kiszabadul, de megkíméli Clarice-t (A bárányok hallgatnak)',
		'Thorin Oakenshield meghal (A hobbit)',
		'Walter White meghal (Breaking bad)',
		'Katniss és Peeta nyernek (Éhezők viadala)',
		'Leia Luke testvére (Star Wars)',
		'Claire Underwood lesz az elnök (Kártyvár)',
		'Bernard egy robot (Westworld)',
		'Logan meghal (Logan)',
		'A falu a mi világunkban van (A falu)',
		'Doofy a gyilkos (Horrorra akadva)',
		'Django mindenkit megöl (Django elszabadul)',
		'Spartacus meghal (Spartacus: Vér és Homok)',
		'A szerelem az örödik elem (Ötödik elem)',
		'Neo megmenti Trinityt (Mátrix)',
		'A Titanic elsüllyed, és Jack meghal (Titanic)',
		'Jigsaw tettette, hogy halott (Fűrész)',
		'Joffreyt megmérgezik (Game of Thrones)',
		'"Doc" túléli a terrorista támadást (Vissza a jövőbe)',
		'Fiona egy ogre (Shrek)',
		'Ned Strak meghal (Game of Thrones)',
		'Loki megöli Coulsont (Bosszúállók)',
		'Andy megszökik a börtönből (A remény rabjai)',
		'Jack Sparrow egy élőholt (Karib tenger kalózai)',
		'Anyád se szeret (Az életed)'
	]
	await client.say(random.choice(possible_responses)) //'Megemlíti a parancs íróját'
	pass
        
'''@client.command()
async def square(number):
        squared_value = int(number) * int(number)
        await client.say(str(number) + " squared is " + str(squared_value))
@client.event
async def on_ready():
        await client.change_presence(game=Game(name="with humans"))
        print("Logged in as" + client.user.name)
@client.command()
async def bitcoin():
        url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
        response = requests.get(url)
        value = response.json()['bpi']['USD']['rate']
        await client.say("Bitcoin price is: " + value)
async def list_servers():
        await client.wait_until_ready()
        while not client.is_clsed:
                print("Current servers:")
                for servers in client.servers:
                      print(server.name)
                await asyncio.sleep(6)

        client.loop.create_task_task(list_servers())
@client.command()
async def Hang():
        await client.say('$skip')'''
                        

client.run(process.env.BOT_TOKEN)
