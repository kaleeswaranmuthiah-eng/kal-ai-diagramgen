import pandas as pd

def excel_to_yaml(file):
    df = pd.read_csv(file)

    envs = {}

    for _, r in df.iterrows():
        env = r["environment"]
        comp = r["component"]

        if env not in envs:
            envs[env] = []

        connects = str(r.get("connects_to", "")).split(",") if pd.notna(r.get("connects_to")) else []

        envs[env].append({
            "name": comp,
            "type": r["type"],
            "connects_to": [c.strip() for c in connects if c.strip()]
        })

    return {"environments": [{"name": k, "components": v} for k,v in envs.items()]}