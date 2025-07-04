import random
from sentiment_analysis import analyze_sentiment
from coping_mechanisms import get_coping_mechanism, get_crisis_resources

def chatbot_response(user_input):
    user_input_lower = user_input.lower()
    sentiment_result = analyze_sentiment(user_input_lower)
    sentiment_category = sentiment_result['category']
    # Use a compound-like score for thresholds, actual values based on mapping in sentiment_analysis.py
    sentiment_compound_for_logic = sentiment_result['compound']

    # --- Crisis Detection (Highest Priority) ---
    crisis_keywords = ["suicide", "end my life", "kill myself", "can't go on", "hopeless", "harm myself", "worthless"]
    if any(keyword in user_input_lower for keyword in crisis_keywords) or sentiment_compound_for_logic < -0.8: # Example threshold
        return get_crisis_resources()

    # --- Sentiment-based Responses ---
    if sentiment_category == 'negative':
        responses = [
            "It sounds like you're going through a tough time. I'm here to listen.",
            "I hear you. Feeling down or stressed is really hard. What's on your mind?",
            "It's okay to feel this way. Sometimes, just talking about it can help a little.",
            "I'm sorry you're feeling negative right now. Remember, it's temporary."
        ]
        response_prefix = random.choice(responses)
        coping_suggestion = get_coping_mechanism(sentiment_compound_for_logic)
        return f"{response_prefix} {coping_suggestion}"
    elif sentiment_category == 'positive':
        responses = [
            "That's great to hear!",
            "I'm happy you're feeling positive!",
            "Awesome! Keep up the good vibes.",
            "It's wonderful that you're feeling good."
        ]
        return random.choice(responses) + " Is there anything else you'd like to talk about or explore?"
    else: # Neutral sentiment or no strong emotion detected
        if "hello" in user_input_lower or "hi" in user_input_lower:
            return "Hi there! How are you feeling today?"
        elif "how are you" in user_input_lower:
            return "I'm just a program, but I'm here and ready to chat with you!"
        elif "coping" in user_input_lower or "help me feel better" in user_input_lower:
            return get_coping_mechanism(sentiment_compound_for_logic)
        elif "thank you" in user_input_lower or "thanks" in user_input_lower:
            return "You're welcome! I'm here to help."
        elif "about you" in user_input_lower:
            return "I'm a chatbot designed to provide support and information about mental well-being for teenagers. I'm not a human therapist, but I can offer some tools and resources."
        elif "disclaimer" in user_input_lower or "what can you do" in user_input_lower:
             return ("I'm here to offer support, information about coping mechanisms, and direct you to professional resources. "
                     "I cannot diagnose, treat, or replace professional mental health care. "
                     "If you are in crisis, please contact emergency services or a crisis hotline immediately.")
        else:
            return "I'm not sure I understand. Can you tell me more about what's on your mind? Or would you like to talk about coping strategies?"

def main():
    print("Welcome to your Mental Well-being Chatbot for Teenagers!")
    print("Disclaimer: I'm here to offer support and information, not to replace professional help. "
          "If you are in crisis, please reach out to emergency services or a crisis hotline immediately.")
    print("Type 'exit' to end our chat.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Thanks for chatting! Remember, it's okay to ask for help.")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()