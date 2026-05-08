# Use a lean, official Python base image
FROM python:3.9-slim

# 1. INSTALL SYSTEM DEPENDENCIES.
# Install packages needed for downloading, installing, and running Google Chrome
# and its driver. We also install `jq` to easily parse the official Chrome JSON feed.
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    jq \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# 2. INSTALL GOOGLE CHROME BROWSER
# Add Google's official signing key and repository to ensure we get a stable release.
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-chrome-keyring.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable

# 3. INSTALL THE MATCHING CHROMEDRIVER
# This command uses the official Google Chrome JSON endpoint to find the URL for the
# latest stable chromedriver that matches the browser we just installed.
# This is the most reliable method for ensuring version compatibility.
RUN CHROME_DRIVER_URL=$(wget -qO- https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json | jq -r '.channels.Stable.downloads.chromedriver[] | select(.platform=="linux64") | .url') \
    && wget -q -O chromedriver-linux64.zip ${CHROME_DRIVER_URL} \
    && unzip chromedriver-linux64.zip \
    && mv chromedriver-linux64/chromedriver /usr/local/bin/ \
    && rm chromedriver-linux64.zip \
    && rm -rf chromedriver-linux64

# 4. SET UP PYTHON ENVIRONMENT
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .


RUN touch tests/__init__.py

# 5. DEFINE THE COMMAND TO RUN TESTS
# This command will be executed when your Docker container starts.
CMD ["pytest", "tests/"]