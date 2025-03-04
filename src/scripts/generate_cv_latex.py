import json
from jinja2 import Environment, FileSystemLoader

def load_data():
    with open('applications.json', 'r') as f:
        return json.load(f)

def generate_tex_files(applications):
    # Load environment
    env = Environment(loader=FileSystemLoader('/path/to/template/directory'))

    # Load template
    template = env.get_template('cv_template.tex.j2')

    for app in applications:
        for contact in app['contacts']:
            for position in contact['positions']:
                # Render template with data
                output = template.render(app)

                # Write the output to cv_template.tex
                with open(f'{position["position_name"]}_cv_template.tex', 'w') as f:
                    f.write(output)

def main():
    applications = load_data()
    generate_tex_files(applications)

if __name__ == '__main__':
    main()