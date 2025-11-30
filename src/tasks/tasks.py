from crewai import Task

class FeedbackTasks:
    def read_csv_task(self, agent, file_paths):
        return Task(
            description=f'Read the feedback data from the following CSV files: {", ".join(file_paths)}. Extract all relevant columns including review text, subject, body, rating, and user info.',
            expected_output='A JSON object or list containing all the raw feedback entries from the provided files.',
            agent=agent
        )

    def classify_feedback_task(self, agent, context):
        return Task(
            description='Analyze the provided feedback data. For EACH entry, determine its category (Bug, Feature Request, Praise, Complaint, Spam). Look for keywords and sentiment.',
            expected_output='A list of feedback entries with an added "category" field.',
            agent=agent,
            context=[context] if not isinstance(context, list) else context
        )

    def analyze_bugs_task(self, agent, context):
        return Task(
            description='For entries categorized as "Bug", extract technical details (device, OS, version), identify steps to reproduce if available, and assign a severity level (Critical, High, Medium, Low). If not a bug, skip technical analysis.',
            expected_output='The feedback list with added "technical_details" and "severity" fields for bugs.',
            agent=agent,
            context=[context] if not isinstance(context, list) else context
        )

    def extract_features_task(self, agent, context):
        return Task(
            description='For entries categorized as "Feature Request", summarize the requested feature and estimate the potential impact (High, Medium, Low).',
            expected_output='The feedback list with added "feature_summary" and "impact" fields for feature requests.',
            agent=agent,
            context=[context] if not isinstance(context, list) else context
        )

    def create_tickets_task(self, agent, context):
        return Task(
            description='Transform the analyzed feedback into structured tickets. Each ticket should have: Title, Description, Type (Category), Priority, Labels, and Source Link/ID. Format this as a structured list.',
            expected_output='A list of structured ticket objects ready for export.',
            agent=agent,
            context=[context] if not isinstance(context, list) else context
        )

    def review_tickets_task(self, agent, context):
        return Task(
            description='Review the generated tickets. Ensure the priority matches the severity/impact. Check for clear titles. If a ticket looks like Spam, mark it as "Closed/Spam". Finalize the list.',
            expected_output='A final, polished list of tickets in CSV-ready format (list of dictionaries).',
            agent=agent,
            context=[context] if not isinstance(context, list) else context
        )
