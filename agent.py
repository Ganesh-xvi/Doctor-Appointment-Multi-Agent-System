from langgraph_supervisor import create_supervisor

class DoctorAppointmentAgent:
    def __init__(self, llm, booking_agent, availability_agent):
        self.llm = llm
        self.booking_agent = booking_agent
        self.availability_agent = availability_agent
        self.supervisor = None

    def create_supervisor(self):
        """Create and compile the supervisor agent."""
        self.supervisor = create_supervisor(
            model=self.llm,
            agents=[self.booking_agent, self.availability_agent],
            prompt=(
                "You are a supervisor that decides whether the user needs booking, "
                "rescheduling, cancelling, or just checking availability. "
                "Route the query to the right agent."
            ),
            add_handoff_back_messages=False,
            output_mode="full_history",
        ).compile()
        return self.supervisor