import csv
import json
import os
from datetime import datetime
from uuid import uuid1

from flask import Flask, flash, jsonify, redirect, render_template, request

from .utils.pipedriver import create_lead, create_note, create_person
from .utils.settings import get_token, set_token


'''
TODO: 
- Add acquisition source to lead after creation
- Update /tmp folder to use OS tmp folder
'''


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.update(
        DEBUG= True,
        SECRET_KEY= 'secret',
        TEMPLATE_FOLDER= 'templates',
        STATIC_FOLDER= 'static'
    )
    
    
    @app.route('/')
    def index():
        return render_template('index.html', settings=get_token())
    
    
    @app.route('/parse', methods=['POST'])
    def parse():
        # Check if API token is set
        if not get_token():
            flash('API token is required to continue.', 'error')
            return redirect('/')
        # check if file is in request
        if 'file' not in request.files:
            flash('Lead source file is required.', 'error')
            return redirect('/')
        if request.files['file'].filename == '':
            flash('Lead source file is required.', 'error')
            return redirect('/')
        # check if template is default
        template = request.form.get('template')
        if template == 'default':
            flash('Please select a valid template', 'error')
            return redirect('/')
    
        # save csv file to tmp folder
        file = request.files['file']
        filename = f'/tmp/{uuid1()}.csv'
        file.save(filename)
        
        data = []
        start = request.form.get('start')
        
        # read csv file
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            lines = list(reader)
           
            # Parse template 1 - Mahindra USA
            if template == '1':
                for line in lines[1:]:
                    create_date = datetime.strptime(line[23], '%m/%d/%Y %I:%M:%S %p')
                    # Filter by date if start is provided
                    note_content = ''
                    for f in lines[0]:
                        if line[lines[0].index(f)] == '':
                            continue
                        note_content += f'\n{f}: {line[lines[0].index(f)]}'
                    
                    if start and create_date >= datetime.strptime(start, '%Y-%m-%d'):
                        data.append({
                            "person": {
                                "name": line[4] + " " + line[5],
                                "email": [line[6]],
                                "phone": [line[7]],
                                "visible_to": 3
                            },
                            "lead": {
                                "title":  line[4] + " " + line[5]+ " Lead",
                                "person_id": "",
                                # set acquisition source
                                "9c9489db4f5479edc23289ec41853a19f4a4780c": 22,
                            },
                            "note": {
                                "content": note_content,
                                "lead_id": "",
                                "pinned_to_lead_flag": 1
                            },
                        })
                    elif not start:
                        data.append({
                            "person": {
                                "name": line[4] + " " + line[5],
                                "email": [line[6]],
                                "phone": [line[7]],
                                "visible_to": 3
                            },
                            "lead": {
                                "title":  line[4] + " " + line[5]+ " Lead",
                                "person_id": "",
                                # set acquisition source
                                "9c9489db4f5479edc23289ec41853a19f4a4780c": 22,
                            },
                            "note": {
                                "content": note_content,
                                "lead_id": "",
                                "pinned_to_lead_flag": 1
                            },
                        })
                        
                # Remove tmp file
                os.remove(filename)
                
                # Render template
                return render_template('index.html', data=data)
                    
                                
            else:
                flash('Please select a valid template', 'error')
                return redirect('/')
                  
                    
    @app.route('/create', methods=['POST'])
    def create():
        form = request.form
        
        approvals = []
        
        # Find approved indexes
        for raw in form.items():
            if 'approve' in raw[0]:
                if raw[1] == 'on':
                    print('Approving index ' + raw[0].split('-')[1])
                    approvals.append(raw[0].split('-')[1])
        
        
        if not approvals or len(approvals) == 0:
            flash('No items were approved. Please try again.', 'error')
            return redirect('/')
             
        # Create Pipedrive objects for approved indexes
        for index in approvals:
            raw = form['data-'+index]
            print(raw.replace("'", '"'))
            data = json.loads(raw.replace("'", '"'))
            # Create person
            person = create_person(data['person'])
            
            # Create lead
            data['lead']['person_id'] = person['id']
            lead = create_lead(data['lead'])
            print(lead)
            
            # Create note
            data['note']['lead_id'] = lead['id']
            note = create_note(data['note'])
        
        flash(f'{len(approvals)} items created in Pipedrove.', 'success')
        return redirect('/')
    
      
    @app.route('/settings', methods=['POST'])
    def settings():
        form = request.form
        set_token(form['api_token'])
        flash('API token saved', 'success')
        return redirect('/')
        
        
    return app
        
        
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
