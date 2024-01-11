FROM python:3.10

# working directory set to /app
WORKDIR /app

# Copy the current directory into the container at /app
COPY . /app

# Install packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x /usr/local/bin/streamlit /app/app.py

# Make port 8050 available to the world outside this container
EXPOSE 8050

# Run app.py when the container launches
CMD ["/usr/local/bin/streamlit", "run", "app.py"]