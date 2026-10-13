"""Fetch the NAB subset used by this project into data/."""

from pathlib import Path
import sys

import requests

REPO_RAW = "https://raw.githubusercontent.com/numenta/NAB/master"

SERIES = [
    ("data/realKnownCause/machine_temperature_system_failure.csv",
     "machine_temperature_system_failure.csv"),
    ("data/realKnownCause/ec2_request_latency_system_failure.csv",
     "ec2_request_latency_system_failure.csv"),
    ("data/realKnownCause/nyc_taxi.csv",
     "nyc_taxi.csv"),
    ("data/realAWSCloudwatch/ec2_cpu_utilization_5f5533.csv",
     "ec2_cpu_utilization_5f5533.csv"),
]

LABELS_PATH = "labels/combined_windows.json"
DATA_DIR = Path("data")


def download(url, dest):
    if dest.exists():
        print(f"  already present: {dest.name}")
        return

    print(f"  downloading: {dest.name}")
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    dest.write_bytes(response.content)


def main():
    DATA_DIR.mkdir(exist_ok=True)

    print("Downloading NAB series:")
    for remote_path, local_name in SERIES:
        url = f"{REPO_RAW}/{remote_path}"
        dest = DATA_DIR / local_name
        try:
            download(url, dest)
        except requests.HTTPError as e:
            print(f"  FAILED {local_name}: {e}", file=sys.stderr)
            return 1

    print("Downloading labels:")
    try:
        download(f"{REPO_RAW}/{LABELS_PATH}", DATA_DIR / "combined_windows.json")
    except requests.HTTPError as e:
        print(f"  FAILED labels: {e}", file=sys.stderr)
        return 1

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
