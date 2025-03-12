# Application Management System
[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-blue?logo=github)](https://github.com/sponsors/kevinveenbirkenbach) [![Patreon](https://img.shields.io/badge/Support-Patreon-orange?logo=patreon)](https://www.patreon.com/c/kevinveenbirkenbach) [![Buy Me a Coffee](https://img.shields.io/badge/Buy%20me%20a%20Coffee-Funding-yellow?logo=buymeacoffee)](https://buymeacoffee.com/kevinveenbirkenbach) [![PayPal](https://img.shields.io/badge/Donate-PayPal-blue?logo=paypal)](https://s.veen.world/paypaldonate)


This software aims to manage and streamline the application process. It takes in information about companies, contacts, and positions, saves this data in a JSON file, then uses this data to generate application documents (CV, cover letter, attachments) using [Stefanqn/Bewerbung](https://github.com/Stefanqn/Bewerbung) LaTeX templates. Once the documents have been confirmed as correct, the software sends the application via email using a previously specified sender address with SMTP-forwarder. The software then marks the application status in the JSON file as sent.

## Author

This software was developed by Kevin Veen-Birkenbach. You can contact him at kevin@veen.world

## License

This project is licensed under the AGPL v3 License.

## Chat-GPT

This project is based on a conversation available at https://chat.openai.com/share/50de73c8-bfec-4cdd-be58-fe3fd9036d1c.

### Scan files for Chat-GPT
To scan the files execute:

```bash 
find . -type f -not -path './.git/*' -not -name '*.md' -not -name '*.txt' -exec sh -c 'echo "--- {} ---"; cat {}' \;
```

## Todo
- check sent status attribut in create_application.py

