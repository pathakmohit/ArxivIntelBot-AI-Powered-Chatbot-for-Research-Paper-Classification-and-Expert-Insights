# Backend.py

import json
import os
import pickle
from concurrent.futures import ThreadPoolExecutor
import gdown
def download_dataset():
    url = "https://drive.google.com/file/d/17_TAzEQimPfmsDoExFoRd--3XGf666IH/view?usp=drive_link"  # Replace with your link
    output = "/tmp/arxiv-metadata-oai-snapshot.json"
    gdown.download(url, output, quiet=False)
    return output
DATASET_PATH = download_dataset()

# Load and Search Dataset with Multithreading
def search_papers(query, file_path=DATASET_PATH, max_results=5):
    results = []
    query_lower = query.lower()

    def match_paper(line):
        try:
            data = json.loads(line)
            title = data.get("title", "").lower()
            abstract = data.get("abstract", "").lower()
            if query_lower in title or query_lower in abstract:
                return {
                    "title": data.get("title"),
                    "abstract": data.get("abstract"),
                    "authors": data.get("authors"),
                    "categories": data.get("categories"),
                    "doi": data.get("doi"),
                    "update_date": data.get("update_date"),
                }
        except json.JSONDecodeError:
            return None

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            with ThreadPoolExecutor() as executor:
                for paper in executor.map(match_paper, file):
                    if paper and len(results) < max_results:
                        results.append(paper)
    except FileNotFoundError:
        print("❌ Dataset file not found!")

    return results

# Helper: Summarize Retrieved Papers
def generate_context_summary(papers):
    if not papers:
        return "No relevant papers found."
    
    summary = ""
    for i, paper in enumerate(papers, start=1):
        summary += f"Paper {i}: {paper['title']}\nSummary: {paper['abstract'][:300]}...\n\n"
    return summary

if __name__ == "__main__":
    # Quick test
    query = "machine learning"
    found_papers = search_papers(query)
    print(generate_context_summary(found_papers))
