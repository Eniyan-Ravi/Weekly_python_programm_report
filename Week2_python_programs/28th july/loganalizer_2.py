#log analizer problem 2
timestamps = ["2026-06-19 10:00","2026-06-19 10:05","2026-06-19 10:08"]
levels = ["INFO","ERROR","WARNING"]
messages = ["Model Loaded","API Timeout","High Memory"]

#Combine them into a list of tuples.
print("To combine list into tuples")
logs = []
for i in range(len(timestamps)):
    logs.append((timestamps[i], levels[i], messages[i]))
print(logs)
print("")

#Create a dictionary mapping timestamp to message.
print("To create dict with timestamp and message")
dic_logs={}
for i in range(len(timestamps)):
    dic_logs[timestamps[i]] = messages[i]
print(dic_logs)
print("")

#Print log number before each log.
print("To print log no.for each logs")
count = 101
for log in logs:
    print("Log", count, ":", log)
    count += 1
print("")

#Create a dictionary where key is log number and value is the log tuple.
print("Dict with log no. as key tuples as values")
log_dic= {}
count = 101
for log in logs:
    log_dic[count] = log
    count += 1
print(log_dic)
print("")

#Create a generator that yields one ERROR log at a time.
print("To create a generator for error logs")
def error_logs():
    for error in logs:
        if error[1] == "ERROR":
            yield error

g = error_logs()
for i in g:
    print(i)
print("")

#create a generator that yield one log record at a time 
def log_rec():
    for lo in logs:
        yield lo
log_records=log_rec()
for x in log_records:
    print(x)