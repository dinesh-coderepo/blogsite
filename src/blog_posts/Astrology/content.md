---
title: Developing a Astrology web app users will love
subheading: Making of astrology app to revolutionize the way we use atro with AI and LLMs
date: 2024-08-07
---

# Devloping a Astrology web app using replit AI and deploying to webapp.


## Using Replit AI to Generate Basic UI

To kickstart our astrology web app, we'll leverage Replit AI to generate the basic placeholder for the initial version of the app to host. The idea is to develop a full-fledged subscription model app with the following features:

1. Customer Perspective:
   - Access via phone or mobile for daily predictions
   - Push notifications or email for daily astrology insights
   - Login using Google (initially)
   - Customer-specific view
   - Features:
     - One-time overall life prediction
     - Daily suggestions and weekly forecasts
   - Daily predictions should be actionable and suggestive:
     - What color to wear
     - What mantra to say
     - Recommended poojas
   - 1 week free prediction with monthly payment options
   - Paid content visible only to subscribed customers
   - Future scope: mobile app version

2. Technology Perspective:
   - Collate accurate astrology material
   - Research existing apps and implement successful flows
   - Integrate AI component (LLMs) for text-based content generation
   - Explore RAG (Retrieval-Augmented Generation) to integrate knowledge base with LLM

### Initial Placeholder app Development with Replit AI

1. **Generating Initial Version:**
   - Used Replit AI agent to create a placeholder app
   - AI executed and corrected code autonomously
   - Effective for small-scale projects

   ![Replit AI Agent](./replit1.png)

2. **Setup:**
   - AI agent set up dependencies and installation
   - Iterative error correction
   - Suitable for small-scale projects

   ![Replit AI Agent](./replit2.png)

3. **Generated Code:**
   - Available in Replit repo: [AstroGuide](https://replit.com/@maluchurudinesh/AstroGuide?v=1)

4. **Local Development:**
   - Imported code to local Cursor environment
   - Set up app to run locally
   - Replit can generate a README.md with dependency information

5. **Deployment and hosting:**
    - Initial version of the app is now ready , this is a placeholder version until all the other features are implemented and added.
    - Purchased the domain astroyuga.com in AWS.
    - Using the same approach as blogapp ,deploying to webapp using githubactions and then bind the domain to the webapp.
    - Binding of aws domain to webapp, I am doing this for the first time , will document the approach.

6. **CI and CD using github actions:**
    - Will include one implemented

7. **Domain binding to webapp:**
    - First time doing this , will document the approach.





