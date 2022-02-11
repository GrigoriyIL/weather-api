# Weather-api
Rest api that allows you to track the weather for the next few days in Kiev and other cities available in Gismeteo.

The following options are available for the /api/ endpoint:
location: city location for example weather-kyiv-4944
day: number of days, maximum 9, default 3

## :scroll: Table of contents
1. [Requirements and Preparation](#electric_plug-requirements-and-preparation)
2. [Installation](#hammer_and_wrench-installation)
3. [Commands](#tada-commands)

## :electric_plug: Requirements and Preparation
The system requires Docker and Docker Compose for development.
It is recommended to use GNU/Linux operating system (Debian, Ubuntu, etc.).

## :hammer_and_wrench: Installation
1. Open the command prompt.
3. Run `make init`
5. You are great, and can start working.

## :tada: Commands
- `make init` — Initialize development environment.
- `make up` — Start development environment.
- `make down` — Stop development environment.
- `make restart` — Restart development environment.