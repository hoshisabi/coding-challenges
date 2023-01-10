import csv

combined_schedule = {}
emails_sent = {}
ucon_schedule = {}

inits_to_names = {}
missing_dms = {}


# with open("./myschedule.csv") as mycsvfile:
#     myreader = csv.reader(mycsvfile)
#     for row in myreader:
#         print(",".join(row))

with open("./verify_emails.csv") as vecsvfile:
    vereader = csv.reader(vecsvfile)
    for row in vereader:
        al_code = row[0]
        start_time = row[1]
        event_id = row[2]
        dm_init = row[3]
        emails_sent[event_id] = {"al_code": al_code, "start_time": start_time, "dm_init": dm_init}

# 0 "Event Name"
# 1 "Event Number"
# 2 "Event Type"
# 3 "Host Names"
# 4 "Description"
# 5 "Price"
# 6 "Age Range"
# 7 "Max Tickets"
# 8 "Sold Count"
# 9 "Wait Count","Starts"
# 10 "Start Date (UTC)"
# 11 "Duration (minutes)"
# 12 "More Info"
# 13 "Room"
# 14 "Space"
# 15 "Date Created"
# 16 "Date Updated"
# 17 "View URI"
# 18 "Player Experience"
# 19 "Game Complexity"
# 20 "Minimum # of Players"
# 21 "Hosting Company, Group, or Club Name"
# 22 "Game System (without edition)"
# 23 "Game Edition"
# 24 "Table Size Request"
with open("./u-con-2022-schedule.csv", encoding="utf8") as uccsvfile:
    ucreader = csv.reader(uccsvfile)
    for row in ucreader:
        event_name = row[0]
        event_id = row[1]
        dm_name = row[3]
        start_time = row[10]
        if len(row) > 22:
            host_group = row[22]
            if host_group == "U-Con Adventurers League":
                ucon_schedule[event_id] = {"event_name": event_name, "dm_name": dm_name, "start_time": start_time}

for item in ucon_schedule:
    combined_schedule[item] = {}
    dm_init = ""
    dm_name = ""
    if item in emails_sent:
        combined_schedule[item]["al_code"] = emails_sent[item]["al_code"]
        dm_init = emails_sent[item]["dm_init"]
        combined_schedule[item]["dm_init"] = dm_init
        combined_schedule[item]["start_time"] = emails_sent[item]["start_time"]
    if item in ucon_schedule:
        combined_schedule[item]["event_name"] = ucon_schedule[item]["event_name"]
        dm_name = ucon_schedule[item]["dm_name"]
        combined_schedule[item]["dm_name"] = dm_name
        combined_schedule[item]["uc_start_time"] = ucon_schedule[item]["start_time"]
    inits_to_names[dm_init] = dm_name
    if dm_name == "Daniel E. Chapman II":
        missing_dms[item] = dm_init

print(inits_to_names)
print(missing_dms)
print(combined_schedule)
print(combined_schedule.values())
print(list(filter(lambda _: _["dm_init"] == "NR", combined_schedule.values())))
