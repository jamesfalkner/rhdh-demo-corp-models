# Red Hat Developer Hub LLM Catalog

This repository contains a comprehensive catalog of Large Language Models (LLMs) configured for Red Hat Developer Hub. The catalog includes realistic LLM definitions, user/group entities, and API specifications for enterprise AI/ML platform integration.

## Contents

- **LLM Entities**: 10 different LLM models from various providers (Anthropic, OpenAI, Meta, Google, etc.)
- **User & Group Definitions**: Platform team and AI platform team with realistic team members
- **API Specifications**: Complete OpenAPI 3.0 definitions for each LLM's REST API
- **OpenShift AI Integration**: All models configured with OpenShift AI endpoints

## Models Included

- Claude 3.5 Sonnet (Anthropic)
- GPT-4o (OpenAI)
- Llama 3.1 70B (Meta)
- Gemini 1.5 Pro (Google)
- Mistral 7B Instruct (Mistral AI)
- CodeLlama 34B (Meta)
- Qwen 2.5 72B (Alibaba)
- Phi-3 Medium (Microsoft)
- DeepSeek Coder 33B (DeepSeek)
- Mixtral 8x7B Instruct (Mistral AI)

## Usage

This catalog can be imported into Red Hat Developer Hub to provide a comprehensive view of available LLM services, their APIs, and the teams responsible for managing them.

## File Structure

```
├── catalog-info.yaml    # Main catalog file with all entities
└── README.md           # This file
```

## Import Instructions

1. Copy the `catalog-info.yaml` file to your Red Hat Developer Hub instance
2. Configure the catalog to point to this file location
3. The catalog will automatically load all LLM entities, users, groups, and API definitions

## Features

- **Realistic Team Structure**: Platform team and AI platform team with detailed member profiles
- **Complete API Documentation**: OpenAPI 3.0 specs for each LLM with proper request/response schemas
- **OpenShift AI Integration**: All endpoints configured for OpenShift AI platform
- **Enterprise Ready**: Proper tagging, lifecycle management, and ownership definitions
- **Multimodal Support**: APIs configured for models that support text, image, and audio inputs
- **Code-Specific Models**: Specialized configurations for code generation models

## Contributing

This catalog is designed to be a realistic example for Red Hat Developer Hub. Feel free to modify the entities, add new models, or adjust team structures to match your organization's needs.
