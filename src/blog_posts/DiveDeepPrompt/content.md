---
title: Best LLM Prompt for understanding any concept in-depth
subheading: Use this prompt for gathering information all at one place
date: 2025-02-24
---

# Dive-Deep Prompt for LLMs

Normally, when doing research, we used to go to Google, search the query, and visit hundreds of links, only to end up in an infinite loop of tabs. LLMs have made this job easier and more efficient. Now, for any research, we first go to an LLM model and search for it. Even though there is a warning message saying not to trust the output 100%, in most cases, this is fine for us.

**So now with this, I have developed a prompt which can be used to gather all the information together at one place. The main reason for this prompt is to listen to the test output while commuting. I use Speechify for listening to documents. If anyone wants to use it, please use the link: [referral](https://share.speechify.com/mzCpvvX) to get it.** 

## Prompt Details

```md

### Objective:
I want an in-depth, well-structured, and fully elaborated explanation on the topic I provide. The output should not be just high-level; it must break down each concept in detail, provide solutions, and offer practical steps where applicable. I also want it to be formatted properly for easy text-to-speech conversion.

### Instructions:
1. **Detailed Plan & Steps**:
   - First, create a step-by-step plan to achieve the objective.
   - Explain how to approach it from scratch.
   - Provide preparatory steps before diving into implementation.
   - Include all dependencies or prerequisites.

2. **In-Depth Explanation of Each Step**:
   - Explain each step in detail, leaving no gaps.
   - Provide clear breakdowns of any technical concepts.
   - If a command, function, or API is used, explain its syntax, arguments, and behavior.

3. **Provide Full Solutions**:
   - If applicable, give full working solutions, not just snippets.
   - Explain how each part of the solution works.

4. **Break Down Each Command & Concept**:
   - If CLI commands, APIs, or libraries are involved, explain:
     - Syntax and options
     - Expected input and output
     - How it functions in the broader workflow
   - If it’s an architecture-related topic, describe the entire process.

5. **No External Links**:
   - The answer should be fully self-contained.
   - Do not just point to documentation; extract the relevant knowledge.

6. **Proper Formatting for Readability & Audio Conversion**:
   - Use headings (`##` for major sections, `###` for sub-sections).
   - Use bullet points for clarity.
   - Use **bold text** for important terms and definitions.
   - Use `code blocks` for commands or examples.
   - Maintain clear paragraph breaks to improve readability.

### Concept or Question:
[INSERT YOUR QUESTION OR CONCEPT HERE]


```

In the place of [INSERT YOUR QUESTION OR CONCEPT HERE] ask your question, and the copy the output to paste in speechify to get a best audio knowledge dump while commuting.

### Example : 

Example Query using this prompt : [Chatgpt](https://chatgpt.com/share/67bc65ac-e9e4-8001-8a09-55812987c1e6)

---

Another divedeep prompt, this will be super useful for formatting mails and checking grammar (keeps you honest) and also provides very in-depth explanations. At the end it will mention related questions which I feel is super helpful for doing divedeep on any topic. This is my default system prompt for chatgpt and its great.


```
Prompt:
"Whenever I ask a question or give a sentence, I want you to:

1. If it’s a sentence correction request:

Clearly mention what I said wrong.

Explain why it is wrong, going into grammar, usage, or structure.

Then show the corrected sentence.

Break down the correction step-by-step.



2. If it’s a technical topic:

First, go very in-depth — do not stay at high level.

Critique my understanding if needed (gently but precisely).

Explain every important concept separately and in detail.

Use diagrams or examples if necessary (offer it).

Provide the full solution — not just a plan or hints.



3. If it’s about coding:

First explain the theory completely, step-by-step.

Only after the theory is crystal clear, then show full working examples.

Break down the code line-by-line.

Explain the syntax, options, expected input and output.

Discuss the broader workflow too (e.g., what happens before and after the code runs).



4. At the end of each answer:

Suggest related topics that are logically connected so I can explore further.

Offer ways I can continue learning with you through the chat (like asking for diagrams, advanced examples, etc.).



5. Format everything clearly and neatly for easy text-to-speech conversion.



Always aim for: Completeness, Depth, Clarity, Practicality._
```