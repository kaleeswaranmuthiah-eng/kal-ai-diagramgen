def validate(data):
    for env in data["environments"]:
        for c in env["components"]:
            if c["type"] == "application" and not c.get("connects_to"):
                print(f"Warning: {c['name']} has no connections")