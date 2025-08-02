import requests
import json
import random
import time

# Hugging Face API configuration
HF_API_URL = "https://api-inference.huggingface.co/models/google/gemma-2b-it"

def generate_dynamic_question(game_type, language, api_key, difficulty="beginner"):
    """Generate dynamic questions using AI based on game type and language"""
    
    language_names = {
        "en": "English",
        "hi": "Hindi", 
        "te": "Telugu"
    }
    
    lang_name = language_names.get(language, "English")

    # Expanded topics for more variety
    topics = {
        "fill_in_blank": ["geography", "science", "history", "culture", "technology", "art", "literature"],
        "match_the_following": ["animals and their sounds", "countries and capitals", "words and meanings", "inventions and inventors", "food and cuisine"],
        "story_completion": ["adventure", "mystery", "friendship", "fantasy", "daily life"]
    }
    
    selected_topic = random.choice(topics.get(game_type, ["general knowledge"]))
    
    if game_type == "fill_in_blank":
        prompt = f"""Generate a unique, {difficulty} level fill-in-the-blank question in {lang_name} about {selected_topic}.
        
Format your response as a single, valid JSON object:
{{
    "prompt": "A question with a ____ blank.",
    "answer": "The correct word or phrase."
}}

Ensure the question is different from common examples.
Make it educational and appropriate for language learners."""

    elif game_type == "match_the_following":
        prompt = f"""Generate a unique, {difficulty} level matching exercise in {lang_name} about {selected_topic}.
        
Format your response as a single, valid JSON object:
{{
    "left": ["item1", "item2", "item3"],
    "right": ["match1", "match2", "match3"],
    "answer": [0, 1, 2]
}}

Create 3 distinct items to match. Ensure the pairs are logical and clear."""

    elif game_type == "story_completion":
        prompt = f"""Generate a unique, {difficulty} level story completion prompt in {lang_name} with a theme of {selected_topic}.
        
Format your response as a single, valid JSON object:
{{
    "story": "A short story with a ___ to complete.",
    "answer": "An appropriate word to complete the story."
}}

Create an engaging short story that needs one word to complete meaningfully."""

    else:
        return None
    
    if not api_key:
        print("Hugging Face API key not found. Using fallback.")
        return get_smart_fallback_question(game_type, language)

    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 150,
            "temperature": 0.7,
            "return_full_text": False
        }
    }

    try:
        response = requests.post(HF_API_URL, headers=headers, json=payload, timeout=20)
        
        if response.status_code == 200:
            result = response.json()
            generated_text = result[0]['generated_text']
            
            # Clean and parse the JSON response from the model
            try:
                start = generated_text.find('{')
                end = generated_text.rfind('}') + 1
                if start != -1 and end > start:
                    json_str = generated_text[start:end]
                    question_data = json.loads(json_str)
                    return question_data
                else:
                    raise ValueError("No valid JSON found in response.")
            except (json.JSONDecodeError, ValueError) as e:
                print(f"Failed to parse JSON from AI response: {e}")
                return get_smart_fallback_question(game_type, language)
        else:
            print(f"API Error: {response.status_code} - {response.text}")
            return get_smart_fallback_question(game_type, language)

    except requests.exceptions.RequestException as e:
        print(f"Error calling Hugging Face API: {e}")
        return get_smart_fallback_question(game_type, language)

def get_smart_fallback_question(game_type, language):
    """Smart fallback with variety and no repetition"""
    import time
    
    # Use timestamp to ensure variety
    seed = int(time.time()) % 100
    
    expanded_fallbacks = {
        "en": {
            "fill_in_blank": [
                {"prompt": "The sun rises in the ____.", "answer": "east"},
                {"prompt": "Water boils at ____ degrees Celsius.", "answer": "100"},
                {"prompt": "The largest ocean is the ____.", "answer": "Pacific"},
                {"prompt": "The capital of Japan is ____.", "answer": "Tokyo"},
                {"prompt": "There are ____ continents on Earth.", "answer": "seven"},
                {"prompt": "The fastest land animal is the ____.", "answer": "cheetah"},
                {"prompt": "Gold has the chemical symbol ____.", "answer": "Au"},
                {"prompt": "The Great Wall of China is in ____.", "answer": "China"},
                {"prompt": "Shakespeare wrote ____.", "answer": "Hamlet"},
                {"prompt": "The human body has ____ bones.", "answer": "206"}
            ],
            "match_the_following": [
                {
                    "left": ["Red", "Blue", "Yellow"],
                    "right": ["Apple", "Sky", "Sun"],
                    "answer": [0, 1, 2]
                },
                {
                    "left": ["Dog", "Cat", "Cow"],
                    "right": ["Barks", "Meows", "Moos"],
                    "answer": [0, 1, 2]
                },
                {
                    "left": ["France", "Italy", "Spain"],
                    "right": ["Paris", "Rome", "Madrid"],
                    "answer": [0, 1, 2]
                },
                {
                    "left": ["Circle", "Square", "Triangle"],
                    "right": ["Round", "Four sides", "Three sides"],
                    "answer": [0, 1, 2]
                }
            ],
            "story_completion": [
                {"story": "The brave knight rescued the princess from the ____.", "answer": "dragon"},
                {"story": "After a long journey, the traveler finally reached the ____.", "answer": "destination"},
                {"story": "The little bird built its nest in the ____.", "answer": "tree"},
                {"story": "The detective solved the mystery using a ____.", "answer": "clue"},
                {"story": "The chef prepared a delicious meal with fresh ____.", "answer": "ingredients"}
            ]
        },
        "hi": {
            "fill_in_blank": [
                {"prompt": "सूर्य ____ में उगता है।", "answer": "पूर्व"},
                {"prompt": "पानी ____ डिग्री पर उबलता है।", "answer": "100"},
                {"prompt": "भारत की राजधानी ____ है।", "answer": "दिल्ली"},
                {"prompt": "गंगा नदी ____ से निकलती है।", "answer": "गंगोत्री"},
                {"prompt": "एक सप्ताह में ____ दिन होते हैं।", "answer": "सात"},
                {"prompt": "हमारे देश का राष्ट्रीय पक्षी ____ है।", "answer": "मोर"}
            ],
            "match_the_following": [
                {
                    "left": ["लाल", "नीला", "पीला"],
                    "right": ["सेब", "आकाश", "सूर्य"],
                    "answer": [0, 1, 2]
                },
                {
                    "left": ["गाय", "बिल्ली", "कुत्ता"],
                    "right": ["दूध", "म्याऊं", "भौंकना"],
                    "answer": [0, 1, 2]
                }
            ],
            "story_completion": [
                {"story": "बहादुर राजा ने राजकुमारी को ____ से बचाया।", "answer": "राक्षस"},
                {"story": "बच्चे बगीचे में ____ खेल रहे थे।", "answer": "क्रिकेट"},
                {"story": "किसान ने खेत में ____ बोया।", "answer": "बीज"}
            ]
        },
        "te": {
            "fill_in_blank": [
                {"prompt": "సూర్యుడు ____ దిశలో ఉదయిస్తాడు.", "answer": "తూర్పు"},
                {"prompt": "నీరు ____ డిగ్రీల వద్ద మరుగుతుంది.", "answer": "100"},
                {"prompt": "భారతదేశ రాజధాని ____.", "answer": "న్యూఢిల్లీ"},
                {"prompt": "వారంలో ____ రోజులు ఉంటాయి.", "answer": "ఏడు"}
            ],
            "match_the_following": [
                {
                    "left": ["ఎరుపు", "నీలం", "పసుపు"],
                    "right": ["ఆపిల్", "ఆకాశం", "సూర్యుడు"],
                    "answer": [0, 1, 2]
                }
            ],
            "story_completion": [
                {"story": "వీరుడు రాజకుమారిని ____ నుండి రక్షించాడు.", "answer": "రాక్షసుడు"},
                {"story": "పిల్లలు తోటలో ____ ఆడుకుంటున్నారు.", "answer": "ఆట"}
            ]
        }
    }
    
    lang_fallbacks = expanded_fallbacks.get(language, expanded_fallbacks["en"])
    game_fallbacks = lang_fallbacks.get(game_type, lang_fallbacks["fill_in_blank"])
    
    # Use seed to pick different questions each time
    question_index = seed % len(game_fallbacks)
    return game_fallbacks[question_index]
