from datetime import datetime

now = datetime.now()

print(now)

print(str(datetime.now()))

print(datetime.now().timestamp())

filename = f"report_{datetime.now().timestamp()}.json"
print(filename)