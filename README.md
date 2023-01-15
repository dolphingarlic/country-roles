# Country Roles
A Discord bot to add country roles functionality to your Discord server.

## Features
- Adds all of the countries listed in `countries.py` as roles in your discord server.
- Allows server members to add a single country role, via slash commands.
- Send a list of other members with the same country role as you via DM

## Instructions
- Run `/start` as a server administator to add the country roles to the server.
- Run `/reset` as a server administator to remove the country roles from the server.
- the above commands can cause Discord to throttle you for some time, so please run those commands with care.
- `/country` followed by the country name or flag emoji will add that role to the member invoking the command
- `/countries` lists all accepted country names. Countries need to be specified exactly as shown in this list.
- `/nearme` will DM a list of other server members with the same country role as you.

## Customisation
- Edit `countries.py` if you wish to add/remove countries/regions. Make sure that all country roles have been removed from your server before doing so, as a difference between this file and your server's roles can result in country roles being incorrectly added/removed. Manually having to deleted country roles is a tedious task.
- remove features by commenting out that slash command block in `county_roles.py`

## Prerequisites
- [Pycord] v2.3.2 - a modern, easy to use, feature-rich, and async ready API wrapper for Discord, written in Python. At the time of writing v3 is in development and will create **breaking changes** if used.

## Installation
You must self host this bot in order to use it.
- Create a new application and bot at the [Discord Developer Portal](https://discord.com/developers/applications). Follow this [guide](https://realpython.com/how-to-make-a-discord-bot-python/) if you are unsure.
- create a local .env file to store `DISCORD_TOKEN`. Add both your bot's secret token to this file as `DISCORD_TOKEN=xxxxxxx`
- Enable the bot permissions 'Manage Roles, 'Send Messages', 'Use Slash Commands'
- Host the files on your platform of choice, adding `DISCORD_TOKEN` to the platform's environment variables.

## Development
Want to contribute? Simply fork, clone, edit and then create a pull request. Details of how to do this can be found [here](https://www.digitalocean.com/community/tutorials/how-to-create-a-pull-request-on-github).


## Credits
- [Country Roles](https://github.com/dolphingarlic/country-roles) by [dolphingarlic](https://github.com/dolphingarlic), from which this project was forked. I first converted this original codebase to utilise Discord's slash commands, before adding more functionality.

## License
MIT

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [git-repo-url]: <https://github.com/TheRealOwenRees/country-roles>
   [Pycord]: <https://pycord.dev/>
   [GBIF]: <https://pypi.org/project/python-dotenv/>
   [PFAF]: <https://pfaf.org>
   [python-dotenv]: <https://pypi.org/project/python-dotenv/>