import os
from crewai import Crew, Process 
from src.agents.agents import FeedbackAgents
from src.tasks.tasks import FeedbackTasks
import pandas as pd
import json
from datetime import datetime

class FeedbackCrew:
    def __init__(self):
        self.agents = FeedbackAgents()
        self.tasks = FeedbackTasks()

    def run(self, review_file_path, email_file_path):
        # Instantiate Agents
        csv_reader = self.agents.csv_reader_agent()
        classifier = self.agents.feedback_classifier_agent()
        bug_analyst = self.agents.bug_analysis_agent()
        feature_extractor = self.agents.feature_extractor_agent()
        ticket_creator = self.agents.ticket_creator_agent()
        quality_critic = self.agents.quality_critic_agent()

        # Instantiate Tasks
        read_task = self.tasks.read_csv_task(csv_reader, [review_file_path, email_file_path])
        classify_task = self.tasks.classify_feedback_task(classifier, read_task)
        bug_task = self.tasks.analyze_bugs_task(bug_analyst, classify_task)
        feature_task = self.tasks.extract_features_task(feature_extractor, classify_task) # Parallel-ish
        ticket_task = self.tasks.create_tickets_task(ticket_creator, [bug_task, feature_task])
        review_task = self.tasks.review_tickets_task(quality_critic, ticket_task)

        # Create Crew
        crew = Crew(
            agents=[csv_reader, classifier, bug_analyst, feature_extractor, ticket_creator, quality_critic],
            tasks=[read_task, classify_task, bug_task, feature_task, ticket_task, review_task],
            verbose=True,
            process=Process.sequential
        )

        # Run Crew
        result = crew.kickoff()
        return result

def save_results_to_csv(result):
    try:
        # CrewAI returns a CrewOutput object, extract the raw output
        if hasattr(result, 'raw'):
            result_str = result.raw
        elif hasattr(result, 'output'):
            result_str = result.output
        else:
            result_str = str(result)
        
        # Clean markdown code blocks
        clean_str = result_str.replace('```json', '').replace('```', '').strip()
        
        # Try to parse as JSON
        try:
            data = json.loads(clean_str)
        except json.JSONDecodeError:
            # Fallback: find JSON array in text
            import re
            match = re.search(r'\[.*\]', clean_str, re.DOTALL)
            if match:
                data = json.loads(match.group(0))
            else:
                # If still can't parse, create simple structure from text
                data = [{
                    'ticket_id': 1,
                    'title': 'Analysis Complete',
                    'description': clean_str[:500],
                    'category': 'Mixed',
                    'priority': 'Medium'
                }]

        # Ensure data is a list
        if isinstance(data, dict):
            data = [data]
        
        df = pd.DataFrame(data)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = 'data/processed'
        os.makedirs(output_dir, exist_ok=True)
        
        output_path = os.path.join(output_dir, f'generated_tickets_{timestamp}.csv')
        df.to_csv(output_path, index=False)
        
        return output_path, df
        
    except Exception as e:
        print(f"Error saving results: {e}")
        # Save raw result for debugging
        output_dir = 'data/processed'
        os.makedirs(output_dir, exist_ok=True)
        
        error_path = os.path.join(output_dir, 'raw_output_error.txt')
        with open(error_path, 'w') as f:
            f.write(str(result))
        
        return None, None

if __name__ == "__main__":
    # Test run
    crew = FeedbackCrew()
    result = crew.run('data/raw/app_store_reviews.csv', 'data/raw/support_emails.csv')
    print("Crew finished.")
    save_results_to_csv(result)
