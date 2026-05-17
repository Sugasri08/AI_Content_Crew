from crewai import Task
 

def research_task(agent, topic):
    return Task(
        description=f"Gather comprehensive insights, data points, and context about: {topic}.",
        expected_output="A bulleted list of research insights, current trends, and structural details.",
        agent=agent
    )

def writing_task(agent, topic, content_type, tone, word_count, research_context):
    # 🌟 CRITICAL FIX: Explicitly instruct the model how to layout different types
    layout_instructions = ""
    if content_type == "Blog Post":
        layout_instructions = "Include an engaging H1 title, conversational introduction, subheadings (H2/H3), and a conclusion."
    elif content_type == "LinkedIn Post":
        layout_instructions = "Start with a strong hook sentence, use short single-sentence paragraphs, linebreaks for readability, bullet points, and add 3-5 relevant hashtags at the bottom. DO NOT use email greetings like 'Dear' or subject lines."
    elif content_type == "YouTube Script":
        layout_instructions = "Structure it cleanly as an audio/visual script. Include clear indicators like [Hook], [Intro Graphic], [Main Segment], [Call to Action], and explicit host dialogue."
    elif content_type == "Instagram Caption":
        layout_instructions = "Keep it concise, high-energy, leading with the main value proposition, heavily interspersed with contextual emojis, followed by a block of hashtags."
    elif content_type == "Email":
        layout_instructions = "Structure it precisely as a professional email with a clear 'Subject:' line, an appropriate greeting, a clean body, and a sign-off footer."

    return Task(
        description=f"""
        Using the provided research, write a **{content_type}** about '{topic}'.
        
        CRITICAL REQUIREMENTS:
        1. **Tone**: The entire text must be written in a strict **{tone}** tone.
        2. **Length**: Target roughly **{word_count} words**.
        3. **Layout Guidelines**: {layout_instructions}
        
        Ensure you only output the generated content itself. Do not write introductory meta-text like 'Here is your post:' or conversational replies.
        """,
        expected_output=f"A fully finished and formatted {content_type} adhering exactly to the specified layout guidelines.",
        agent=agent,
        context=[research_context]
    )