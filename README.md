# Docker

Educational Docker project with Python services for loss metric calculation.

## Repository Contents

- `Dockerfile` - base image and dependency installation.
- `docker-compose.yml` - multi-service run configuration.
- `requirements.txt` - Python dependencies.
- `src/losses.py` - implementations of loss functions.
- `src/mse_service.py` - service script for Mean Squared Error.
- `src/mae_service.py` - service script for Mean Absolute Error.
- `src/hinge_service.py` - service script for Squared Hinge Loss.
- `src/main.py` - local script for combined metric calculation.

## Implemented Functionality

The code calculates three metrics on predefined input arrays:

- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)
- Squared Hinge Loss

The project runs these calculations in separate containerized services via Docker Compose.
