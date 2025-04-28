from google import genai
from google.genai import types

def analyze_image():
    client = genai.Client(
        vertexai=True,
        project="YOUR_PROJECT_ID",
        location="us-central1",
    )

    system_instruction_text = (
        "Describe the image in fewer than 10 words. "
        "Be extremely creative, unusual, and imaginative."
    )

    model = "gemini-2.0-flash-001"

    # Replace with your actual image bytes
    image_path = "path_to_local_or_gcs_image.png"
    with open(image_path, "rb") as f:
        image_data = f.read()

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_data(data=image_data, mime_type="image/png")
            ]
        ),
    ]

    generate_content_config = types.GenerateContentConfig(
        temperature=1.2,  # Higher creativity
        top_p=0.9,
        max_output_tokens=128,
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

analyze_image()
