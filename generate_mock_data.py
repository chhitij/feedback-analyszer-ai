import pandas as pd
import os
from datetime import datetime, timedelta
import random

# Ensure data directory exists
os.makedirs('data/raw', exist_ok=True)

def generate_data():
    # 1. App Store Reviews
    reviews_data = [
        {
            "review_id": "REV_001",
            "platform": "App Store",
            "rating": 1,
            "review_text": "App crashes every time I try to upload a photo. It's completely unusable since the last update.",
            "user_name": "angry_user_99",
            "date": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"),
            "app_version": "2.1.3"
        },
        {
            "review_id": "REV_002",
            "platform": "Google Play",
            "rating": 5,
            "review_text": "Love the new dark mode! It's exactly what I was waiting for. Great job team.",
            "user_name": "happy_camper",
            "date": (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d"),
            "app_version": "2.1.3"
        },
        {
            "review_id": "REV_003",
            "platform": "App Store",
            "rating": 3,
            "review_text": "It's okay, but I wish there was a way to export my data to PDF. Please add this!",
            "user_name": "feature_seeker",
            "date": (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d"),
            "app_version": "2.1.2"
        },
        {
            "review_id": "REV_004",
            "platform": "Google Play",
            "rating": 1,
            "review_text": "Buy cheap rolex watches at http://fake-site.com",
            "user_name": "spammer_123",
            "date": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"),
            "app_version": "2.1.3"
        },
        {
            "review_id": "REV_005",
            "platform": "App Store",
            "rating": 2,
            "review_text": "Too expensive for what it does. I can find free alternatives.",
            "user_name": "budget_conscious",
            "date": (datetime.now() - timedelta(days=4)).strftime("%Y-%m-%d"),
            "app_version": "2.1.3"
        },
         {
            "review_id": "REV_006",
            "platform": "Google Play",
            "rating": 1,
            "review_text": "Data sync is broken. I lost all my notes from yesterday!",
            "user_name": "lost_data_user",
            "date": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"),
            "app_version": "2.1.3"
        }
    ]
    
    df_reviews = pd.DataFrame(reviews_data)
    df_reviews.to_csv('data/raw/app_store_reviews.csv', index=False)
    print("Generated data/raw/app_store_reviews.csv")

    # 2. Support Emails
    emails_data = [
        {
            "email_id": "EMAIL_001",
            "subject": "Login Issue - Critical",
            "body": "Hi Support, I cannot login to my account. I keep getting 'Error 503'. I am using an iPhone 13 Pro, iOS 16. Please help ASAP as I need to access my work.",
            "sender_email": "urgent@business.com",
            "timestamp": (datetime.now() - timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S"),
            "priority": "High"
        },
        {
            "email_id": "EMAIL_002",
            "subject": "Suggestion for Improvement",
            "body": "Hello, I really enjoy the app. It would be great if you could add a calendar view for the tasks. Currently the list view is a bit cluttered.",
            "sender_email": "fan@gmail.com",
            "timestamp": (datetime.now() - timedelta(hours=5)).strftime("%Y-%m-%d %H:%M:%S"),
            "priority": ""
        },
        {
            "email_id": "EMAIL_003",
            "subject": "Refund Request",
            "body": "I want a refund. The app is too slow on my Android device.",
            "sender_email": "unhappy@yahoo.com",
            "timestamp": (datetime.now() - timedelta(hours=24)).strftime("%Y-%m-%d %H:%M:%S"),
            "priority": "Low"
        },
         {
            "email_id": "EMAIL_004",
            "subject": "Bug Report: Font size",
            "body": "The font size on the settings page is too small on my iPad Mini. It's hard to read.",
            "sender_email": "grandma@icloud.com",
            "timestamp": (datetime.now() - timedelta(hours=48)).strftime("%Y-%m-%d %H:%M:%S"),
            "priority": "Medium"
        }
    ]
    
    df_emails = pd.DataFrame(emails_data)
    df_emails.to_csv('data/raw/support_emails.csv', index=False)
    print("Generated data/raw/support_emails.csv")

    # 3. Expected Classifications (Ground Truth)
    expected_data = [
        {"source_id": "REV_001", "source_type": "Review", "category": "Bug", "priority": "High", "technical_details": "Crash on photo upload, Version 2.1.3", "suggested_title": "Fix crash during photo upload"},
        {"source_id": "REV_002", "source_type": "Review", "category": "Praise", "priority": "Low", "technical_details": "None", "suggested_title": "Positive Feedback: Dark Mode"},
        {"source_id": "REV_003", "source_type": "Review", "category": "Feature Request", "priority": "Medium", "technical_details": "PDF Export requested", "suggested_title": "Feature: PDF Export"},
        {"source_id": "REV_004", "source_type": "Review", "category": "Spam", "priority": "Low", "technical_details": "None", "suggested_title": "Spam Review"},
        {"source_id": "REV_005", "source_type": "Review", "category": "Complaint", "priority": "Low", "technical_details": "Pricing complaint", "suggested_title": "Pricing Feedback"},
        {"source_id": "REV_006", "source_type": "Review", "category": "Bug", "priority": "Critical", "technical_details": "Data sync failure, data loss", "suggested_title": "Critical: Data Sync Data Loss"},
        {"source_id": "EMAIL_001", "source_type": "Email", "category": "Bug", "priority": "Critical", "technical_details": "Error 503, iPhone 13 Pro, iOS 16", "suggested_title": "Login Failure: Error 503"},
        {"source_id": "EMAIL_002", "source_type": "Email", "category": "Feature Request", "priority": "Medium", "technical_details": "Calendar View requested", "suggested_title": "Feature: Calendar View"},
        {"source_id": "EMAIL_003", "source_type": "Email", "category": "Complaint", "priority": "Low", "technical_details": "Performance issue on Android", "suggested_title": "Refund Request / Performance"},
        {"source_id": "EMAIL_004", "source_type": "Email", "category": "Bug", "priority": "Low", "technical_details": "iPad Mini, Settings page font size", "suggested_title": "UI Bug: Settings Font Size"}
    ]
    
    df_expected = pd.DataFrame(expected_data)
    df_expected.to_csv('data/raw/expected_classifications.csv', index=False)
    print("Generated data/raw/expected_classifications.csv")

if __name__ == "__main__":
    generate_data()
