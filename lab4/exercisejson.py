import json
json_path = r"C:\Users\HP\Downloads\sample-data.json"
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print("-" * 80)
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes.get("descr", "")  # Если нет описания, оставляем пустым
    speed = attributes.get("speed", "inherit")  # Если нет значения, указываем inherit
    mtu = attributes.get("mtu", "9150")  # Если нет значения, указываем 9150
    print(f"{dn:<50} {descr:<20} {speed:<7} {mtu:<6}")
