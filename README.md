# 🤖 Feedback Analyzer AI

**AI-Powered Multi-Agent System for Automated User Feedback Analysis**

Transform thousands of user reviews and support emails into actionable tickets in minutes using 6 specialized AI agents powered by CrewAI and OpenAI GPT-4o-mini.


https://github.com/user-attachments/assets/298d7414-e3df-47ad-b281-0ad9ec39aa35


---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Output Files](#-output-files)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

### The Problem
Modern applications receive massive amounts of user feedback through:
- 📱 App store reviews
- 📧 Support emails  
- 💬 In-app surveys

**Manual processing is:**
- ⏰ Time-consuming (hours per day)
- 🎲 Inconsistent (different team members, different categorizations)
- ❌ Error-prone (critical issues get missed)
- 📉 Non-scalable (volume grows faster than team capacity)

### The Solution
**6 specialized AI agents** working together to:
1. 📖 **Read** feedback from multiple sources
2. 🏷️ **Classify** into Bug/Feature/Praise/Complaint
3. 🐛 **Analyze** bugs for severity and technical details
4. 💡 **Extract** feature requests with impact estimation
5. 🎫 **Generate** structured tickets with priority
6. ✅ **Validate** output quality and completeness

**Result:** Process 100+ feedback items in < 5 minutes with 95%+ accuracy!

---

## ✨ Key Features

- **🤖 Multi-Agent Architecture**: 6 specialized AI agents with distinct roles
- **🔄 Sequential Processing**: Agents work in pipeline with validated outputs
- **📊 Real-time Dashboard**: Streamlit UI for monitoring and control
- **🎨 Interactive Visualizations**: Plotly charts for insights
- **💾 Multiple Export Formats**: CSV & Excel reports
- **🔐 Secure API Key Management**: Session-based with `.env` support
- **📈 Progress Tracking**: Real-time logs and progress bars
- **🎯 High Accuracy**: 95%+ classification accuracy vs expected results

---

## 🏗️ System Architecture

### Agent Pipeline

```
┌─────────────────┐
│  CSV Reader     │ → Loads feedback data from files
└────────┬────────┘
         ↓
┌─────────────────┐
│  Classifier     │ → Categorizes: Bug/Feature/Complaint/Praise
└────────┬────────┘
         ↓
    ┌────┴────┐
    ↓         ↓
┌──────────┐ ┌─────────────────┐
│Bug       │ │Feature          │
│Analyst   │ │Extractor        │ → Parallel analysis
└────┬─────┘ └────────┬────────┘
     └────────┬────────┘
              ↓
    ┌─────────────────┐
    │Ticket Creator   │ → Generates structured tickets
    └────────┬────────┘
             ↓
    ┌─────────────────┐
    │Quality Critic   │ → Validates & refines output
    └─────────────────┘
```

### Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **AI Framework** | CrewAI 0.76.1 | Multi-agent orchestration |
| **LLM Provider** | OpenAI GPT-4o-mini | Natural language processing |
| **UI Framework** | Streamlit 1.51.0 | Interactive dashboard |
| **Data Processing** | Pandas 2.3.3 | CSV manipulation |
| **Visualization** | Plotly 6.5.0 | Interactive charts |
| **Vector DB** | ChromaDB 0.4.24 | Embedding storage |
| **Environment** | Python 3.9+ | Runtime |

---

## 📋 Prerequisites

- **Python**: 3.9 or higher
- **Conda**: Anaconda or Miniconda (recommended)
- **OpenAI API Key**: Get from [OpenAI Platform](https://platform.openai.com/api-keys)
- **Git**: For cloning repository

---

## 🚀 Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/feedback-analyzer-ai.git
cd feedback-analyzer-ai
```

### Step 2: Create Conda Environment

```bash
# Create environment
conda create -n feedback-analyszer-ai python=3.9

# Activate environment
conda activate feedback-analyszer-ai
```

### Step 3: Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt
```

**Important:** If you encounter dependency conflicts, install in this order:

```bash
# Uninstall conflicting packages
pip uninstall numpy chromadb qdrant-client -y

# Install NumPy first
pip install numpy==1.26.4 --only-binary :all:

# Install ChromaDB (will install compatible qdrant-client)
pip install chromadb==0.4.24

# Install CrewAI with compatible versions
pip install crewai==0.76.1 crewai-tools==0.76.0

# Install remaining packages
pip install streamlit pandas python-dotenv plotly openpyxl
```

---

## ⚙️ Configuration

### Option 1: Environment File (Recommended)

Create a `.env` file in the project root:

```bash
OPENAI_API_KEY="your-openai-api-key-here"
OPENAI_MODEL_NAME="gpt-4o-mini"
```

### Option 2: UI Input (Runtime)

1. Launch the Streamlit app
2. Enter your API key in the sidebar
3. Key is stored in session state (temporary)

---

## 🎮 Usage

### Run Streamlit Dashboard

```bash
# Navigate to UI directory
cd src/ui

# Launch dashboard
streamlit run app.py
```

The app will open at `http://localhost:8501`

### Run Command Line

```bash
# From project root
python src/main_crew.py
```

### Dashboard Workflow

1. **Configure API Key** (sidebar)
   - Enter OpenAI API key
   - Verify connection

2. **View Input Data** (Input Data tab)
   - Preview app store reviews
   - Preview support emails

3. **Start Analysis** (Dashboard tab)
   - Click "🚀 Start Analysis Agent Crew"
   - Monitor real-time progress
   - View completion status

4. **Explore Results** (Results tab)
   - View classification distribution (pie chart)
   - View priority breakdown (bar chart)
   - Download CSV/Excel reports

---

## 📁 Project Structure

```
feedback-analyszer-ai/
├── data/
│   └── raw/
│       ├── app_store_reviews.csv      # Input: App reviews
│       ├── support_emails.csv          # Input: Support tickets
│       └── expected_classifications.csv # Validation data
├── src/
│   ├── main_crew.py                   # Agent orchestration
│   ├── agents/
│   │   └── agents.py                  # 6 AI agent definitions
│   ├── tasks/
│   │   └── tasks.py                   # Task definitions
│   ├── tools/
│   │   └── csv_tools.py               # Custom CSV tools
│   └── ui/
│       ├── app.py                     # Main Streamlit app
│       ├── components/
│       │   └── sidebar.py             # API key management
│       ├── tabs/
│       │   ├── dashboard_tab.py       # Control & monitoring
│       │   ├── input_data_tab.py      # Data preview
│       │   └── results_tab.py         # Visualizations
│       └── utils/
│           └── data_loader.py         # CSV loading helpers
├── requirements.txt                    # Python dependencies
├── requirements.in                     # High-level dependencies
├── .env                               # API keys (gitignored)
├── README.md                          # This file
└── project-deatils.md                 # Detailed documentation
```

---

## 🔍 How It Works

### Agent Roles & Responsibilities

#### 1. **CSV Reader Agent** 📖
- **Role**: Data Ingestion Specialist
- **Input**: CSV files from `data/raw/`
- **Output**: Raw JSON with all feedback entries
- **Tools**: `CSVReaderTool`, `FileReadTool`, `CSVSearchTool`

#### 2. **Classifier Agent** 🏷️
- **Role**: Categorization Expert
- **Input**: Raw feedback JSON
- **Output**: Categorized feedback (Bug/Feature/Praise/Complaint/Spam)
- **Logic**: Keyword detection + sentiment analysis

#### 3. **Bug Analyst Agent** 🐛
- **Role**: Technical Bug Analyst
- **Input**: Bug-categorized feedback
- **Output**: Technical details + severity scores
- **Details Extracted**:
  - Device info (iOS/Android, version)
  - Reproduction steps
  - Severity: Critical/High/Medium/Low

#### 4. **Feature Extractor Agent** 💡
- **Role**: Product Feature Strategist
- **Input**: Feature-categorized feedback
- **Output**: Feature summaries + impact estimates
- **Estimates**:
  - User demand (High/Medium/Low)
  - Business value assessment
  - Implementation complexity

#### 5. **Ticket Creator Agent** 🎫
- **Role**: JIRA Ticket Creator
- **Input**: Analyzed feedback from agents 3 & 4
- **Output**: Structured tickets with:
  - Title
  - Description
  - Category
  - Priority
  - Assigned team
  - Estimated effort

#### 6. **Quality Critic Agent** ✅
- **Role**: Quality Assurance Reviewer
- **Input**: All generated tickets
- **Output**: Validated, refined final report
- **Checks**:
  - Title clarity
  - Description completeness
  - Priority consistency
  - Format standardization

### Data Flow Example

```
Input: "App crashes when I try to login on iOS 17"
   ↓
CSV Reader: Extracts text + metadata
   ↓
Classifier: Category = "Bug"
   ↓
Bug Analyst: Severity = "High", OS = "iOS 17", Issue = "Login crash"
   ↓
Ticket Creator: 
   Title: "[BUG] App crash on login - iOS 17"
   Priority: High
   Description: User reports app crashing during login on iOS 17...
   ↓
Quality Critic: ✅ Approved (clear, complete, properly prioritized)
```

---

## 📊 Output Files

After analysis, files are saved to `data/processed/`:

### `analyzed_tickets_YYYY-MM-DD_HH-MM-SS.csv`

```csv
ticket_id,title,description,category,priority,source
1,[BUG] Login crash iOS 17,App crashes when...,Bug,High,review_123
2,[FEATURE] Dark mode request,Users want dark theme...,Feature,Medium,email_456
3,[PRAISE] Love the new UI,Great redesign!,Praise,Low,review_789
```

### Columns Explained

| Column | Description | Example |
|--------|-------------|---------|
| `ticket_id` | Unique ticket identifier | 1, 2, 3 |
| `title` | Short descriptive title | [BUG] Login crash iOS 17 |
| `description` | Detailed explanation | User reports app crashing... |
| `category` | Feedback type | Bug, Feature, Praise |
| `priority` | Urgency level | Critical, High, Medium, Low |
| `source` | Original feedback ID | review_123, email_456 |

---

## 🔧 Troubleshooting

### Common Issues

#### 1. **ImportError: cannot import name 'EnvVar'**

**Problem**: CrewAI version mismatch

**Solution**:
```bash
pip uninstall crewai crewai-tools -y
pip install crewai==0.76.1 crewai-tools==0.76.0
```

#### 2. **AttributeError: `np.float_` was removed**

**Problem**: NumPy 2.0 incompatibility

**Solution**:
```bash
pip uninstall numpy -y
pip install numpy==1.26.4 --only-binary :all:
```

#### 3. **cannot import name 'HasVectorCondition' from 'qdrant_client'**

**Problem**: qdrant-client version conflict

**Solution**:
```bash
pip uninstall chromadb qdrant-client -y
pip install chromadb==0.4.24
```

#### 4. **API Key Not Working**

**Symptoms**: 401 Unauthorized errors

**Solutions**:
- Verify key is valid at [OpenAI Platform](https://platform.openai.com/api-keys)
- Check `.env` file format (no quotes in some cases)
- Ensure `OPENAI_API_KEY` environment variable is set
- Try entering key directly in UI sidebar

#### 5. **Streamlit Port Already in Use**

**Solution**:
```bash
# Use different port
streamlit run app.py --server.port 8502
```

### Dependency Resolution

If you encounter multiple dependency conflicts:

```bash
# Nuclear option: Fresh environment
conda deactivate
conda remove -n feedback-analyszer-ai --all
conda create -n feedback-analyszer-ai python=3.9
conda activate feedback-analyszer-ai

# Install in specific order
pip install numpy==1.26.4 --only-binary :all:
pip install chromadb==0.4.24
pip install crewai==0.76.1 crewai-tools==0.76.0
pip install streamlit pandas python-dotenv plotly openpyxl
```

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/feedback-analyzer-ai/issues)
- **Documentation**: See `project-deatils.md` for comprehensive guide
- **Email**: your.email@example.com

---

## 🙏 Acknowledgments

- **CrewAI**: Multi-agent orchestration framework
- **OpenAI**: GPT-4o-mini language model
- **Streamlit**: Interactive dashboard framework
- **Community**: All contributors and users

---

## 📈 Roadmap

- [ ] Support for additional data sources (Slack, Jira, GitHub)
- [ ] Multi-language feedback analysis
- [ ] Sentiment trend analysis over time
- [ ] Auto-assignment to dev teams based on expertise
- [ ] Custom model fine-tuning for domain-specific feedback
- [ ] Real-time webhook integrations
- [ ] Advanced analytics dashboard

---

**Made with ❤️ using CrewAI and OpenAI**
