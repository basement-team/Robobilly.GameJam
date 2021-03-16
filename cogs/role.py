import discord
from discord.ext import commands


class role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    async def get_jam_role(self, guild):
        """
        fetches and returns the gamejam role.
        """
        jam_role = discord.utils.get(guild.roles, name='Basement GameJam 2021')
        if jam_role is None:
            jam_role = await guild.create_role(name='Basement GameJam 2021')

        return jam_role
    

    @commands.command(name="gamejam", aliases=["GameJam", "Gamejam", "gj"])
    async def game_jam(self, ctx):
        """
        gives the gamejam role to the user.
        """
        await ctx.author.add_roles(await self.get_jam_role(ctx.guild))
        embed = discord.Embed(color = discord.Color.green())
        embed.add_field(name="Role Added 🎉", value="you've got the game jam role!")
        await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(role(bot))