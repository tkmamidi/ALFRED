import autogen
from autogen.agentchat.contrib.agent_builder import AgentBuilder

config_path = "configs/config_list.json"
default_llm_config = {"temparaure": 0, "timeout": 500}

builder = AgentBuilder(config_path=config_path)

building_task = (
    "Find a paper on arxiv by programming, and analyze its application in some domain."
)

agent_list, agent_configs = builder.build(building_task, default_llm_config)


def start_task(execution_task: str, agent_list: list, llm_config: dict):
    config_list = autogen.config_list_from_json(config_path)

    group_chat = autogen.GroupChat(agents=agent_list, messages=[], max_round=12)
    manager = autogen.GroupChatManager(
        groupchat=group_chat, llm_config={"config_list": config_list, **llm_config}
    )
    agent_list[0].initiate_chat(manager, message=execution_task)


start_task(
    execution_task="Find a recent paper about gpt-4 on arxiv and find its potential applications in software.",
    agent_list=agent_list,
    llm_config=default_llm_config,
)

# config_list = [{"model": "open_ai",
#         "api_type": "open_ai",
#         "api_key": "openai_api",
#         "api_base": "https://api.openai.com/v1/engines/davinci-codex/completions",}]

# llm_config_assistant = {
#     "Seed" : 42,
#     "temperature": 0,
#         "functions": [
#         {
#             "name": "answer_PDF_question",
#             "description": "Answer any PDF related questions",
#             "parameters": {
#                 "type": "object",
#                 "properties": {
#                     "question": {
#                         "type": "string",
#                         "description": "The question to ask in relation to PDF",
#                     }
#                 },
#                 "required": ["question"],
#             },

#         }
#     ],
#     "config_list": config_list,
#     "timeout": 120,
# }

# assistant = autogen.AssistantAgent(
#             name="assistant",
#             llm_config=llm_config_assistant,
#             system_message="""You are a helpful assistant, Answer the question based on the context.
#                               Keep the answer accurate. Respond "Unsure about answer" if not sure about the answer."""

#         )

# user_proxy = autogen.UserProxyAgent(
#             name="user_proxy",
#             human_input_mode="NEVER",
#             max_consecutive_auto_reply=10,
#             code_execution_config={"work_dir": "work_dir"},
#             system_message="""Reply "Unsure about answer" if not sure about the answer.""",

#             # llm_config_assistant = llm_config_assistant,
#             # function_map={
#             #     "answer_PDF_question": answer_PDF_question
#             # }
#         )

# user_proxy.initiate_chat(
#     assistant,
#     message="""
# Write a Openchat word blog post titled why openchat better than GPT3 that uses the exact keyword OpenChat
# at least once every 100 words. The blog post should include an introduction, main body,
#  and conclusion. The conclusion should invite readers to leave a comment. The main
#  body should be split into at least 4 different subsections.
# """
# )

# coder = Ollama(model="codellama", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))


# llm_config={
#     "timeout": 600,
#     "cache_seed": 42,
#     "config_list": config_list,
#     "temperature": 0,
# }

# # create an AssistantAgent instance named "assistant"
# assistant = autogen.AssistantAgent(
#     name="assistant",
#     llm_config=llm_config,
# )

# user_proxy = autogen.UserProxyAgent(
#     name="user_proxy",
#     human_input_mode="TERMINATE",
#     max_consecutive_auto_reply=10,
#     is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
#     code_execution_config={"work_dir": "web"},
#     llm_config=llm_config_mistral,
#     system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
# Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
# )
