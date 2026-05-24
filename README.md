# Langchain


for output parser 


      from langchain_core.prompts import ChatPromptTemplate
      from langchain_core.output_parsers import PydanticOutputParser
      from langchain_classic.output_parsers.fix import OutputFixingParser
      
      parser = PydanticOutputParser(pydantic_object=Plan)
      
      fixing_parser = OutputFixingParser.from_llm(
          parser=parser,
          llm=chat_model,
          max_retries=5
      )
      
      prompt = ChatPromptTemplate.from_messages([
          (
              "system",
              """
      You are a senior technical writer.
      
      Generate a technical blog plan.
      
      IMPORTANT:
      - Return ONLY valid JSON
      - Follow the schema exactly
      - Every task must contain:
        - id
        - title
        - goal
        - bullets
        - target_words
        - section_type
      """
          ),
          (
              "human",
              """
      Topic: {topic}
      
      {format_instructions}
      """
          )
      ])
      
      chain = (
          prompt.partial(
              format_instructions=parser.get_format_instructions()
          )
          | chat_model
          | fixing_parser
      )
