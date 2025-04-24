#!/usr/bin/env bash

# ensure the .streamlit folder exists
mkdir -p ~/.streamlit/

# credentials.toml — replace with your email
cat <<EOF > ~/.streamlit/credentials.toml
[general]
email = "xxl1323@case.edu"
EOF

# config.toml — tell Streamlit to bind to the Heroku $PORT
cat <<EOF > ~/.streamlit/config.toml
[server]
headless = true
enableCORS = false
port = \$PORT
EOF
