from crewai import Task

def research_task(agent, topic):
    return Task(
        description=f"Gather comprehensive insights, data points, and current trends about: {topic}.",
        expected_output="A clean list of raw facts, key insights, and context about the topic.",
        agent=agent
    )

def writing_task(agent, topic, content_type, tone, word_count, research_context):
    # Enforce strict visual formatting constraints depending on the dropdown selection
    layout_instructions = ""
    
    if content_type == "Blog Post":
        layout_instructions = "Include an engaging main H1 title, a hook introduction, subheadings (H2/H3) for distinct sections, conversational spacing, and a summary conclusion."
    
    elif content_type == "LinkedIn Post":
        layout_instructions = "Start with an attention-grabbing hook sentence. Use short, punchy paragraphs (1-2 sentences max), generous spacing/linebreaks, bullet points for key items, relevant emojis for visual breaks, and exactly 3-5 hashtags at the ultimate bottom. DO NOT use email introductions like 'Dear', 'Subject:', or formal letter sign-offs."
    
    elif content_type == "YouTube Script":
        layout_instructions = "Structure it explicitly as an interactive video production script. Use organizational markers like [Hook - 0:00], [Intro Scene], [Main Segment], and [Call to Action]. Write the actual spoken lines clearly under host speech blocks."
    
    elif content_type == "Instagram Caption":
        layout_instructions = "Keep it concise, punchy, and highly visual. Lead with a compelling first line to prevent truncation. Use contextual emojis throughout the text, a clear call to action, and place a block of tags at the bottom."
    
    elif content_type == "Email":
        layout_instructions = "Format it purely as an email. Provide a dedicated 'Subject:' line at the absolute top, followed by a personalized greeting, structured body paragraphs, and a formal closing remark signature block."

    return Task(
        description=f"""
        Using the provided research context, write a **{content_type}** about '{topic}'.
        
        CRITICAL OPERATIONAL RULES:
        1. **Tone**: You must write exclusively in a **{tone}** tone.
        2. **Length**: Target approximately **{word_count} words**.
        3. **Layout Restrictions**: Follow these strict layout rules: {layout_instructions}
        
        Do not add meta conversational notes like 'Here is your text' or wrap your response in conversational small talk. Output ONLY the raw finalized content.
        """,
        expected_output=f"A finalized {content_type} fully matching the layout specifications and the {tone} tone instruction.",
        agent=agent,
        context=[research_context]
    )