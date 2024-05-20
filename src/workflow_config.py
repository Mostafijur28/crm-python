import json

class WorkflowConfiguration:
    def __init__(self, config_path='config/workflows.json'):
        with open(config_path, 'r') as file:
            self.workflows = json.load(file)['workflows']

    def get_workflow(self, lead_source):
        for workflow in self.workflows:
            if workflow['lead_source'] == lead_source:
                return workflow
        return None
