import discord
from discord import app_commands
from discord.ext import commands


class General(commands.Cog):
    """Allgemeine Beispielbefehle."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="ping", description="Antwortet mit Pong und der Latenz")
    async def ping(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f"Pong! {round(self.bot.latency * 1000)} ms")

    @app_commands.command(name="info", description="Zeigt Informationen zu diesem Server")
    @app_commands.guild_only()
    async def info(self, interaction: discord.Interaction) -> None:
        guild = interaction.guild
        embed = discord.Embed(title=guild.name)
        embed.add_field(name="Mitglieder", value=str(guild.member_count))
        embed.add_field(name="Erstellt", value=discord.utils.format_dt(guild.created_at, "D"))
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(General(bot))
