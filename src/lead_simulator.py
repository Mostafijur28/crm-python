import random

class LeadSimulator:
    def __init__(self):
        self.lead_sources = ['Salesforce', 'HubSpot', 'DirectAPI', 'LinkedIn']

    def generate_lead(self):
        return {
            'lead_source': random.choice(self.lead_sources),
            'lead_data': 'Sample lead data'
        }
