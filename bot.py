import asyncio
import os
from pathlib import Path

import discord
from discord.ext import commands

TOKEN = os.environ.get("DISCORD_TOKEN")
if not TOKEN:
    raise SystemExit("Kein Token gesetzt: Die Umgebungsvariable DISCORD_TOKEN fehlt.")


class Bot(commands.Bot):
    def __init__(self) -> None:
        # Slash-Befehle brauchen keinen Message-Content-Intent.
        super().__init__(command_prefix=commands.when_mentioned, intents=discord.Intents.default())

    async def setup_hook(self) -> None:
        # Jede Datei in cogs/ ist eine Erweiterung mit einer setup()-Funktion.
        for file in sorted(Path(__file__).parent.joinpath("cogs").glob("*.py")):
            if not file.name.startswith("_"):
                await self.load_extension(f"cogs.{file.stem}")
        # Registriert die Slash-Befehle bei Discord (global; kann einige Minuten dauern).
        await self.tree.sync()

    async def on_ready(self) -> None:
        print(f"Bot ist online als {self.user}")


async def main() -> None:
    async with Bot() as bot:
        await bot.start(TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
