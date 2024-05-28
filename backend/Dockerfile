# Stage 1: Build environment with pipenv
FROM python:3.11-slim-bookworm AS builder

# Set environment variables
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT=1

# Set the working directory
WORKDIR /app/

# Install pipenv and dependencies
RUN python -m pip install --upgrade pip \
    && pip install pipenv

# Copy Pipfile.lock and install dependencies
ADD ./backend/Pipfile.lock .
RUN pipenv sync

# checking that the packages are installed correctly
RUN /app/.venv/bin/python -c "import django; print(django.VERSION)"

# Stage 2: Final image with application code
FROM python:3.11-slim-bookworm AS runtime

# Set environment variables
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT=1

# Copy the installed packages from builder stage
COPY --from=builder /app/.venv/ /app/.venv/

# Set the working directory
WORKDIR /app/

# Copy only necessary files and directories
COPY ./backend/ .

# checking that the packages are installed correctly
# RUN /app/.venv/bin/python -c "import django; print(django.VERSION)"

# Exposing the port
EXPOSE 8000
