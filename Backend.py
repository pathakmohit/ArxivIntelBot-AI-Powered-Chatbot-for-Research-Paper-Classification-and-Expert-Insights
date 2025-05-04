import json
import os
import logging
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Dataset Path
DATASET_PATH = "D:/project101/task7/arxiv-metadata-oai-snapshot.json"

def search_papers(query: str, file_path: str = DATASET_PATH, max_results: int = 5) -> List[Dict]:
    """
    Search for papers matching the query in the dataset using multithreading.
    
    Args:
        query: Search query string
        file_path: Path to the dataset JSON file
        max_results: Maximum number of results to return
    
    Returns:
        List of matching paper dictionaries
    
    Raises:
        FileNotFoundError: If dataset file is not found
        ValueError: If query is invalid
    """
    if not query or not isinstance(query, str):
        raise ValueError("Query must be a non-empty string")
    
    results = []
    query_lower = query.lower().strip()
    
    if not os.path.exists(file_path):
        logger.error(f"Dataset file not found: {file_path}")
        raise FileNotFoundError(f"Dataset file not found: {file_path}")

    def match_paper(line: str) -> Optional[Dict]:
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
        except json.JSONDecodeError as e:
            logger.warning(f"Invalid JSON line: {e}")
        return None

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            with ThreadPoolExecutor() as executor:
                for paper in executor.map(match_paper, file):
                    if paper and len(results) < max_results:
                        results.append(paper)
        logger.info(f"Found {len(results)} papers for query: {query}")
    except Exception as e:
        logger.error(f"Error searching papers: {e}")
        raise
    
    return results

def generate_context_summary(papers: List[Dict]) -> str:
    """
    Generate a summary of retrieved papers.
    
    Args:
        papers: List of paper dictionaries
    
    Returns:
        Formatted summary string
    """
    if not papers:
        logger.info("No papers found for summary")
        return "No relevant papers found."
    
    summary = ""
    for i, paper in enumerate(papers, start=1):
        abstract = paper.get("abstract", "")[:300]
        title = paper.get("title", "Untitled")
        summary += f"Paper {i}: {title}\nSummary: {abstract}...\n\n"
    
    logger.info(f"Generated summary for {len(papers)} papers")
    return summary

def validate_query(query: str) -> str:
    """
    Validate the search query.
    
    Args:
        query: Input query string
    
    Returns:
        Validated lowercase query
    
    Raises:
        ValueError: If query is invalid
    """
    if not isinstance(query, str):
        raise ValueError("Query must be a string")
    query = query.strip()
    if not query:
        raise ValueError("Query cannot be empty")
    return query.lower() 

if __name__ == "__main__":
    try:
        query = input("Enter your query: ")
        query = validate_query(query)
        found_papers = search_papers(query)
        print(generate_context_summary(found_papers))
    except (ValueError, FileNotFoundError) as e:
        logger.error(f"Error: {e}")
        print(f"Error: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")
