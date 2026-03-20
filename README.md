# docker-practice

Educational Docker project with Python scripts for loss metric calculation.

## Project Scope

Containerized execution of metric calculation scripts using a shared Python environment.

## Repository Structure

- `Dockerfile`
- `docker-compose.yml`
- `requirements.txt`
- `src/losses.py`
- `src/mse_service.py`
- `src/mae_service.py`
- `src/hinge_service.py`
- `src/main.py`

## Implemented Functionality

- Mean Squared Error calculation
- Mean Absolute Error calculation
- Squared Hinge Loss calculation
- Separate service execution through Docker Compose