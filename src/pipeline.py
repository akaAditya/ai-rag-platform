import os
import csv
import json
from src.ingestors.csv_ingestor import CSVIngestor
from src.ingestors.json_ingestor import JSONIngestor

# HANDS-ON VALIDATION ENVIRONMENT

if __name__ == "__main__":
    print("--- 🚀 Initializing RAG Platform Ingestion Test 🚀 ---\n")

    csv_file = "test_knowledge_base.csv"
    json_file = "test_metadata.json"

    # --- A. Generating Dummy Data Files ---
    print("[SETUP] Generating temporary dummy files for testing...")

    # Creating Dummy CSV (Simulating knowledge base text chunks)
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["doc_id", "content", "source_url"])
        writer.writerow(["101", "Vector embeddings represent text in semantic space.", "https://docs.ai/vectors"])
        writer.writerow(["102", "Generative AI requires strict prompt context constraints.", "https://docs.ai/prompting"])

    # Creating dummt JSON (Simulating configuration or metadata)
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump([
            {"config_id": "cfg_01", "model": "gpt-4o", "temperature": 0.2},
            {"config_id": "cfg_02", "model": "claude-3.5-sonnet", "temperature": 0.0}
        ], f)
    
    print("[SETUP SUCCESS] Dummy files created successfully. \n" + "="*50 + "\n")

    # ---B. Running Ingestion Engine Framework ---
    try: 
        # 1. Testing CSV Ingestor
        print("[STAGE 1] Triggering CSV Ingestion Pipeline...")
        csv_pipeline = CSVIngestor(file_path=csv_file)
        csv_docs = csv_pipeline.extract_data()
        print(f"[OUTPUT] Parsed Data: {csv_docs}\n")

        print("-" *50)

        # 2. Testing JSON Ingestor
        print("[STAGE 2] Triggering JSON Ingestion Pipeline...")
        json_pipeline = JSONIngestor(file_path=json_file)
        json_docs = json_pipeline.extract_data()
        print(f"[OUTPUT] Parsed Data: {json_docs}\n")

        print("-" *50)

        # 3. Testing Error Handling (Robustness Check)
        print("[STAGE 3] Triggering Error Handling Check (Fake Path)...")
        fake_pipeline = CSVIngestor(file_path="non_existent_file.csv")
        fake_pipeline.extract_data()


    except Exception as e:
        print(f"\n[EXCEPTION CAUGHT AS EXPECTED] Error handled smoothly:\n{e}")

    finally:
        #---- C. Cleanup ----
        print("\n" + "="*50 + "\n[CLEANUP] Removing temporary test files")
        if os.path.exists(csv_file): os.remove(csv_file)
        if os.path.exists(json_file): os.remove(json_file)
        print("[CLEANUP SUCCESS] Workspace is clean. Test Complete.")