import discord
import asyncio
import CobraMusic

client = discord.Client()
BAN_WORDS= ["pokeball","carapuce","dresseurs","javascript","giratina","yeet"]

"""
Commandes possibles:
    - !hello
    - !carapuce
    - !embed
    - !play url_vidéo

    - Mot banni --> mp d'averissement
"""


@client.event
async def on_ready():
  print("Capitaine Salamèche à la rescousse !")

@client.event
async def on_message(message):
  print(message.content)


  if message.content=="!hello":
    member_name = message.author.name
    guild_name = message.guild.name
    new_msg = await message.channel.send("Salut "+member_name+". Tu te trouves sur "+guild_name)
    await new_msg.pin()


  if message.content=="!carapuce":
    await message.channel.send("OH NO")


  if message.content=="!embed":
    em = discord.Embed(title="titre", description="description (wow c'est fou)", colour=0xFF0000, timestamp=message.created_at)
    em.add_field(name="Un field", value="Youpi", inline=True)
    em.add_field(name="Un autre field", value="o/", inline=True)
    em.add_field(name="Un field pas sur la même ligne", value="grace au 'inline'", inline=False)
    em.set_author(name="Un gars super", icon_url=message.author.avatar_url)
    em.set_footer(text="Sur un super serveur", icon_url=message.guild.icon_url)
    em.set_image(url="https://cdn.discordapp.com/attachments/"+"567630033246617621/581496185424969749/1733852_0.jpg")
    await message.channel.send(embed=em)

  if message.content!="!carapuce":
    msgNO=False
    for word in BAN_WORDS:
      if word in message.content.lower():
          msgNO=True
          break
    if message.author != client.user and msgNO==True:
      print("ALERTE: MOT INTERDIT UTILISE")
      await message.delete()
      ID= message.author.id
      print(ID)
      await message.author.send("ATTENTION : Sur le serveur"+ message.guild.name +", vous avez envoyé le message : "+ message.content +". Ce message contient le mot interdit "+ word +". Veuillez ne pas renvoyer de message contenant de mot interdit sur ce serveur")


  if "!play " in message.content:
    split= message.content.split(" ")
    print(split)
    music_client = await CobraMusic.get_client(message, client)
    await music_client.play(split[1])

client.run ("TOKEN")