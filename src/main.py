from ingestion.ingest import excel_to_yaml
from generators.mermaid import generate_mermaid
from generators.ppt import generate_ppt
from agents.validation import validate

def run_pipeline(file):
    data = excel_to_yaml(file)
    validate(data)
    mermaid = generate_mermaid(data)
    return generate_ppt(mermaid)