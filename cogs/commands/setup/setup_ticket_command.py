import discord
from discord.ext import commands
from discord import app_commands

from cogs.ticket_system import TicketMenuView, emoji, images, color
from main import config


class setup_ticket_command(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    
    @app_commands.command(name="setup-ticket", description="Erlaubt es dir die Ticket embed in diesem Kanal zu erstellen")
    @app_commands.guild_only()
    @app_commands.guilds(int(config["guild_id"]))
    @app_commands.default_permissions(administrator=True)
    async def setup_ticket(self, interaction: discord.Interaction):
        await interaction.response.send_message("✅ Ticket-Embed erfolgreich gesendet.", ephemeral=True)
        embed = discord.Embed(title=f"{emoji["mail"]} TICKET SUPPORT", description="> **Ticket Support Informationen**\n> - Die Wartezeit beträgt 0-48h\n > - Nutze die Tickets nur für Angebrachte Dinge. Die Fehlnutzung dieses Systems kann Folgen haben.\n\n> **Wie öffnet man ein Ticket?**\n > - Klicke auf das Menü unten und wähle die Kategorie aus, in die dein Ticket fällt, danach wird sich ein Ticketkanal für dich öffnen.\n> - Bitte habe etwas geduld, bis ein Teammitglied sich dort meldet.", color=color["grey"])
        embed.set_image(url=images["grey_ticket_line"])
        await interaction.channel.send(embed=embed, view=TicketMenuView(self.client))

async def setup(client:commands.Bot) -> None:
    await client.add_cog(setup_ticket_command(client))