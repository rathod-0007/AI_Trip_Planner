# Agentic TravX – AI-Powered Trip Planning Platform

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.30-orange)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/langchain-0.1-purple)](https://www.langchain.com/docs/)
[![LangChain Community](https://img.shields.io/badge/langchain--community-0.1-lightgrey)](https://github.com/hwchase17/langchain-community)
[![LangChain Experimental](https://img.shields.io/badge/langchain--experimental-0.1-lightgrey)](https://github.com/hwchase17/langchain-experimental)
[![LangGraph](https://img.shields.io/badge/langgraph-0.1-green)](https://github.com/yourusername/langgraph)
[![LangChain Groq](https://img.shields.io/badge/langchain--groq-0.1-red)](https://www.groq.com/)
[![LangChain OpenAI](https://img.shields.io/badge/langchain--openai-0.1-blue)](https://platform.openai.com/)
[![LangChain Tavily](https://img.shields.io/badge/langchain--tavily-0.1-lightblue)](https://github.com/yourusername/langchain_tavily)
[![LangChain Google Community](https://img.shields.io/badge/langchain--google--community-0.1-yellow)](https://github.com/yourusername/langchain-google-community)
[![LangChain Google Places API](https://img.shields.io/badge/langchain--google--places-0.1-orange)](https://developers.google.com/places)
[![FastAPI](https://img.shields.io/badge/fastapi-0.95-blue)](https://fastapi.tiangolo.com/)
[![Uvicorn](https://img.shields.io/badge/uvicorn-0.22-green)](https://www.uvicorn.org/)
[![Python Dotenv](https://img.shields.io/badge/python--dotenv-0.21-lightgrey)](https://pypi.org/project/python-dotenv/)
[![Pydantic](https://img.shields.io/badge/pydantic-2.3-blue)](https://docs.pydantic.dev/)
[![HTTPX](https://img.shields.io/badge/httpx-0.24-lightblue)](https://www.python-httpx.org/)
[![Requests](https://img.shields.io/badge/requests-2.31-red)](https://docs.python-requests.org/)
[![Groq API](https://img.shields.io/badge/groq-API-red)](https://www.groq.com/)
[![Google Places API](https://img.shields.io/badge/gplaces-API-blue)](https://developers.google.com/maps/documentation/places)
[![Google Weather API](https://img.shields.io/badge/weather-API-lightblue)](https://developers.google.com/weather)
[![ExchangeRates API](https://img.shields.io/badge/exchangerates-API-lightgreen)](https://exchangeratesapi.io/)
[![Google API](https://img.shields.io/badge/google-API-blue)](https://developers.google.com/)

The **AI Trip Planner** is an intelligent travel planning system powered by AI. It provides personalized itineraries, recommended attractions, hotels, and transportation suggestions, and adapts dynamically to user preferences.

## Features

- Personalized trip planning based on user preferences
- AI-powered itinerary generation for cities worldwide
- Recommendations for attractions, restaurants, and accommodations
- Dynamic adjustment of trip plan based on time, budget, and interests
- Web interface with interactive map and calendar view
- Natural language queries for travel suggestions

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-trip-planner.git
cd ai-trip-planner
```

### 2. Install Dependencies

```bash
pip install streamlit requests pandas numpy folium langchain openai
```

### 3. Configure API Keys

```python
# OpenAI API Key
import os
os.environ['OPENAI_API_KEY'] = 'YOUR_OPENAI_API_KEY'

# Optional: Any other APIs like Google Maps or TripAdvisor API
os.environ['GOOGLE_MAPS_API_KEY'] = 'YOUR_GOOGLE_MAPS_API_KEY'
```

### 4. Run the Application

```bash
streamlit run app.py
```

This will start the AI Trip Planner in your browser at `http://localhost:8501`.

## Usage

### Basic Example

```python
from ai_trip_planner import TripPlanner

# Initialize planner
planner = TripPlanner(user_preferences={
    "city": "Paris",
    "days": 5,
    "interests": ["museum", "food", "shopping"]
})

# Generate itinerary
itinerary = planner.generate_itinerary()
print(itinerary)
```

### Advanced Example with Custom Constraints

```python
custom_plan = planner.generate_itinerary(
    budget=1500,
    transportation="public",
    avoid=["museums on Monday"],
)
print(custom_plan)
```

### Streamlit Web Interface

- Upload preferences or enter city, days, and interests
- Generate AI-powered trip plan
- Visualize locations on an interactive map
- Export itinerary to PDF or shareable format

## Project Structure

```
ai-trip-planner/
├── app.py                # Streamlit main app
├── ai_trip_planner/      # Core AI logic module
│   ├── __init__.py
│   ├── planner.py        # Trip planning logic
│   └── utils.py          # Helper functions
├── requirements.txt
└── README.md
```

## References

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Maps API](https://developers.google.com/maps/documentation)
- [LangChain](https://www.langchain.com/docs/)



## Author

**Rathod Pavan Kumar Naik**  
- Email: bt22cse111@iiitn.ac.in  
- GitHub: [rathod-pavan](https://github.com/rathod-pavan)
