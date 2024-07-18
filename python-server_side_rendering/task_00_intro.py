#!/usr/bin/python3
"""This module defines a function generate_invitations that takes
two paramaters: template and attendees"""

import logging
import sys

def generate_invitations(template, attendees):
    """Generates invitation files based on a template
    for each attendee"""

    if not isinstance(template, str) or not isinstance(attendees, list):
        raise ValueError("Invalid input types. Expect template as str and\
                         attendees as list of dictionaries")
    
    template = template.strip()

    if not template:
        logging.warning("Template content is empty")
        return
    
    if not attendees:
        logging.warning("No attendees provided")
        return
    
    idx = 1

    for attendee in attendees:
        output_content = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(
                key, 'N/A') if attendee.get(key) is not None else 'N/A'
            placeholder = f'{{{key}}}'
            output_content - output_content.replace(placeholder, value)

        output_filename - f'output_{idx}.txt'

        base, extension = os.path.splitext(output_filename)
        counter = 1
        while os.path.exists(output_filename):
            output_filename = f"{base}_{counter}{extension}"
            counter += 1

        with open(output_filename, 'w') as output_file:
            output_file.write(output_content)
        print(f"Generated {output_filename}")

        idx += 1
        
    except ValueError as e:
        print(f"Error: {e}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
