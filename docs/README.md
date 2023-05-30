# Application Management System

This software aims to manage and streamline the application process. It takes in information about companies, contacts, and positions, saves this data in a JSON file, then uses this data to generate application documents (CV, cover letter, attachments) using [Stefanqn/Bewerbung](https://github.com/Stefanqn/Bewerbung) LaTeX templates. Once the documents have been confirmed as correct, the software sends the application via email using a previously specified sender address with SMTP-forwarder. The software then marks the application status in the JSON file as sent.

## Author

This software was developed by Kevin Veen-Birkenbach. You can contact him at kevin@veen.world

## License

This project is licensed under the AGPL v3 License.

## Acknowledgements

This project is based on a conversation available at https://chat.openai.com/share/50de73c8-bfec-4cdd-be58-fe3fd9036d1c.
