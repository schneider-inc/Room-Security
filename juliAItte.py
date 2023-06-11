from time import sleep

from play_voice import voice
from school import school_reminder

# will just remind you when certain events take place
# for now just school day schedule
# FUTURE: perhaps support for getting a rundown of today's activities

while not (to_voice:=school_reminder())[0]:
    print("Nope, not yet")
    sleep(1)

print("yarrrrr, she blows!")
voice("23h 30min Musik BEGINN")
