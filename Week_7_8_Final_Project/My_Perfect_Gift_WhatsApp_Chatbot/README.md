# My Perfect Gift — WhatsApp Chatbot

## Overview

This is my final project console version designed to run through the Code in Place WhatsApp chatbot feature.

The chatbot helps a customer choose a personalized gift by asking five quick questions and matching the answers with products from a real catalog.

## How It Works

1. The user chooses English or Spanish.
2. The chatbot explains that it uses a CSV catalog uploaded to the IDE.
3. Python reads the CSV file and filters products based on the user's answers.
4. The program builds a structured prompt using the best product matches.
5. GPT is called to generate a clear recommendation ready for WhatsApp.
6. At the end, the user can return to the main menu or finish the conversation.

## Required CSV File

The program expects a CSV file with this exact name:

```text
catalogo_real_mi_regalo_perfecto.csv
```

That file works as the product catalog database for the chatbot.

## Main Concepts

- File reading
- CSV parsing
- Lists
- Dictionaries
- String cleaning
- Conditional logic
- Scoring logic
- User input
- GPT-assisted recommendation
- WhatsApp chatbot workflow

## File

- `my_perfect_gift_whatsapp_chatbot.py` — Console chatbot version for WhatsApp.

## Takeaway

This project helped me connect Python foundations with a real business workflow. The program uses data from a CSV catalog, applies rule-based filtering, and then calls GPT to create a more natural recommendation for the customer.
