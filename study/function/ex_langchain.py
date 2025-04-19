from langchain.agents import initialize_agent, AgentType, Tool
from langchain.chat_models import ChatOpenAI
import os

# 환경 변수에서 API 키 설정
os.environ["OPENAI_API_KEY"] = ""

# 날씨 정보를 가져오는 함수
def get_weather(city: str) -> str:
    """도시의 현재 날씨 정보를 반환합니다."""
    # 실제 구현에서는 날씨 API를 호출할 수 있습니다
    return f"{city}의 현재 날씨: 맑음, 기온: 25°C"

# Tool 등록
tools = [
    Tool(
        name="get_weather",
        func=get_weather,
        description="도시 이름을 입력하면 현재 날씨를 알려줍니다. (예: get_weather(city='서울'))"
    )
]

# GPT 모델
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Agent 생성
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # tool 선택 + 사용 자동
    verbose=True
)

# 사용자 질문
result = agent.run("서울 날씨 알려줘")
print(result)
