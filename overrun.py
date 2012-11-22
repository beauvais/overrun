#!/usr/bin/env python

discussion = {}

discussion['Peter'] = 45

discussion['Paul'] = 30

discussion['Simon'] = 20

discussion['Mark'] = 30


def talk_time(argv):
    count = 0
    remaining = sum(argv.values())
    print("OK, we are ready to start." + "\n")
    for k, v in argv.items():
        print(str(k) + " starts talking when session has been going for " + str(count) + " minutes.")
        count += v
        remaining -= v
        if remaining > 0:
            print("after " + k + ", the session has: " + str(remaining) + " minutes to go")
        elif remaining < 0:
            over = remaining * -1
            print over
            print("... and we ran over by " + over + " minutes!")
        else:
            pass


print(talk_time(discussion))
