def config_prompts(prompt_id, data):
    configPrompts = {
        "extract_relevant_info" : f"""
            You are a product research AI.
            Your task:
            Extract ONLY important product-related information useful for ecommerce marketing.
            REMOVE:
            - navigation text
            - footer text
            - cookies/privacy
            - duplicate text
            - generic company statements
            KEEP:
            - product features
            - customer pain points
            - benefits
            - differentiators
            - pricing info
            - target users
            - AI features
            - workflow features
            Return ONLY valid JSON.
            Format:
            {{
              "relevant_information": [
                "...",
                "...",
                "..."
              ]
            }}
            Webpage Content:
            {data}
        """,
        "generate_market_research_info": f"""
            You are an expert ecommerce market research AI.
            Your task is to analyze product information and generate structured marketing insights.
            RULES:
            - Return ONLY valid JSON
            - Do not explain anything
            - Do not add markdown
            - Keep hooks under 12 words
            - Emotional triggers should be concise
            - Target audience should be specific
            Required JSON format:
            {{
              "marketing_hooks": [
                "...",
                "...",
                "..."
              ],
              "emotional_triggers": [
                "...",
                "...",
                "..."
              ],
              "target_audience": [
                "...",
                "...",
                "..."
              ]
            }}
            Product Information:
            {data}
        """,
        "generate_creative_strategy_prompts": f"""
            You are an expert AI Creative Director for ecommerce advertising.
            Your task is to generate 5 high-quality AI image generation prompts for product marketing creatives.
            OBJECTIVE:
            Create visually compelling, cinematic, high-converting advertisement concepts suitable for social media marketing campaigns.
            INSTRUCTIONS:
            - Use the provided marketing hooks, emotional triggers, target audience, visual themes, and ad angles
            - Generate prompts optimized for AI image generation models like FLUX, SDXL, Midjourney, and Stable Diffusion
            - Focus on commercial-quality advertising visuals
            - Create realistic and emotionally engaging scenes
            - Each prompt should represent a unique creative direction
            - Include:
                - environment
                - subject actions
                - emotional tone
                - lighting
                - camera/composition style
                - branding aesthetic
                - product interaction
            - Use modern social media ad aesthetics
            - Make prompts highly descriptive but concise
            - Avoid generic wording
            - Avoid repetition
            IMAGE STYLE REQUIREMENTS:
            - Cinematic lighting
            - Commercial photography
            - Ultra realistic
            - High detail
            - Premium brand aesthetic
            - Social media ad style
            - Professional composition
            RETURN FORMAT:
            Return ONLY valid JSON.
            {{
              "image_prompts": [
                "...",
                "...",
                "...",
                "...",
                "..."
              ]
            }}
            MARKETING STRATEGY DATA:
            {data}
        """,
        "critic_agent_prompt": f"""
            You are an expert AI advertisement critic.
            Your task:
            Evaluate the quality of an AI-generated advertisement prompt.
            Evaluate:
            - advertisement quality
            - branding clarity
            - product visibility
            - emotional marketing
            - commercial appeal
            - uniqueness
            Return ONLY valid JSON.
            Format:
            {{
              "score": 0-10,
              "strengths": [
                "...",
                "..."
              ],
              "issues": [
                "...",
                "..."
              ],
              "improvements": [
                "...",
                "..."
              ]
            }}
            PROMPT:
            {data}
        """,
        "script_generation_agent_prompt": f"""
            You are an expert Direct Response Marketing Copywriter and Video Advertisement Strategist.
            Your task is to create a short-form video advertisement script for social media platforms such as TikTok, Instagram Reels, YouTube Shorts, and Facebook Ads.
            OBJECTIVE:
            Create a high-converting advertisement storyboard designed to maximize:
            - Attention
            - Curiosity
            - Emotional engagement
            - Product understanding
            - Conversion
            INPUT:
            Marketing research data including:
            - Marketing hooks
            - Emotional triggers
            - Target audience
            - Product features
            - Product benefits
            INSTRUCTIONS:
            Generate exactly 5 scenes.
            Scene Structure:
            1. Hook
               - Capture attention within 3 seconds.
               - Create curiosity or identify a pain point.
            2. Problem
               - Highlight the customer's frustration or challenge.
            3. Solution
               - Introduce the product as the solution.
            4. Benefits
               - Showcase the strongest product benefit or transformation.
            5. Call To Action
               - Encourage the viewer to take action.
            For each scene generate:
            - scene_number
            - scene_type
            - visual_description
            - on_screen_text
            - voiceover
            - emotion
            - duration_seconds
            RULES:
            - Voiceover must sound natural and conversational.
            - On-screen text must be short and punchy.
            - Hook must be under 10 words.
            - CTA must be action-oriented.
            - Visual descriptions should be suitable for AI image generation.
            - Each scene should flow naturally into the next.
            - Focus on selling outcomes, not features.
            - Use emotional marketing principles.
            - Optimize for social media advertisement performance.
            RETURN ONLY VALID JSON.
            Format:
            {{
              "ad_title": "",
              "target_audience": "",
              "total_duration": 25,
              "scenes": [
                {{
                  "scene_number": 1,
                  "scene_type": "hook",
                  "visual_description": "",
                  "on_screen_text": "",
                  "voiceover": "",
                  "emotion": "",
                  "duration_seconds": 5
                }},
                {{
                  "scene_number": 2,
                  "scene_type": "problem",
                  "visual_description": "",
                  "on_screen_text": "",
                  "voiceover": "",
                  "emotion": "",
                  "duration_seconds": 5
                }},
                {{
                  "scene_number": 3,
                  "scene_type": "solution",
                  "visual_description": "",
                  "on_screen_text": "",
                  "voiceover": "",
                  "emotion": "",
                  "duration_seconds": 5
                }},
                {{
                  "scene_number": 4,
                  "scene_type": "benefits",
                  "visual_description": "",
                  "on_screen_text": "",
                  "voiceover": "",
                  "emotion": "",
                  "duration_seconds": 5
                }},
                {{
                  "scene_number": 5,
                  "scene_type": "cta",
                  "visual_description": "",
                  "on_screen_text": "",
                  "voiceover": "",
                  "emotion": "",
                  "duration_seconds": 5
                }}
              ]
            }}
            MARKETING DATA:
            {data}
        """
    }
    return configPrompts[prompt_id]
    
def return_model_info(modelInfo,data):
    configModels = {
        "payload_extract_relevant_info" : {
            "model": "qwen2.5:1.5b",
            "prompt": config_prompts("extract_relevant_info",data),
            "stream": False,
            "format": "json",
            "options": {
                "temperature": 0.1,
                "num_predict": 1000
            }
        },
        "payload_marketing_hooks" : {
            "model": "qwen2.5:1.5b",
            "prompt": config_prompts("generate_market_research_info",data),
            "stream": False,
            "format": "json",
            "options": {
                "temperature": 0.1,
                "num_predict": 1000
            }
        },
        "payload_strategy_prompt" : {
            "model": "qwen2.5:1.5b",
            "prompt": config_prompts("generate_creative_strategy_prompts",data),
            "stream": False,
            "format": "json",
            "options": {
                "temperature": 0.1,
                "num_predict": 1000
            }
        },
        "script_writer_prompt" : {
            "model": "qwen2.5:1.5b",
            "prompt": config_prompts("script_generation_agent_prompt",data),
            "stream": False,
            "format": "json",
            "options": {
                "temperature": 0.1,
                "num_predict": 1000
            }
        }
    }
    return configModels[modelInfo]