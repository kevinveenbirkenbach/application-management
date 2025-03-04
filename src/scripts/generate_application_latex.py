import json
from jinja2 import Environment, FileSystemLoader

def create_application():
    # Load the data from the JSON file
    with open('../data/companies.json') as f:
        data = json.load(f)
    
    # Set up the Jinja2 environment
    env = Environment(loader=FileSystemLoader('../src/templates'))

    # Loop through each company
    for company in data['companies']:
        # Loop through each contact
        for contact in company['contacts']:
            # Loop through each position
            for position in contact['positions']:
                # If the application has not been sent
                if position['application_status'] != 'sent':
                    # Load the templates
                    cover_letter_template = env.get_template('cover_letter_template.tex')
                    
                    # Populate the templates with the relevant data
                    cover_letter = cover_letter_template.render(company=company['name'], 
                                                                 contact=contact['name'], 
                                                                 position=position['position_name'])
                    # Write the populated templates to files
                    with open(f'../data/{company["name"]}_{position["position_name"]}_cover_letter.tex', 'w') as f:
                        f.write(cover_letter)

if __name__ == "__main__":
    create_application()