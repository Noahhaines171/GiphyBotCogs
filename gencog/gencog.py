from redbot.core import commands


# Classname should be CamelCase and the same spelling as the folder
class GenCog(commands.Cog):
    """Description of the cog visible with [p]help MyFirstCog"""

    @commands.command()
    async def gen_cog(self, ctx):
        """Description of myfirstcom visible with [p]help myfirstcom"""
        # Your code will go here
        await ctx.send("My first cog!")
