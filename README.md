# Discord-Bot-Vorlage (Python, discord.py)

Minimaler Discord-Bot mit einem Slash-Befehl `/ping`. Zum Lernen, Testen und als Ausgangspunkt für eigene Bots. MIT-Lizenz.

## Lokal starten

1. Im [Discord Developer Portal](https://discord.com/developers/applications) eine Anwendung mit Bot anlegen und den Token kopieren.
2. Bot mit dem Scope `applications.commands` auf deinen Server einladen.
3. Abhängigkeiten installieren und starten:

```bash
pip install -r requirements.txt
export DISCORD_TOKEN=dein-token   # Windows PowerShell: $env:DISCORD_TOKEN="dein-token"
python bot.py
```

Der Token gehört nie in den Code oder in ein öffentliches Repository. Die Datei `.env.example` zeigt nur den Namen der Variablen.

## Rund um die Uhr online

Auf dem eigenen PC ist der Bot nur online, solange der Rechner läuft. Für Dauerbetrieb braucht er einen Server. Diese Vorlage läuft unverändert bei jedem Anbieter, der Python 3.11 oder neuer und eine Umgebungsvariable `DISCORD_TOKEN` unterstützt.

Anleitungen auf Deutsch:

- [Discord-Bot mit Python hosten](https://ventrohosting.com/anleitungen/discord-bot-python-hosten)
- [Discord-Bot kostenlos hosten: Möglichkeiten und Grenzen](https://ventrohosting.com/anleitungen/discord-bot-kostenlos-hosten)
- [Discord-Bot 24/7 online halten](https://ventrohosting.com/anleitungen/discord-bot-247-online)

Hinweis: VentroHosting ist ein unabhängiger Anbieter und nicht mit Discord Inc. verbunden.
