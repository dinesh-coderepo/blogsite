---
title: Leveraging Cursor and Azure for Rapid Website Deployment
subheading: Accelerating Development and Deployment Cycles with AI Tools
date: 2024-08-05
---

# Rapid Development and Deployment Using AI Tools

In this blog post, I'll share my experience using Cursor (an AI-powered development tool) and Microsoft Azure to streamline the process of developing and deploying a website. This combination has significantly accelerated my development and deployment cycle.

## Key Components

1. **Cursor**: An AI-assisted development environment
2. **Azure**: Microsoft's cloud platform for deployment
3. **GitHub Actions**: For continuous integration and deployment

## Essential Commands and Configurations

### Package Management
To capture all required packages for deployment:

    # To get all the packages, which then can be installed later using pip
    # This is needed while deploying using GitHub Actions and while setting up virtual env
    pip list --format=freeze > requirements.txt

### Azure Web App Configuration
In the Azure portal:
1. Go to "Configuration" under the "Settings" section.
2. In the "General settings" tab, find the "Startup Command" field.
3. Enter the following command:

    gunicorn --bind 0.0.0.0:$PORT src.app:app

This tells Azure to run gunicorn and look for the app object in the src.app module.

### Domain Configuration
- Azure Web App domain: `blogging.azurewebsites.net`
- Custom domain bound to the web app: `dineshblog.com`

## Development Process

1. **Learning Resources**:
   - [Microsoft Learn: Building AI web apps with Python and Flask](https://learn.microsoft.com/en-us/training/modules/python-flask-build-ai-web-app/0-introduction?source=learn)
   - [MDN Web Docs: HTML basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)

2. **Version Control**:
   - Project repository: [https://github.com/dinesh-coderepo/blogsite](https://github.com/dinesh-coderepo/blogsite)

3. **Azure Service Principal**:
   - Name: [bloggerdeployment](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationMenuBlade/~/Overview/quickStartType~/null/sourceType/Microsoft_AAD_IAM/appId/e91edd51-068a-4702-89de-5b674ab452dc/objectId/3fa0d802-a84e-450f-a12f-16a6967e5fed/isMSAApp~/false/defaultBlade/Overview/appSignInAudience/AzureADMyOrg/servicePrincipalCreated~/true)
   - Note: To access the Azure Key Vault, the service principal needs to be added to federated credentials in the app registration.

4. **Deployment**:
   - Successfully deployed using GitHub Actions: [Deployment Log](https://github.com/dinesh-coderepo/blogsite/actions/runs/10720927625/job/29728277249)

## Key Learnings and Tips

1. **Service Principal Authentication**: To login to a service principal and access the key vault, you need to add it to federated credentials in the app registration.

2. **Continuous Integration**: The project uses GitHub Actions for CI/CD, ensuring smooth and automated deployments.

3. **Resource Management**: Proper configuration of Azure resources, including the web app and custom domain, is crucial for successful deployment.

4. **AI-Assisted Development**: Cursor's AI capabilities significantly speed up the coding process, allowing for rapid prototyping and development.

## Next Steps: Enhancing the Blog

For the next iteration, I plan to implement a blog-style website with a modern touch:

- No user authentication required
- Read-only content, updated through deployments
- Home page featuring blog post titles and subheadings
- Clickable blog posts that open individual pages

## Conclusion

By combining Cursor's AI-powered development capabilities with Azure's robust deployment options and GitHub Actions for CI/CD, I've created a streamlined process for website development and deployment. This approach significantly reduces development time and simplifies the deployment process, allowing for rapid iterations and updates.

The synergy between AI-assisted coding and cloud deployment platforms represents a powerful shift in web development practices. As we continue to explore these technologies, we can expect even more efficient and innovative ways to build and deploy web applications.

For those interested in diving deeper into this approach, I recommend starting with the Microsoft Learn modules and gradually integrating AI tools like Cursor into your development workflow. The combination of AI assistance in coding and streamlined cloud deployment can dramatically improve your productivity and the quality of your web projects.