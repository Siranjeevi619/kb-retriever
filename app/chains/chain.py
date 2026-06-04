from app.llm.llm import llm
from app.prompts.prompt import prompt

model = prompt | llm 
response = model.invoke({
    "user_query":"what is react ?"
})
print(response.content)