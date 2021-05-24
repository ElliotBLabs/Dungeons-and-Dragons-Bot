import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

import random
from discord import Game

Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()

def get_channel(channel_name): # Finding Channels
    for channel in client.get_all_channels():
        print(channel)
        if channel.name == channel_name:
            return channel
    return None

def get_user(user_req): # Finding users
    for user in client.get_all_members():
        print(user)
        if user.name ==  user_req:
            return user
    return None

@client.event
async def on_ready():
    print('Operational...')
    await client.send_message(get_channel('session-summaries'), "\n*Session 6*:\n")

@client.event
async def on_message(message):
    if message.content.startswith('Durnan:'):  # Requesting bot
        await client.send_message(message.channel, "Durnan, at your service")
        x =server.members
        for member in x:
            print(member. name) # you'll just print out Member objects your way.
    if message.content.startswith('c001'):  # Begin server opening
        #await client.send_message(get_user("Aboedi"), "You awake to a howl in the wind, a shard of a diamond appears in front of you and you hear the voices of a Tavern inside. Without control, you grab the diamond and are thrown through time and space to find yourself in a damp well with a single rope suspended from faint embers glowing at the top. \nhttps://discord.gg/jrNxKmu\nYour adventure awaits...") # Introduce them to the Admin channel
        #await client.send_message(get_user("Cookie"), "You awake to a howl in the wind, a shard of a diamond appears in front of you and you hear the voices of a Tavern inside. Without control, you grab the diamond and are thrown through time and space to find yourself in a damp well with a single rope suspended from faint embers glowing at the top. \nhttps://discord.gg/jrNxKmu\nYour adventure awaits...") # Introduce them to the Admin channel
        #await client.send_message(get_user("Da Cabo"), "You awake to a howl in the wind, a shard of a diamond appears in front of you and you hear the voices of a Tavern inside. Without control, you grab the diamond and are thrown through time and space to find yourself in a damp well with a single rope suspended from faint embers glowing at the top. \nhttps://discord.gg/jrNxKmu\nYour adventure awaits...") # Introduce them to the Admin channel
        #await client.send_message(get_user("luas"), "You awake to a howl in the wind, a shard of a diamond appears in front of you and you hear the voices of a Tavern inside. Without control, you grab the diamond and are thrown through time and space to find yourself in a damp well with a single rope suspended from faint embers glowing at the top. \nhttps://discord.gg/jrNxKmu\nYour adventure awaits...") # Introduce them to the Admin channel
        #await client.send_message(get_user("lwarrel6"), "You awake to a howl in the wind, a shard of a diamond appears in front of you and you hear the voices of a Tavern inside. Without control, you grab the diamond and are thrown through time and space to find yourself in a damp well with a single rope suspended from faint embers glowing at the top. \nhttps://discord.gg/jrNxKmu\nYour adventure awaits...") # Introduce them to the Admin channel
        #await client.send_message(get_user("XV 88"), "You awake to a howl in the wind, a shard of a diamond appears in front of you and you hear the voices of a Tavern inside. Without control, you grab the diamond and are thrown through time and space to find yourself in a damp well with a single rope suspended from faint embers glowing at the top. \nhttps://discord.gg/jrNxKmu\nYour adventure awaits...") # Introduce them to the Admin channel
        pass





#'''

        
@client.event
async def on_member_join(member):  # Checking for additions to server
    print(member.name)
    if member.name == "Aboedi":
        user_info = get_user("Aboedi")
        await client.change_nickname(user_info, "Codus, the Monk") # Change Username
        await client.send_message(get_channel("welcome"), "From the Mountains of the East, self disciplined and a master of Ki. Codus climbs out of the glimmering portal and takes a seat at the bar, politely asking Durnan for a Flagon of 'Orange Juice'.") # Introduce them to the Admin channel
    elif member.name == "Cookie":
        user_info = get_user("Cookie")
        await client.change_nickname(user_info, "Bumble Door, the Warlock") # Change Username
        await client.send_message(get_channel("welcome"), "From the forests of Neverwinter woods, with deep bonds with the very nature that is woven into the grounds and slightly clumsy. Bumble Door stumbles out of th portal, falling flat on his face, a hooded figure chants a spell and he levitates toward a table of bearded dwarves.") # Introduce them to the Admin channel
    elif member.name == "Da Cabo":
        user_info = get_user("Da Cabo")
        await client.change_nickname(user_info, "Alatar, the Cleric") # Change Username
        await client.send_message(get_channel("welcome"), "The mighty, the bold, the violent... Alatar brandishes his warhammer after nobly stepping out of the well, carried by his previous mercenaries he requests a hard ale.") # Introduce them to the Admin channel
    elif member.name == "♂ AssClap ♂":
        user_info = get_user("♂ AssClap ♂")
        await client.change_nickname(user_info, "Sohai , the Monk") # Change Username
        await client.send_message(get_channel("welcome"), "Elegantly, the gentle strokes of bare foot against stone was heard from the base of the well. Leaping out with two polished shortswords in hand was a broad monk. *The Tavern Silences* Durnan shouts 'What are you lot looking at? Never seen a monk before?'") # Introduce them to the Admin channel
    elif member.name == "lwarrel6":
        user_info = get_user("lwarrel6")
        await client.change_nickname(user_info, "Helfie Elfie, the Paladin") # Change Username
        await client.send_message(get_channel("welcome"), "The one and only: *Helfie Elfie*? , a Paladin with a heart of gold and armour of Mithril. Cautiously, grunting, he hauled himself over the well and went to sit with a rowdy group of Elves.") # Introduce them to the Admin channel
    elif member.name == "XV 88":
        user_info = get_user("XV 88")
        await client.change_nickname(user_info, "DM - Rafa") # Change Username
        await client.send_message(get_channel("welcome"), "From afar, the ground begins to quake and the inhabitants of the Yawning Portal Rush outside; a giant floating head of a boy (-Maybe 14/15-) peers down onto the map. Suddenly, a giant, twenty sided object with alien numbers smashed a nearby house. He raises his mug and begins to smile.") # Introduce them to the Admin channel
    


async def background_loop():  # Control _Presence / Barevents
    await client.wait_until_ready()
    while not client.is_closed:
        async for message in client.logs_from(get_channel('yawning-portal'), limit=1):
            if get_user('Durnan "the Wanderer"') == message.author:
                print('YES DURNAN')
                await client.purge_from(get_channel('yawning-portal'), limit = 1)
        barevents = ["Tonight is the 10th annual Dragonfire Drinking contest! The person who can stomach the most Dragonfire Ale (very, VERY hot) will win the grand prize!\n", "A group in the back corner of the tavern are arm wrestling.\n", "An elven bard is playing on stage tonight and asking for requests.\n", "A travelling gnome from a far away land has made a deal with the tavern, and is selling exotic and strange drinks in a wooden stand they have set up in the corner of the room.\n", "It is the monthly wild magic surge brew drinking contest. If you can get the most down, you win. You may lose your hair and grow an extra arm but hey, the prize is 30 gp.\n", "Local criminals hangout in this tavern. They try to sell drugs. One criminal pours red dust in the drinks of the guest while they are not watching.\n", "The tavern is know for gambling. One guy is on a big winsteak and pays drinks for everybody. Nobody knows yet that he plays with loaded dice.\n", "Some tables are flipped over. In the middle of the room is a young orc girl on the ground surrounded by a few people. Her water just broke. She is about to receive twins. Nobody knows what to do.\n", "The owner of the tavern is an old lady. She owns about 5d20 cats. She cant serve you drinks or food right now because she has to feed her cats first.\n", "There is a cow in the middle of the tavern. Everybody is wasted and nobody knows how the cow got there or who owns the cow.\n", "The ‘bartender’ is handing out free drinks and food. The owner is looked into the storage room.\n", "A 10-year old girl is running the tavern. Everybody is afraid of her.\n", "A half-elf sitting alone seems to be muttering to themselves but is actually decribing the comings and goings of the tavern to a sentient weapon on their lap.\n", "Two separate people are drinking alone. Neither seems at all suspicious on their own, but together they happen to be watching every single patron, as well as every entrance/exit.\n", "A soldier is dressed in plainclothes, watching a deal going on at another table. The disguise is not fooling anyone.\n", "It’s the annual ‘Food Frenzy’. For two silver pieces (one of which goes to the house, the other to the pot), participants compete to eat the most meatballs in 10 minutes. There are six heats, and a then final. The winner of the gets the pot.\n", "It’s the annual Ferret-legging Endurance competition. In the sport of ferret-legging, competitors tie their trousers at the ankles before placing two ferrets inside and securely fastening their belts to prevent the ferrets from escaping. Each competitor then stands in front of the judges for as long as he can. Competitors cannot be drunk or drugged, nor can the ferrets be sedated. In addition, competitors are not allowed to wear underwear beneath their trousers which must allow the ferrets free access from one leg to the other and the ferrets must have a full set of teeth that must not have been filed or otherwise blunted. The winner is the person who lasts the longest.\n", "In the annual Bonny Beard Competition, the most elaborately styled beard, as judged by the patrons, nets the winner a night of free drinks. The losers have to shave their beards off.\n", "The Annual Greased Piglet Game requires that a 15x15ft pen is set up in the tavern. Participants pay a small fee to compete to catch a lard greased piglet in the quickest time. The winner keeps the piglet.\n", "A crossbow bolt crashes through the window and strikes a merchant who came to the city from far away.\n", "You hear an explosion from across the tavern. The blast knocked out a male gnome for 1d6 minutes. Once the gnome wakes up he starts madly raving, saying things like ‘I was so close!’ and ‘that was my last chance.’ and ‘it’s too late now.’\n", "A ventriloquist starts preforming. The puppet looks very old and is wearing clothes that were quite fashionable about a century ago. The performance satirizes current events and culture and has the whole tavern laughing, but if you are observant for about half an hour, whenever the ventriloquist suggests wrapping up the performance the puppet dismisses his concerns. The show goes on for three hours until the puppet is finally satisfied, at which point the ventriloquist is extremely tired and looks terrified.\n", "It’s a only milk tavern, including milk derivatives.\n", "Off in the corner a group is gathering around an intense card game. At the table are a wise cracking dwarf, an elf who invented ‘poker face’, and a burly half orc about to loss all him gold.\n", "An old, friendly sea-hag offers a free sample of stew, with more to come if the taster guesses the secret ingredient. The stew gives a positive magical boon on a DC15 CON save and a negative effect on a failure.\n", "As the party walks in they hear a Bard who is recounting there recent adventures as if he was there for all of them. (This is good for a low renown party as it adds an air of mystery).\n", "An old man can be overheard telling a ragtag group of mixed races about a dungeon. After some discussion, and a handshake, he hands them a map.\n", "An old man challenges you to a game of wizard’s chess. The wooden pieces are enchanted, gesturing and shouting as they fight, though you can’t make out what they say. It is fascinating to watch. The man promises who can win from him will win the chess set, though if you lose, it will not be easy to stop playing. He offers no further explanation. (If you lose, you become a chess piece, trapped in the game).\n", "A puritan priest comes in and berates the patrons for their behavior, preaching a path of holiness and purity. The old innkeep tells him ‘Yer aff yer heid, ya wee bawface!’ and proceeds to flash her boobs at him. The priest flees in horror, muttering protective chants.\n", "It’s ‘Bear Night’. There are mounted bear heads on the wall, bear furs on the chairs and your drinks are served in bear-decorated goblets. After a while you begin to notice the bar is packed exclusively with hairy middleaged men, who are all acting rather familiar with each other…\n", "There’s a haggis eating competition. Winner gets free whisky till sunrise.\n", "A scruffy looking man slips something into a drink before returning to the woman at his table.\n", "It’s a busy night and the bar is packed. Suddenly everyone turns around as several squealing greased pigs are released into the tavern. They have numbers painted on their backs. The staff begins chasing them to much hilarity of the patrons. After a while, they have caught the pigs numbered 1, 2 and 4 but there is no sign of number 3.\n", "All the windows of the Inn slam open as the candle light dims, only to be undone a few moments later. Then a small girl stands and shouts her apologies for the disturbance.\n", "Knife throwing competition! D20+DEX: 1-10 miss the target. 10-14 outer ring. 14-18 middle ring. 18-19 inner ring. 20 bullseye. 3 throws each. PCs can play each other or NPCs for gold / rewards etc.\n", "It’s a two for one special night and the tavern is packed, making easy targets for thieves and pickpockets.\n", "A drunk half-orc starts taunting the innkeeper, who’s cut him off.\n", "The tavern has a black board on one of the walls, with the names of each person present, and current bets. It’s a deadpool, in which people bet on your death.\n", "There’s a discussion going on at the bar. One of the customers seems to be underage, and the bartender won’t get them a drink, unless he sees something that confirms they’re old enough to drink. The customer has a way to prove that, but made a bet with the other customers, giving 10 gp to each one that gets it right, and takes 10gp from each who gets it wrong.\n", "A group of exquisitely dressed people walk into the tavern, judging people’s outfits, generally in a negative way.\n", "A portal opens in the middle of the tavern. A man wearing pajamas comes out of it, orders a drink, and leaves through the portal, that closes behind him. If the players ask anyone, they will just say he shows up sometimes.\n", "The tavern’s owner runs into the tavern, saying they won the lottery, and will get everyone free drinks.\n", "A fight breaks out, between two big strong men. The bartender sighs, and gives each a free drink, separating them.\n", "The customers are all looking over their shoulders, with small smiles on their faces, and seem ready to… do something. Suddenly, someone screams ‘FOOD FIGHT!’ and everyone starts throwing food at each other. In the end, the owner gets pissed, and makes everyone clean up the mess.\n", "The tavern is hosting a weekly poker tournament. If the players win, they get gold and gossip possibly leading to a quest.\n", "A man in a dark trench coat is skulking in the back, selling contraband to anyone who asks.\n", "A man in a dark trench coat is skulking in the back, selling contraband to anyone who asks. However, he is part of a sting, and the local guard snatches up the buyers on their way out of the tavern.\n", "Someone playing the knife-fingers stabbing game accidentally stabs their own hand, possibly cutting off a finger.\n", "One of the patrons has gathered a sizable crowd with their exotic pet and its tricks.\n", "The local militia captain busts down the door and grabs the innkeeper, placing him under arrest for an unknown reason.\n", "Two drunken wizards come to blows over a perceived slight. Parts of the tavern catch fire or are otherwise affected by magical effects.\n", "A shadowy figure enters and orders a drink. The only problem is, there seem to be a mass of tentacles where feet should be.\n", "This tavern exists in multiple dimensions, it has at least 20 different doors which connect to the outside world, but as you guessed, different ones. The owner is a mad wizard with the longest and most unkempt beard youve ever seen. Over each of the entries, there is a sign to where it leads. One of the doors is barred and kept shut at all times, the sign reads: dont open, dead inside.\n", "Tonight’s the local Battle of the Bards, where the prize pool includes a set of fine platinum strings.\n", "The first batch of beer from the halfling brewery in the next town is very lively. A bit too lively. A tide of hoppy foam bursts from the barrel and up into the bar, showing no signs of slowing down.\n", "After a few drinks, you could swear all the patrons in the bar have the exact same face. You shake your head. Must be the wine.\n", "The barkeep here has a very literal approach to lock-ins. Sure, you can drink past closing time—as long as you didn’t want to leave again, ever.\n", "The Tavern menu has a ‘Mystery Special’. When ordered it is a large stack of pancakes covered in various fruit that looks like a big smiling face. When eaten the player is reminded of their mother/father/paternal guardian.\n", "A female drow in common clothes and a big hat (to block the sun) walks into the tavern and an uncomfortable silence ensues. After it is clear that the drow doesn’t want any trouble the tavern slowly goes back to normal and the drow woman orders a drink and sits down with a wealthy half elf merchant.\n", "A wrestling ring has been erected in the middle of the tavern. The current champion drinks nearby, and accepts all challengers.\n", "An old drow tells stories about his long life in the Underdark. He tells tales of other drow, kuo toa, mind flayers, flumphs, and even a purple worm he encountered.\n", "The local beastmaster has arranged an animal show. He starts off with a raven, a giant frog, and a blood hawk. He finishes with a bulette, an owlbear, and a displacer beast. Each animal loves him like a family member.\n", "Part of the tavern is under construction after a battle or large fight. Builders are constantly moving planks of wood between tables and sometimes hitting patrons. Roll improvised weapon attacks vs players AC at various points in the visit.\n", "The inn is flooded with people. Survivers of a battle not far off. Some seem to only have superficial wounds while others are not as lucky. Over the sounds of heavy breathing and mouning the party hears a voice ring out ‘CLERIC!! We need a cleric!’\n", "A health inspector busts in and attempts to shut the bar down due to health code violations.\n", "Inside the Tavern the party finds about 60 people stuffed inside this small three room tavern all gathered around the bar. The tavern just recently hired a barmaid to work full time.\n", "After several drinks the party realizes that they’re the only non-monster creatures in the tavern.\n", "After several minutes inside the tavern the party can hear a thunder storm rolling into the area. The whether gets increasing worse the longer they stay inside, and after 45 minutes a tree crashes into the side of the tavern.\n", "A religious group comes inside to preach about the sin of consuming alcohol.\n", "The musicians plating inside the tavern draw in a large enough crowd that the that the bartenders have to start kicking people who are to drunk.\n", "After the party sits down for a drink or two, a group of guards come inside searching for several highway robbers. The robbers descriptions match those of the party members; so they’er handcuffed, dragged to prison, waiting for a trial.\n", "The Half-Orc chef near a large fire pit offers the party a sample of the roasting boar he has over a spit.\n", "A Tabaxi hunter set up in the corner offers to sell the party wild pheasants and other game birds for the Tavern cook to make.\n", "Two Warforged start fighting one another. Watch out for their partner the Gnome pickpocket. She’s the brains of the operation.\n", "A fire elemental moves into the hearth!\n", "This is a thieve’s guild’s secret hideout in plain sight. Tonight, the corpses of the dead they left beneath the floorboards arise!\n", "The tavernkeep is a vampire. One of his servants accidentally begins pouring a bottle of his finest blood.\n", "A group of overzealous paladins springs a sudden raid on the tavern, breaking casks and arresting people, slamming them into cage-carts they parked in the back.\n", "One of the patrons is a werewolf, and he begins to turn.\n", "An ancient legend is (figuratively) brought to life by a traveling team of a bard and an illusion wizard.\n", "Once a month the neighboring warlords meet in this tavern to discuss… literature.\n", "Tavern is holding bar tending classes once a week to train new staff as well as supply competent labor to the noble houses – top of the class gets to pick their assignment.\n", "Tavern acts as a clearinghouse for counterfeit currency. Next shipment arrives two days from today.\n", "A polymorphed silver dragon walks in, orders a drink with no ice, and then he just frosts up his drink whenever. He only has one drink, and when he finishes his drink, you can see him switching from creature to creature , but only minorly.\n", "The tavern begins a ‘you break it, we hire a bounty hunter to make you pay’ policy today. No one wants to be the first person to break the rule.\n", "That Elven barmaid, that’s been slapped on the ass one to many times, turns out to be a shapeshifter. And she’s just transformed into a raging ogre.\n", "A notorious criminal duo known as the Grimshade Brothers have arrived to the tavern to celebrate which is in the neighboring village of the city they just robbed. Their known for robbing banks and causing mayhem wherever they go.\n", "Two goblins are on stage doing a juggling act. The juggling act involves flaming torches, hand axes, and vials of strange green goo. No one seems concerned.\n", "A love potion is accidentally slipped into one of your party’s drinks instead of the beautiful lady at the next table….\n", "It is a roast night. Have the players take turns roasting either each other’s characters, or the DM.\n", "A talent agent is holding auditions for the midwinter festival play. Bonus points for singing and dancing!\n", "After 1d6 drinks gravity seems to hold no sway over the bar patrons. Everyone starts to float and the regular drinks keep drinking on the ceiling as if this is a normal occurrence.\n", "Book signing for the new release ‘Quest for Annihilation : How Adventuring is Destroying Our Moral Fabric’\n", "The drunk mage in the corner is passed out and talking in his sleep. Roll for wild magic effect.\n", "The tavern is about to run out of ale. Your party is discretely asked to procure some more within 1d4 hours to avoid a riot.\n", "A member of your party is mistaken for a local celebrity. People are constantly asking for autographs etc for the whole night.\n", "It’s the owners birthday! Reduced drink prices and free cake!\n", "You stumble into the middle of a wake, complete with the body of the deceased on ice next to the bar. Bonus points if that’s the ice used in the drinks!\n", "The owner makes it very clear he don’t want no trouble in his bar. Will not serve adventurers if they don’t relinquish their weapons.\n", "The barkeep leaves a single coin with a tiny dragon at your table, he says ‘be sure to spend him quick, he likes to travel’ the dragon is friendly but will not separate from the coin."]
        event = random.choice(barevents)
        await client.send_message(get_channel('yawning-portal'), event)
        randlist = ('Settlers of Catan','Dungeons and Dragons','Risk','Hero Quest','Adventure','Magic the Gathering','Joust','Ms Pac Man','Robocop', 'Star Realms', 'Joust', 'War Hammer', 'Donkey Kong', 'Asteroids', 'Tetris', 'Tempest', 'Paperboy', 'Battle Zone', 'Donkey Kong Jr.')   
        await client.change_presence(game=Game(name=(random.choice(randlist))))
  
        await asyncio.sleep(21600)   # Sleep for 6 hours
    
            
       
client.loop.create_task(background_loop())  # Sets background loop


#'''

client.run('Input Key Here')

