import psutil

print(psutil.net_connections(kind='inet4'))
