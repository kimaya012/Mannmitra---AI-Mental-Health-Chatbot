import random

COPING_STRATEGIES = {
    "mild_negative": [
        "How about trying a quick deep breathing exercise? Take a slow breath in for 4 counts, hold for 7, and exhale for 8.",
        "Sometimes, just moving your body helps. Could you take a short walk or stretch?",
        "Journaling can be a great way to process thoughts. Try writing down what's on your mind.",
        "Listening to your favorite music can sometimes shift your mood. Have you tried that?",
        "Focus on your senses: What 5 things can you see? 4 things you can hear? 3 things you can feel?",
        "It might help to talk to someone you trust, like a friend, family member, or school counselor.",
        "Take a few moments to name three things you're grateful for, no matter how small."
    ],
    "moderate_negative": [
        "It sounds like you need some extra support. Have you considered trying a grounding exercise like the 5-4-3-2-1 technique?",
        "When things feel overwhelming, breaking them down into smaller steps can help. What's one small thing you could focus on right now?",
        "Taking a break from screens and spending a few minutes outside can sometimes make a difference. Even just looking out a window.",
        "Remember, it's okay to not be okay. Sometimes, just acknowledging your feelings is a step forward. What's one feeling that's strong for you right now?",
        "If you're feeling really stuck, sometimes a change of scenery, even just a different room, can help reset your mind."
    ],
    "general": [ 
        "Deep breathing can be really helpful. Would you like me to guide you through one?",
        "Exploring a creative outlet like drawing, writing, or listening to music can be a good way to express yourself.",
        "Spending time in nature, even just a few minutes, can be calming.",
        "Connecting with friends or family who make you feel good can offer support.",
        "What's a hobby or activity you enjoy? Sometimes doing something fun can lift your spirits.",
        "Ensuring you're getting enough sleep and eating regularly can also impact how you feel."
    ]
}

# --- CRISIS_RESOURCES FOR INDIA ---
CRISIS_RESOURCES = (
    "\nI hear how much pain you're in, and your safety is the most important thing. "
    "Please reach out for immediate help in India:\n"
    "📞 **AASRA (Mumbai): +91-9820466726** (24/7)\n"
    "📞 **Vandrevala Foundation (National): +91-9999666555** (24/7)\n"
    "📞 **KIRAN Mental Health Rehabilitation Helpline (Govt of India): 1800-599-0019** (24/7, Toll-Free)\n"
    "🌍 **For a wider list of helplines in India, visit:** https://www.indianpsychiatricsociety.org/helpline/\n"
    "🚨 **In an emergency, please call your local emergency services (e.g., Police: 112 or 100, Ambulance: 102).**\n"
    "Please know you are not alone, and help is available."
)

def get_coping_mechanism(sentiment_score):
    """
    Returns a coping mechanism based on the sentiment score.
    A more sophisticated system would match specific emotions to specific coping skills.
    """
    if sentiment_score <= -0.5: # More severe negative (using compound-like score)
        return random.choice(COPING_STRATEGIES["moderate_negative"])
    elif sentiment_score < 0: # General negative (using compound-like score)
        return random.choice(COPING_STRATEGIES["mild_negative"])
    else: # Neutral or positive, or just general request for coping
        return random.choice(COPING_STRATEGIES["general"])

def get_crisis_resources():
    """
    Provides immediate crisis intervention resources.
    """
    return CRISIS_RESOURCES

if __name__ == "__main__":
    print("--- Testing Coping Mechanisms ---")
    print(f"For very negative: {get_coping_mechanism(-0.8)}")
    print(f"For negative: {get_coping_mechanism(-0.3)}")
    print(f"For neutral: {get_coping_mechanism(0.1)}")
    print(f"For positive: {get_coping_mechanism(0.7)}")

    print("\n--- Testing Crisis Resources ---")

    print(get_crisis_resources())
