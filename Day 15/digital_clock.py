from datetime import datetime

now = datetime.now()

print(f"Date: {now.strftime('%d/%m/%Y')}")
print(f"Time: {now.strftime('%H:%M:%S')}")