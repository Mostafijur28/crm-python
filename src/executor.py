from logger import Logger
from message_sender import MessageSender


class WorkflowExecutor:
    def __init__(self, workflow_config):
        self.workflow_config = workflow_config
        self.logger = Logger()
        self.message_sender = MessageSender(self.logger)

    def execute(self, lead):
        workflow = self.workflow_config.get_workflow(lead['lead_source'])
        if workflow:
            self.logger.log(f"Processing lead from {lead['lead_source']} using persona {workflow['persona']} over {workflow['output_channel']}")
            self.process_lead(lead, workflow['persona'], workflow['output_channel'])
        else:
            self.logger.log(f"No workflow found for lead source: {lead['lead_source']}")

    def process_lead(self, lead, persona, output_channel):
            self.message_sender.send_message(lead, persona, output_channel)

