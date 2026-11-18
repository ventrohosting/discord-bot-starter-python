import os

import discord
from discord import app_commands

TOKEN = os.environ.get("DISCORD_TOKEN")
if not TOKEN:
    raise SystemExit("Kein Token gesetzt: Umgebungsvariable DISCORD_TOKEN fehlt.")


class Bot(discord.Client):
    def __init__(self) -> None:
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        # Registriert die Slash-Befehle bei Discord (global; kann einige Minuten dauern).
        await self.tree.sync()


bot = Bot()


@bot.tree.command(name="ping", description="Antwortet mit Pong und der Latenz")
async def ping(interaction: discord.Interaction) -> None:
    await interaction.response.send_message(f"Pong! {round(bot.latency * 1000)} ms")


@bot.event
async def on_ready() -> None:
    print(f"Bot ist online als {bot.user}")


bot.run(TOKEN)
