# icsproxy

Simple proxy for facebook ICS calendar file, because sometimes the google calendar is unable to parse a ics file.
It occurs, when ORGANIZER field has a quotation mark (") inside, which breaks the parser.

## Usage

1. Copy `.env.example` into `.env`, and put your calendar url taken from facebook
2. `docker-compose up -d`

