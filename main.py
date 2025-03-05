import discord 
from discord.ext import commands 
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def upload_image(ctx):
    if len(ctx.message.attachments) == 0:
        await ctx.send("No se entrego ninguna imagen :c")
    else:
        # Iterar sobre los archivos adjuntos
        for attachment in ctx.message.attachments:
            if attachment.filename.endswith(('jpg', 'jpeg', 'png')):
                #guardar imagen sistema local
                filepath = f"images/{attachment.filename}"
                await attachment.save(filepath)

                #enviar la URL de la imagen de vuelta al usuario
                await ctx.send(f"Imagen {attachment.filename} guardada con exito. Disponible en: {attachment.url}")
            else:
                await ctx.send(f"El archivo {attachment.filename} no es un archivo valido.")
bot.run("token")
