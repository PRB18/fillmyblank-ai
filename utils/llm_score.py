import requests

def llama_score_sentence(user_sentence, correct_answer, api_url="http://localhost:8000/completion"):
    prompt = (
        f"Task: Score the learner's answer for a fill-in-the-blank question.\n"
        f"Question: What is the correct answer? {correct_answer}\n"
        f"User's answer: {user_sentence}\n"
        f"Is the answer correct? (yes/no). If not, briefly explain why."
    )
    
    # Try different API formats based on the URL
    try:
        if "fumes-api.onrender.com" in api_url:
            # Format for the fumes API
            payload = {
                "model": "llama3",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 50,
                "temperature": 0.2
            }
        else:
            # Original format for other APIs
            payload = {"prompt": prompt, "n_predict": 32, "temperature": 0.2, "stream": False}
        
        resp = requests.post(api_url, json=payload, timeout=10)
        
        if resp.status_code == 200:
            result = resp.json()
            # Handle different response formats
            if 'choices' in result and len(result['choices']) > 0:
                return result['choices'][0]['message']['content']
            elif 'content' in result:
                return result['content']
            else:
                return str(result)
        else:
            return f"API Error {resp.status_code}: {resp.text}"
            
    except requests.exceptions.RequestException as e:
        return f"Connection Error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"