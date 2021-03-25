# Set the virtualenv for main.py
MY_ENV=.env
if [ ! -d "$MY_ENV" ]; then
    # Create the virtualenv if it does not exists
    python3 -m venv .env
    source .env/bin/activate
    # Load the dependencies from the requirements.txt
    pip install -r requirements.txt
else 
    # Activate the virtualenv if it exists
    source .env/bin/activate
fi

# Run the main.py Python file
python3 main.py
