FROM python:3.12-slim-bookworm

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh
RUN apt-get update && apt-get install -y git

WORKDIR /
COPY agent.py /
COPY exec.py /
COPY phaseA.py /
COPY phaseB.py /
COPY resp.py /
COPY main.py /
# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"
EXPOSE 8000
CMD [ "uv", "run", "main.py" ]