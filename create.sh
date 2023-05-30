#!/bin/bash

# Directories
mkdir -p ./src/scripts
mkdir -p ./src/templates
mkdir -p ./src/utils
mkdir -p ./data
mkdir -p ./docs
mkdir -p ./tests

# Python scripts
touch ./src/scripts/create_application.py
touch ./src/scripts/send_application.py
touch ./src/utils/json_handler.py
touch ./src/utils/smtp_handler.py
touch ./setup.py

# Test scripts
touch ./tests/test_create_application.py
touch ./tests/test_send_application.py

# LaTeX templates
touch ./src/templates/cv_template.tex
touch ./src/templates/cover_letter_template.tex

# JSON data
echo '{
    "companies": [
        {
            "name": "Company 1",
            "contacts": [
                {
                    "name": "Contact 1",
                    "email": "contact1@example.com",
                    "positions": [
                        {
                            "position_name": "Position 1",
                            "url": "http://example.com/position1",
                            "application_status": "sent"
                        },
                        {
                            "position_name": "Position 2",
                            "url": "http://example.com/position2",
                            "application_status": "not sent"
                        }
                    ]
                },
                {
                    "name": "Contact 2",
                    "email": "contact2@example.com",
                    "positions": [
                        {
                            "position_name": "Position 3",
                            "url": "http://example.com/position3",
                            "application_status": "not sent"
                        }
                    ]
                }
            ]
        },
        {
            "name": "Company 2",
            ...
        }
    ]
}' > ./data/companies.json

# Gitignore
touch ./.gitignore

# Requirements
touch ./requirements.txt

# Docs
echo '# Application Management System

This software aims to manage and streamline the application process. It takes in information about companies, contacts, and positions, saves this data in a JSON file, then uses this data to generate application documents (CV, cover letter, attachments) using [Stefanqn/Bewerbung](https://github.com/Stefanqn/Bewerbung) LaTeX templates. Once the documents have been confirmed as correct, the software sends the application via email using a previously specified sender address with SMTP-forwarder. The software then marks the application status in the JSON file as sent.

## Author

This software was developed by Kevin Veen-Birkenbach. You can contact him at kevin@veen.world

## License

This project is licensed under the AGPL v3 License.

## Acknowledgements

This project is based on a conversation available at https://chat.openai.com/share/50de73c8-bfec-4cdd-be58-fe3fd9036d1c.' > ./docs/README.md
