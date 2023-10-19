# Use the official PostgreSQL image as a base
#    This line sets the base image for the Docker container. In this case, it's using the  official PostgreSQL image, and the "latest" tag indicates that the most recent version of this image is to be used.
FROM postgres:latest

# Set environment variables for default username, password, and database

# These lines set environment variables within the Docker container. They're used to specify the default credentials and database name for the PostgreSQL instance.
ENV POSTGRES_USER=admin
# This sets an environment variable for the port on which PostgreSQL will listen.
ENV POSTGRES_PASSWORD=adminpass
# This command tells Docker that the container will listen on the specified network port at runtime. Here, port 5432 is exposed, which is the default port for PostgreSQL.
ENV POSTGRES_DB=scooters

# Expose the default PostgreSQL port
# This sets an environment variable for the port on which PostgreSQL will listen.
ENV LISTEN_PORT=5432
# This command tells Docker that the container will listen on the specified network port at r
EXPOSE 5432

# This command specifies what should be run when the container starts. In this case, it's the PostgreSQL server.
# Command to run when starting the container
CMD ["postgres"]

# Use an official Python runtime as a base image
# This sets a new base image for the Docker container, specifying a slim version of Python 3.9.
FROM python:3.9-slim

# Set the working directory in the container
# This command sets the working directory inside the container. Any subsequent commands will be run from this directory.
WORKDIR /app

# Copy the current directory contents into the container at /app
# This copies the current directory's content on the host into the /app directory of the container.
COPY . /app

#This installs the required Python packages using pip. The --no-cache-dir option ensures that the package installation does not cache, which helps to reduce the image size.
# Install the required packages
RUN pip install --no-cache-dir flask psycopg2-binary flask_swagger_ui

# Make port 5000 available to the world outside this container
ENV LISTEN_PORT=5000
# This sets an environment variable for the port on which the Flask application will listen.
# This command tells Docker that the container will listen on port 5000 at runtime, which is the default port for Flask applications.
EXPOSE 5000

# Run app.py when the container launches
#This command specifies that the container should run app.py using Python when it starts.
CMD ["python", "app.py"]
