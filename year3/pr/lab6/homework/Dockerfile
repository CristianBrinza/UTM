# ------------------------------------------------------------------------------
# Base Image
# ------------------------------------------------------------------------------
# The 'FROM' directive initializes a new build stage and sets the base image for subsequent instructions.
# Here, we use the official 'python:3.9-slim' image, a lightweight version of Python 3.9.
FROM python:3.9-slim

# ------------------------------------------------------------------------------
# Setting the Working Directory
# ------------------------------------------------------------------------------
# The 'WORKDIR' directive sets the working directory for any 'RUN', 'CMD', 'ENTRYPOINT', 'COPY' and 'ADD' 
# instructions that follow it. It can be used multiple times in a Dockerfile. If the directory does not 
# exist, it will be created.
WORKDIR /app

# ------------------------------------------------------------------------------
# Copying Application Files
# ------------------------------------------------------------------------------
# The 'COPY' directive copies new files or directories from the source (the first parameter) and adds them 
# to the filesystem of the container at the path specified in the destination (the second parameter).
# Here, we're copying everything from the current directory (where the Dockerfile is located) to our 
# working directory in the container (/app).
COPY . /app

# ------------------------------------------------------------------------------
# Installing Dependencies
# ------------------------------------------------------------------------------
# The 'RUN' directive will execute any commands in a new layer on top of the current image and commit the 
# results. The resulting committed image will be used for the next step in the Dockerfile.
# Here, we're using pip, the Python package installer, to install our application's dependencies. 
# The '--no-cache-dir' option is used to keep the image size small by preventing pip from caching packages.
RUN pip install --no-cache-dir flask psycopg2-binary flask_swagger_ui

# ------------------------------------------------------------------------------
# Setting Environment Variables
# ------------------------------------------------------------------------------
# Environment variables can be set using the 'ENV' directive and are in the form of key-value pairs. 
# They can be accessed by scripts and applications running in the container.
# Here, we're specifying that our application should listen on port 5000.
ENV LISTEN_PORT=5000

# ------------------------------------------------------------------------------
# Exposing Ports
# ------------------------------------------------------------------------------
# The 'EXPOSE' directive informs Docker that the container listens on the specified network ports at runtime.
# Here, we're exposing port 5000, so when the container runs, the application can be accessed on this port.
EXPOSE 5000

# ------------------------------------------------------------------------------
# Default Command
# ------------------------------------------------------------------------------
# The 'CMD' directive provides defaults for an executing container. It can include an executable, or they 
# can omit the executable, in which case you must specify an 'ENTRYPOINT' directive as well.
# Here, we're specifying that when the container starts, it should execute 'app.py' using Python.
CMD ["python", "app.py"]
