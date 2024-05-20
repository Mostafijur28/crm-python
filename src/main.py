from workflow_config import WorkflowConfiguration
from lead_simulator import LeadSimulator
from executor import WorkflowExecutor


def main():
    workflow_config = WorkflowConfiguration()
    lead_simulator = LeadSimulator()
    workflow_executor = WorkflowExecutor(workflow_config)

    # Simulate incoming leads
    for _ in range(3):
        lead = lead_simulator.generate_lead()
        workflow_executor.execute(lead)


if __name__ == "__main__":
    main()
