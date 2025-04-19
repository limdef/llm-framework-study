import openai
from typing import List, Dict, Any, Callable
import json

# 함수 정의
def get_weather(location: str) -> Dict[str, Any]:
    """지정된 위치의 날씨 정보를 반환합니다."""
    # 실제 구현에서는 날씨 API를 호출할 수 있습니다
    return {
        "location": location,
        "temperature": 25,
        "condition": "맑음",
        "humidity": 60
    }

def get_stock_price(symbol: str) -> Dict[str, Any]:
    """주식 심볼의 현재 가격을 반환합니다."""
    # 실제 구현에서는 주식 API를 호출할 수 있습니다
    return {
        "symbol": symbol,
        "price": 150.75,
        "change": 2.5
    }

# 함수 매핑 정의
FUNCTION_MAP: Dict[str, Callable] = {
    "get_weather": get_weather,
    "get_stock_price": get_stock_price
}

def process_function_call(function_name: str, arguments: Dict[str, Any]) -> Any:
    """함수 호출을 처리합니다."""
    if function_name not in FUNCTION_MAP:
        raise ValueError(f"Unknown function: {function_name}")
    
    return FUNCTION_MAP[function_name](**arguments)

# 예시: LLM과의 대화 시뮬레이션
def simulate_conversation():
    # 사용자 메시지
    user_message = "서울의 날씨와 애플 주식 가격을 알려줘"
    
    # LLM 응답 (실제로는 OpenAI API를 호출)
    response = {
        "role": "assistant",
        "content": None,
        "function_calls": [
            {
                "name": "get_weather",
                "arguments": {"location": "서울"}
            },
            {
                "name": "get_stock_price",
                "arguments": {"symbol": "AAPL"}
            }
        ]
    }
    
    # 함수 호출 처리
    results = []
    for function_call in response["function_calls"]:
        result = process_function_call(
            function_call["name"],
            json.loads(function_call["arguments"])
        )
        results.append(result)
    
    # 결과 출력
    print("날씨 정보:", results[0])
    print("주식 정보:", results[1])

if __name__ == "__main__":
    simulate_conversation()
