resp = requests.get("https://ntfy.sh/disk-alerts/json", stream=True)
for line in resp.iter_lines():
  if line:
    print(line)
