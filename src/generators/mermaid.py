def generate_mermaid(data):
    lines = ["flowchart TB"]

    for env in data["environments"]:
        lines.append(f'subgraph {env["name"]}')

        for c in env["components"]:
            node = f'{env["name"]}_{c["name"]}'.replace("-", "_")
            lines.append(f'{node}[{c["name"]}]')

        for c in env["components"]:
            src = f'{env["name"]}_{c["name"]}'.replace("-", "_")
            for t in c.get("connects_to", []):
                tgt = f'{env["name"]}_{t}'.replace("-", "_")
                lines.append(f'{src} --> {tgt}')

        lines.append("end")

    return "\n".join(lines)