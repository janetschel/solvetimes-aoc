import json
import time
import datetime

with open("times.txt") as file:
    json_data = json.loads(file.read())

members = json_data["members"]

def solve_time_from_ts(ts, day) -> str:
    dt: datetime = datetime.datetime(2020, 12, int(day), 0, 0)
    ut: int = int(time.mktime(dt.timetuple()))
    diff: int = (int(ts) - ut)

    hours_since_midnight = datetime.timedelta(seconds=diff)
    solve_time = hours_since_midnight - datetime.timedelta(hours=6)

    return f"{solve_time}, at: {hours_since_midnight}"


def diff_between_parts(parts) -> str:
    diff = int(parts[str(2)]["get_star_ts"]) - int(parts[str(1)]["get_star_ts"])
    to_part1 = datetime.timedelta(seconds=diff)

    return f"(diff to part 1: {to_part1})"


def format_member(member_num: int):
    member = members[str(member_num)]

    print("\nTimes for '", member["name"], "':", sep="")

    completions = member["completion_day_level"]
    for day in range(1,25):
        try:
            parts = completions[str(day)]
        except:
            break

        for part in range(1,3):
            solve_time = parts[str(part)]["get_star_ts"]
            print("day", day, "part", part, "-> ", end="")
            print(f"{solve_time_from_ts(solve_time, day)} ", end="" if part == 2 else "\n")

            if part == 2:
                print(diff_between_parts(parts))
        

for member_num in members:
    format_member(member_num)