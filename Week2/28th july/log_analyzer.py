#log analyzer
logs = [
    ("2026-06-19 10:00", "INFO", "Model Loaded"),
    ("2026-06-19 10:05", "ERROR", "API Timeout"),
    ("2026-06-19 10:08", "WARNING", "High Memory"),
    ("2026-06-19 10:10", "INFO", "Prediction Completed"),
    ("2026-06-19 10:12", "ERROR", "API Timeout"),
    ("2026-06-19 10:15", "INFO", "Prediction Completed"),
    ("2026-06-19 10:18", "ERROR", "Database Connection Failed"),
    ("2026-06-19 10:20", "WARNING", "Disk Usage High"),
    ("2026-06-19 10:25", "INFO", "Model Reloaded"),
    ("2026-06-19 10:30", "ERROR", "API Timeout")
]

#Store all ERROR log messages in a new list.
print("Display of all erroe messages")
errors=[]
for error in logs:
    if error[1]=="ERROR":
        errors.append(error)
print(errors)
print("")

#Store all timestamps of WARNING logs.
print("Display of all warning messages")
warning_log=[]
for warning in logs:
    if warning[1]=="WARNING":
        warning_log.append(warning)
print(warning_log)
print("")

#Print each log using tuple unpacking.
print("Printing each log using tuple unpacking.")
for tup in logs:
    time_stp,lev,msg= tup
    print("Time stamp:",time_stp)
    print("Messages:",lev)
    print("Log:",msg)
    print("")

#Find all unique log levels.
levels=set()
print("Unique log levels in the logs")
for tup in logs:
    time_stp,lev,msg= tup
    levels.add(lev)
print(levels)
print("")

#Find unique error messages.
print("To Find unique error messages.")
error_msg=set()
for err in logs:
    if err[1]=="ERROR":
        time_stp,lev,msg= err
        error_msg.add(msg)
print(error_msg)
print("")

#To Count the number of logs for each level.
print("Counting the no. of logs for each level.")
lev_count={}
for tuple in logs:
    time_stp,lev,msg= tuple
    if lev in lev_count:
        lev_count[lev]+=1
    else:
        lev_count[lev]=1
print(lev_count)
print("")

#Count each error message.
err_count={}
for tuple in logs:
    time_stp,lev,msg=tuple
    if lev=="ERROR":
        if msg in err_count:
            err_count[msg]+=1
        else:
            err_count[msg]=1
print(err_count)
print("")

#Extract all INFO messages.
print("To Extract all INFO messages.")
info_msg=set()
for tuple in logs:
    time_stp,lev,msg=tuple
    if lev=="INFO":
        info_msg.add(msg)
print(info_msg)
print("")

#Extract all timestamps.
print("To extract all timestamps")
time_stamp=[]
for tuple in logs:
    time_stp,lev,msg=tuple
    time_stamp.append(time_stp)
print(time_stamp)
print("")

#Create a dictionary with log level as key and count as value.
count={}
for tuple in logs:
    time_stp,lev,msg= tuple
    if lev in count:
        count[lev]+=1
    else:
        count[lev]=1
print(count)
print("")

#Convert all log messages to uppercase.
print("Log messages to uppercase.")    
for tuple in logs:
    time_stp,lev,msg= tuple
    print(msg.upper())
    print("")

#Extract only the date from each timestamp.
print("To extract date from timestamp")
for tuple in logs:
    time_stamp,lev,msg=tuple
    date = time_stamp.split()[0]
    print(date)
print("")

#Filter logs whose message contains the word "Model".
print("Message with the word 'model'")
for tuple in logs:
    time_stamp,lev,msg=tuple
    if "Model" in msg:
        print(tuple)

