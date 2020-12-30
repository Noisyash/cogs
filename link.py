from redbot.core import commands

class link(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def link(self, ctx, arg):
        name = ctx.message.author.id
        with open('userlist.yaml','a') as yaml_file:
            yaml_file.write(str(name) + "." + arg + '\n')
        yaml_file.close()
        await ctx.send("steam id " + arg + " linked")
