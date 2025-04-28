from google import genai
from google.genai import types

def generate_tagline():
    client = genai.Client(
        vertexai=True,
        project="YOUR_PROJECT_ID",
        location="us-central1",
    )

    system_instruction_text = (
        "You are an expert tagline generator. "
        "Always include the keyword 'nature' in the tagline. "
        "Use the provided product attributes, target audience, and emotional tone."
    )

    model = "gemini-2.0-flash-001"

    user_prompt = """
Product Attributes: Lightweight, durable hiking boots, waterproof, designed for rugged mountain terrain.
Target Audience: Young adventure seekers, nature lovers, and eco-conscious travelers.
Emotional Tone: Bold, inspiring, adventurous.

Generate a short, catchy tagline that includes the word 'nature'.
"""

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=user_prompt)
            ]
        ),
    ]

    generate_content_config = types.GenerateContentConfig(
        temperature=1.0,  # Creative, but not random
        top_p=0.95,
        max_output_tokens=512,
        response_modalities=["TEXT"],
        system_instruction=system_instruction_text,
        safety_settings=[
            types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="OFF"),
            types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="OFF"),
            types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="OFF"),
            types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="OFF"),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

generate_tagline()

