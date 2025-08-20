# AI Trip Planner

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/) [![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

The **AI Trip Planner** is an intelligent travel planning system powered by AI. It allows users to get personalized travel itineraries, recommended attractions, hotels, and transportation suggestions. The system leverages agentic AI to provide smart trip plans and adapts to user preferences.

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
- [OpenAI API](https://platform.openai.com/docs/)
- [Google Maps API](https://developers.google.com/maps/documentation)
- [LangChain](https://www.langchain.com/docs/)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Rathod Pavan Kumar Naik**  
- Email: bt22cse111@iiitn.ac.in  
- GitHub: [rathod-pavan](https://github.com/rathod-pavan)
