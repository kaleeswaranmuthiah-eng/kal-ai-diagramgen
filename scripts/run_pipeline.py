from src.main import run_pipeline

if __name__ == "__main__":
    output = run_pipeline("data/sample.csv")
    print("Generated:", output)