# Vertex AI Challenge Project: Cymbal Direct AI Tools

This repository contains projects built for the Google Cloud Vertex AI Challenge Course.  
The project involves creating AI-powered tools using the Gemini 2.0 Flash model in Vertex AI Studio, focused on image analysis and tagline generation for Cymbal Direct’s new outdoor product line.

## Project Overview

| Task | Description | Output |
|:---|:---|:---|
| Task 1 | Image analysis from product photos using Gemini | `image-analysis.ipynb` |
| Task 2 | Customizable tagline generator based on product attributes, target audience, and emotional tone | `tagline-generator.ipynb` |
| Task 3 | Modify image analysis to produce short, creative descriptions | Updates inside `image-analysis.ipynb` |
| Task 4 | Modify tagline generation to enforce inclusion of a keyword ("nature") | Updates inside `tagline-generator.ipynb` |

## Requirements

- Python 3.10+
- Google Cloud SDK installed (`gcloud auth application-default login`)
- Vertex AI API enabled
- IAM roles: Vertex AI User, Storage Object Viewer

## Setup Instructions

Clone the repository:
   ```bash
   git clone https://github.com/your-username/vertex-ai-cymbal-direct.git
   cd vertex-ai-cymbal-direct

