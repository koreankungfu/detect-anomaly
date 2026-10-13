# detect-anomaly

Real-time anomaly detection on streaming numeric sensor data. The system
ingests a stream of readings, flags unusual patterns using a trained
model, and exposes predictions through an API and dashboard.

Built with Python, FastAPI, PyTorch, and Docker.

## Data

Uses the [Numenta Anomaly Benchmark](https://github.com/numenta/NAB) —
a labelled collection of real-world time series for evaluating anomaly
detection algorithms. Four series are used, spanning industrial, cloud,
and transport domains.

The raw data is not committed to this repository. To fetch it:

    pip install -r requirements.txt
    python scripts/download_data.py

Data is written to `data/`, which is gitignored. The script is
idempotent — re-running it is safe and skips files already present.

**Licence:** NAB is released under AGPL-3.0. The data is downloaded at
runtime and not redistributed with this project.

## Project structure

    src/
      ingestion/     read CSVs as a simulated stream
      features/      rolling windows, scaling, train/test split   (M3)
      models/        isolation forest, LSTM autoencoder           (M4, M6)
      evaluation/    metrics and threshold selection              (M5)
      api/           FastAPI service                              (M8)
      dashboard/     Streamlit UI                                 (M9)
      monitoring/    drift detection                              (M10)
    scripts/         download and utility scripts
    tests/           test suite
    models/          saved model artefacts and metadata
    reports/         evaluation outputs

## Status

Early development. Current milestone: M2 complete (ingestion).
Next: M3 (features — rolling windows, chronological split, scaling).
