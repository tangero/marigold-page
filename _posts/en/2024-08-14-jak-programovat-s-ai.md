---
audio_url: http://www.marigold.cz/audio/2024-07-14-jak-programovat-s-ai.mp3
author: Patrick Zandl
categories:
- AI
- Umělá inteligence
content_hash: 7180fe0ff4989540cbbd26c9bf755486
hide: true
lang: en
layout: post
original_lang: cs
permalink: /en/item/jak-programovat-s-ai/
post_excerpt: With artificial intelligence, programming has become accessible even
  to people who can't program. In this article, we'll look at how to develop apps
  using AI when you can't program yourself.
thumbnail: https://www.marigold.cz/assets/prgramovani-s-ai.png
title: A guide to programming with AI when you can't program
translated: true
---

Last time, we discussed [how to use AI to write better articles, reports and texts](/item/how-to-write-articles-with-the-help-of-artificial-intelligence-ai/). AI has changed yet another thing. Suddenly, non-programmers can program too. And that's what we're going to look at today. So this article is not for programmers to increase their productivity, but for non-programmers who occasionally need to create a program.

  

Programming has a major disadvantage over many other creative practices: you have to know something about it. If you open a development environment, you have to know how to compose commands for yourself, and until you do it right, nothing works. If you want to write or draw, you might not write or draw anything particularly pretty, but somehow it will work. With programming, it doesn't - you either know how to do it, or you don't do shit.

  

But AI changes that. If you subscribe to ChatGPT or Claude, you can let AI create even very large programs for you. Of course, it's better to start with smaller scripts and get a bit familiar with the whole thing.

  

Let's take a look at how to do it.

  

**First, you need to be clear about what you want to create.** Definitely don't assume that AI will generate Facebook-scale sites in one fell swoop. First of all. Second, it's good to know something about web development and operations, obviously the more the better, but any basics are useful. Thirdly, think of AI as a more experienced colleague that you can ask for, but you have to explain it well.

  

The process of building an AI program is an iterative process. You have an input - that is, a baseline and the conditions from which it starts. Then you have the output - what you want to get and what you want it to look like. And in between is the magic that laymen tend not to care about, which we now hope AI will solve.

  

Let's take an example. For example, I use a system for logging projects where I write down what I've done and follow it with a hash of the name of the project or work. For example "I order a new server #marigold". I write that down in Excel. Now I want to have a web service where firstly I note this down, secondly I can list all these notes. It's a relatively simple application for our AI programming example.

  

**So let's be clear about the brief for this app:**

- data is entered via a web form in any short text format and can contain a hashtag, i.e. a word starting with #

- this data can be output by date and also limited to a specific hashtag

- as this is a web service accessible from the internet, it will be appropriate to make the data available only to the logged-in user

  

And that is actually the whole brief of our project. Deliberately ripped off, which an experienced designer would rightly accuse me of, but we'll see why later.

  

Let's assume you're paying for ChatGPT, but the procedure will be similar for other tools like Claude. In ChatGPT, however, you have the advantage of being able to use GPT. Find in the Explore GPT section a tool called [*Code Copilot*](https://chatgpt.com/g/g-5qFFjp0bP-code-copilot), it is a great customized tool to support programming. Let's insert roughly this prompt:

  

> Hi, I need to create a web application. The application should allow user registration and login. The logged in user can enter text in the text input field which will be saved. It is saved including the date and time of entry. Another page allows to list all the entered texts in a selectable time range and sort them by hashtag. The next page generates a cloud of hashtags including frequency of use. I expect the service to be underused. What programming language and approach do you consider most appropriate for this assignment? I would like to generate readable code and you can help me choose a hosting where I can easily deploy this code, everything will be readable and understandable for a beginner. I would like the hosting to be free or paid depending on the frequency of use. First, give me a summary of your recommendations for programming language and for hosting, describe the pros and cons.

Code Copilot (CC) will offer to implement the solution in Python, using the Flask framework for the backend and Jinja2 for the frontend. This is where it comes in handy if you know roughly what's going on, we won't explain.

  

> ### Recommendations for programming language and framework
>
>
>
> **Language:** Python
>
> **Framework:** Flask (for backend) and Jinja2 (for frontend templates)
>
>
>
> > #### Benefits:
>
> - **Simplicity:** Python is a language known for its readability and ease of learning, making it ideal for beginners.

> - **Flask:** It is a lightweight web framework that is simple to use, allows for rapid prototyping, and provides flexibility in
> application development. Flask is very well documented, which makes it easy to
> development and troubleshooting.
>
> - **Wide support:** Python and Flask have a large community and a number of libraries that can simplify work (for example, to manage
> users, working with databases, or generating graphs and word clouds).
>
> - **Flexibility:** Flask is very modular, allowing easy integration with different databases (e.g. SQLite for easy deployment).
> > and front-end frameworks.
>
> - **Learnability:** Python has a simple and readable syntax, making it a great choice for learning and understanding web development.
>
>
>
> > #### Disadvantages:
>
> - **Performance:** Flask is not as powerful as other full-featured frameworks like Django or Node.js, but for an underutilized
> service, this shouldn't be a problem.
>
> - **Less features:** Flask doesn't provide as many built-in features as more robust frameworks (like Django), which means that some features
> you'll have to implement some features yourself.
>
>
>
> ### Hosting Recommendations
>
>
>
> **Hosting Platform:** Heroku
>
>
>
> > #### Benefits:
>
> - **Easy deployment:** Heroku offers easy deployment of applications directly from GitHub or via the command line, which is convenient for
> > beginners.
>
> - **Free:** Heroku offers a free plan, which is suitable for small and low-usage applications. Paid plans are available for larger
> > scaling.
>
> - **Python support:** Heroku has built-in support for Python and Flask applications, allowing for easy integration and deployment.
>
> - **Databases:** Heroku offers built-in support for PostgreSQL databases, giving you a scalable and reliable database directly
> on the platform.
>
>
>
> > #### Disadvantages:
>
> - **Limited resources on the free plan:** The free Heroku plan has a limit on the number of hours the app can run per month and may not be suitable.
> > for applications with high traffic or large databases.
>
> - **Inactivity startup:** Applications deployed on the free plan may sleep after inactivity and may be slower when restarted.
> response time.
>
>
>
> ### Alternative options
>
>
>
> - **Vercel or Netlify:** These platforms are mainly focused on the front-end, but can also be used for full-stack applications using
> serverless features. They are also very beginner friendly and have
> free plans.
>
> - **Render:** An alternative to Heroku that offers similar deployment options with a simple user interface and free plans.
>
>
>
> ### Summary
>
>
>
> I recommend using Python with Flask to develop your web application.
> This approach will give you readable and flexible code that is easily
> understandable for beginners. For hosting, I would recommend Heroku,
> because it offers easy deployment and a free plan suitable for smaller
> projects.
>
>
>
> **a.** Do you want to proceed with the implementation of the application backend using Flask?
>
> **b.** Should I help you set up the project and prepare the code for basic functionality such as user registration and text storage?

CC will also recommend platforms for hosting Python, he suggests using Heroku, alternatively Vercel, Netlify or Render, all very valid choices. But how come he didn't recommend, say, Amazon AWS or MS Azure when there are ads for them everywhere? Let's ask:

  

> Why didn't you recommend AWS, Azure or Google Cloud?

CC answers that these are very complex platforms that will be difficult for a beginner to set up. Heroku, Vercel, and similar platforms are focused on simplicity and user-friendliness, which is good for lower-end projects and for users who don't want to deal with complex configuration. Which I can attest to, setting up AWS/Azure is tedious for a beginner. By the way, Claude provided this disclaimer on that very first prompt. We provided the fact that we are beginners to AI in the initial prompt and immediately defined that ease of deployment would be important to us.

  

We can still ask how the hosting situation is in the Czech Republic (I get recommendations for Active 24, Wedos and Stable, all relevant) - but AI correctly reminds me that in this case I should be looking at a virtual private server, which is more expensive and already requires administration experience.

  

So, let's put the first indulgence to bed and figure out the next workflow to get everything set up:

  

> What would you recommend as a workflow for developing this app of mine? So I'm going to use python and Heroku, and my computer is running macOS.

Both CC and Claude give us pretty much the same advice (with varying degrees of detail) on how to proceed.  First, we should set up a local development environment, i.e. install Python, Flask and some source code editor - we are advised directly what and how. That's the reason we put in the prompts what operating system we will be working from. AI now directly offers us command-line commands or software suitable for that operating system (the answer this time is from Claude).

> To develop your application in Python with Heroku deployment and using
> macOS, I would recommend the following workflow:
>
> 1. Setting up the development environment:
> - Install Python (if you don't already have it): use Homebrew or download from python.org
> - Install Git for version control
> - Install a code editor (e.g. Visual Studio Code or PyCharm)
>
> 2. Create a project:
> - Create a new directory for the project
> - Initialize the Git repository: `git init`
> - Create a virtual environment: `python -m venv venv`
> - Activate the virtual environment: `source venv/bin/activate`
>
> 3. Flask application settings:
> - Install Flask: `pip install flask`
> - Create requirements: `pip freeze > requirements.txt`
> - Create the basic structure of the Flask application
>
> > 4. Development:
> - Work on the functionality incrementally
> - Use Git to save changes on an ongoing basis:
> ```
> git add .
> git commit -m "Description of changes"
> ```
> - Test locally: `flask run`
>
> 5. Deploy to Heroku:
> - Install Heroku CLI: `brew tap heroku/brew && brew install heroku`
> - Login to Heroku: `heroku login`
> - Create a Heroku application: `heroku create application-name`
> - Create a Procfile for Heroku
> - Deploy the application: `git push heroku main`
>
> 6. Continuous development and deployment:
> - Continue development locally.
> - Test changes
> - Commit changes to Git
> - Deploy to Heroku: `git push heroku main`
>
> > 7. Monitoring and debugging:
> - Monitor logs: `heroku logs --tail`.
> - Use Heroku dashboard for monitoring
>
> > I also recommend:
> - Use the `.gitignore` file to exclude unnecessary files from Git
> - Consider using automatic code formatting tools (e.g. Black)
> - Implement unit tests for key features
>
> > You want me to show you how to get started with this workflow by creating
> basic project structure?

  

If we don't understand something, we can ask the AI directly. For example:

  

> How do I install Git for version control on macOS?

  

And get the details I need.

  

After some time following the AI's instructions, we should be pretty well equipped. We have a local development environment, so we can develop and test the application right on our computer. We have a versioning system in place, so we have good control over how we build the code and can deploy it to "production" at the appropriate time - or send it to Heroku and make it visible to the world there.

  

Now we're clear on what we want and how we're going to proceed. At this point, the "context window" is important, i.e. the fact that modern LLM models keep long texts of the previous conversation in memory. Thanks to this, we can just give a simple prompt to the AI to generate the application as we have designed it:

  

> Create the source code for my app and describe in beginner's detail what to set up where and where to store it so that the code works when deployed.

The AI will now describe the file structure, i.e. where to store what, and then output the contents of those files. Now comes the tedious click-and-click moment where you have to use Copy&Paste to transfer the code (preferably via that installed development environment) to your computer and stack it where you have the project directory in GIT. And now comes the moment when you can test the application on your local machine. Only, how? Let's ask the AI:

  

> How do I test the app on my local machine running macOS?

Get a description of how to test the app in your environment and on your computer. It's very easy for the first run of an application to fail for some reason. In that case, an error message will appear on the console. Copy the message and prompt:

  

> I got this error message: and copy&paste the error text or log extract

The AI is quite flexible in this, you can copy a very long error log to it and it will figure it out. It will explain where the error occurred and suggest an adjustment you need to make.

  

Once you've debugged the app, deploy it to Heroku and test it again, there can be errors here too. Again, you consult the error log with the AI.

  

You can probably see where the main problem is. The constant copying of source code from the AI response to the development environment. Fortunately, most AIs will format the code nicely and offer you a button to easily transfer the text to a clipboard, but it's still a hassle. It would be better if the AI could directly link this output to Github or your GIT, but you can't do that yet, you have to save each file one by one.

  

> Tips:
> - Sometimes the AI will recommend you to make a specific fix in the code, for example just rewrite a piece of functionality. If you can find it in the code, do it, if not, tell it to give you the whole corrected code. Other times, you might be tempted to fix something in the code yourself, like text - in that case, tell the AI, because the next time it fixes the code, it wouldn't know about your edits.
> - If you don't understand something, have the AI explain it, ask.

  

As you can see, the procedure is not entirely suitable for large-scale application development.