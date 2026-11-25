import json

with open("nodes.json", "r", encoding="utf-8") as f:
    nodes = json.load(f)

# remove "color" key
for n in nodes:
    n.pop("color", None)

# save cleaned file
with open("nodes_no_color.json", "w", encoding="utf-8") as f:
    json.dump(nodes, f, indent=2, ensure_ascii=False)

print("Done. color removed.")
