from crewai import Agent
from crewai_tools import FileReadTool, CSVSearchTool
from src.tools.csv_tools import csv_reader_tool  # Updated import

class FeedbackAgents:
    def __init__(self):
        # Use the function-based tool
        self.csv_reader_tool = csv_reader_tool
        # Built-in CrewAI tools
        self.file_reader = FileReadTool()
        self.csv_search = CSVSearchTool()

    def csv_reader_agent(self):
        return Agent(
            name='CSV Reader Agent',
            role='CSV Reader Specialist',
            goal='Read and extract data from feedback CSV files accurately',
            backstory='You are an expert data ingestion specialist. Your job is to read raw CSV files containing customer feedback and prepare them for analysis. You ensure no data is missed.',
            tools=[self.csv_reader_tool, self.file_reader, self.csv_search],
            verbose=True,
            allow_delegation=False
        )

    def feedback_classifier_agent(self):
        return Agent(
            name='Feedback Classifier Agent',
            role='Feedback Classification Expert',
            goal='Categorize feedback into Bug, Feature Request, Praise, Complaint, or Spam',
            backstory='You are a seasoned product manager with a keen eye for categorizing user feedback. You can distinguish between a critical bug and a user complaint. You analyze the sentiment and intent of every piece of feedback.',
            verbose=True,
            allow_delegation=False
        )

    def bug_analysis_agent(self):
        return Agent(
            name='Bug Analysis Agent',
            role='Technical Bug Analyst',
            goal='Extract technical details, reproduction steps, and assess severity of bugs',
            backstory='You are a QA Lead. When a bug is reported, you dig into the details to find device info, OS versions, and steps to reproduce. You assign a severity level (Critical, High, Medium, Low) based on the impact.',
            verbose=True,
            allow_delegation=False
        )

    def feature_extractor_agent(self):
        return Agent(
            name='Feature Extractor Agent',
            role='Product Feature Strategist',
            goal='Identify feature requests and estimate user impact/demand',
            backstory='You are a Product Strategist. You look for hidden feature requests in user feedback. You estimate how valuable a feature would be to the user base.',
            verbose=True,
            allow_delegation=False
        )

    def ticket_creator_agent(self):
        return Agent(
            name='Ticket Creator Agent',
            role='JIRA Ticket Creator',
            goal='Create structured, actionable tickets from analyzed feedback',
            backstory='You are a Project Manager who loves organized tickets. You take analyzed data and format it into clear, concise tickets with titles, descriptions, priorities, and labels.',
            verbose=True,
            allow_delegation=False
        )

    def quality_critic_agent(self):
        return Agent(
            name='Quality Critic Agent',
            role='Quality Assurance Critic',
            goal='Review generated tickets for completeness, accuracy, and consistency',
            backstory='You are the gatekeeper of quality. You review every ticket created to ensure it meets the team\'s high standards. You check if the priority makes sense and if the description is clear.',
            verbose=True,
            allow_delegation=False
        )