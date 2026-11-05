#!/usr/bin/env python3

import json
from pathlib import Path
from pprint import pprint

from urllib.error import HTTPError, URLError
from urllib import request

# dataset location
DATASET_PATH = Path(__file__).parent / "datasets" / "incidents.json"


def load_dataset():
    with DATASET_PATH.open("r", encoding="utf-8") as f:
        incidents = json.load(f)

    return incidents


def analyze_incident(logs: str) -> str:
    url = "http://localhost:8000/analyze"
    
    # convertiomos el diccionario a JSON y luego a bytes
    data = json.dumps({"logs": logs}).encode("utf-8")

    # construimos la solicitud HTTP POST
    http_request = request.Request(
        url=url, 
        data=data, 
        headers={"Content-Type": "application/json"},
        method="POST")

    # enviamos la solicitud y esperamos la respuesta
    with request.urlopen(http_request, timeout=120) as response:
        result = json.load(response)

    return result["response"]



def save_results_to_file(results: list[dict]) -> None:

    results_path = Path(__file__).parent / "results" / "latest.json"

    with results_path.open("w", encoding="utf-8") as file:
        json.dump(results, file, ensure_ascii=False, indent=4)

    print(f"\n Results saved to: {results_path}")


def main():
    results = []
    incidents = load_dataset()
    print(f"Loaded {len(incidents)} incidents from the dataset.")
    
    for incident in incidents:
        print("Incident ID:", incident.get("id"))
        print("Category:", incident.get("category"))
        print("Logs:", incident.get("logs"))

        try:
            diagnosis = analyze_incident(incident.get("logs"))
            print("\nAI Diagnosis:")
            print("Diagnosis:", diagnosis)

            results.append({
                "incident_id": incident.get("id"),
                "category": incident.get("category"),
                "logs": incident.get("logs"),
                "diagnosis": diagnosis
            })
        except HTTPError as error:
            print(f"Error analyzing incident {incident.get('id')}: {error}")

        except URLError as error:
            print(f"Error analyzing incident {incident.get('id')}: {error}")

        except TimeoutError as error:
            print(f"Error analyzing incident {incident.get('id')}: Request timed out.")

    save_results_to_file(results)

if __name__ == "__main__":
    main()
