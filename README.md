# Discord-Bot-Vorlage (Python, discord.py)

Solide Ausgangsbasis für einen eigenen Discord-Bot: Slash-Befehle, Cogs (jede Datei in `cogs/` wird automatisch geladen), Dockerfile und CI. MIT-Lizenz, deutsch dokumentiert.

*English: A small, clean discord.py starter with slash commands, auto-loaded cogs, Dockerfile and CI. German docs, MIT licensed.*

## Inhalt

- [Voraussetzungen](#voraussetzungen)
- [Schnellstart](#schnellstart)
- [Projektaufbau](#projektaufbau)
- [Eigenen Befehl hinzufügen](#eigenen-befehl-hinzufügen)
- [Mit Docker starten](#mit-docker-starten)
- [Rund um die Uhr online](#rund-um-die-uhr-online)
- [Häufige Fehler](#häufige-fehler)

## Voraussetzungen

- Python 3.11 oder neuer
- Eine Anwendung mit Bot im [Discord Developer Portal](https://discord.com/developers/applications)

## Schnellstart

1. Anwendung anlegen, unter **Bot** den Token zurücksetzen und kopieren.
2. Unter **OAuth2 › URL Generator** die Scopes `bot` und `applications.commands` wählen und den Bot auf deinen Server einladen.
3. Projekt holen und starten:

```bash
git clone https://github.com/ventrohosting/discord-bot-starter-python.git
cd discord-bot-starter-python
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
export DISCORD_TOKEN=dein-token                       # PowerShell: $env:DISCORD_TOKEN="dein-token"
python bot.py
```

In der Konsole erscheint „Bot ist online als …“. Auf deinem Server funktionieren jetzt `/ping` und `/info`.

Der Token gehört nie in den Code und nie in ein öffentliches Repository.

## Projektaufbau

```
bot.py            Start, lädt alle Cogs und registriert die Slash-Befehle
cogs/general.py   Beispielbefehle /ping und /info
```

## Eigenen Befehl hinzufügen

Lege eine neue Datei in `cogs/` an, zum Beispiel `cogs/hallo.py`:

```python
import discord
from discord import app_commands
from discord.ext import commands


class Hallo(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="hallo", description="Sagt Hallo")
    async def hallo(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f"Hallo {interaction.user.display_name}!")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Hallo(bot))
```

Nach einem Neustart registriert der Bot den Befehl automatisch.

## Mit Docker starten

```bash
docker build -t mein-bot .
docker run -d --name mein-bot --restart unless-stopped -e DISCORD_TOKEN=dein-token mein-bot
```

## Rund um die Uhr online

Auf dem eigenen PC ist der Bot nur online, solange der Rechner läuft. Für Dauerbetrieb brauchst du einen Rechner, der nie ausgeht: einen Raspberry Pi, einen eigenen Server oder einen Bot-Hoster. Die Vorlage läuft unverändert überall, wo Python 3.11 oder neuer und die Umgebungsvariable `DISCORD_TOKEN` zur Verfügung stehen.

Offenlegung: Dieses Repository pflegt [VentroHosting](https://ventrohosting.com), ein Anbieter für Discord-Bot-Hosting. Die Vorlage ist unabhängig von jedem Anbieter nutzbar. Passende Anleitungen auf Deutsch:

- [Discord-Bot mit Python hosten](https://ventrohosting.com/anleitungen/discord-bot-python-hosten)
- [Discord-Bot erstellen und einladen](https://ventrohosting.com/anleitungen/discord-bot-erstellen)
- [Discord-Bot kostenlos hosten: Möglichkeiten und Grenzen](https://ventrohosting.com/anleitungen/discord-bot-kostenlos-hosten)
- [Discord-Bot 24/7 online halten](https://ventrohosting.com/anleitungen/discord-bot-247-online)
- [Discord-Bot-Hosting vergleichen: Checkliste](https://ventrohosting.com/anleitungen/discord-bot-hosting-vergleichen)
- [Kostenloser Discord-Timestamp-Generator](https://ventrohosting.com/tools/discord-timestamp-generator) und [Embed-Generator](https://ventrohosting.com/tools/discord-embed-generator)

## Häufige Fehler

| Meldung | Ursache |
|---|---|
| `Kein Token gesetzt` | `DISCORD_TOKEN` ist nicht gesetzt. |
| `Improper token has been passed` | Der Token ist falsch oder wurde zurückgesetzt. |
| `PrivilegedIntentsRequired` | Der Code nutzt einen Intent, der im Developer Portal unter **Bot** nicht aktiv ist. Diese Vorlage braucht nur die Standard-Intents. |
| Slash-Befehle erscheinen nicht | Nach der ersten Registrierung kurz warten, Discord neu laden und prüfen, ob der Bot mit `applications.commands` eingeladen wurde. |
| `ModuleNotFoundError` | `pip install -r requirements.txt` ausführen. |

Weitere Fehler und Lösungen: [Discord-Bot offline? Häufige Fehler](https://ventrohosting.com/anleitungen/discord-bot-offline-fehler).

Hinweis: VentroHosting ist ein unabhängiger Anbieter und nicht mit Discord Inc. verbunden.
