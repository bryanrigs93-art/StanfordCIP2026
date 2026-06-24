# My Perfect Gift — WhatsApp Chatbot

## Overview

This is my final project console version designed to run through the Code in Place WhatsApp chatbot feature.

The chatbot helps a customer choose a personalized gift by asking five quick questions and matching the answers with products from a real catalog.

## WhatsApp Demo

You can interact with this project directly through the Code in Place WhatsApp runner.

Send this message:

```text
PVXRMT
```

to this WhatsApp number:

```text
+1 (415) 728-3856
```

Shared message:

```text
Hey! I want you to see my Code in Place project. You can interact with my program directly on WhatsApp. Send message PVXRMT to +1 (415) 728-3856 to see it run!
```

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

## Files

- `my_perfect_gift_whatsapp_chatbot.py` — Console chatbot version for WhatsApp.
- `catalogo_real_mi_regalo_perfecto.csv` — Real product catalog used by the chatbot.

## Takeaway

This project helped me connect Python foundations with a real business workflow. The program uses data from a CSV catalog, applies rule-based filtering, and then calls GPT to create a more natural recommendation for the customer.
