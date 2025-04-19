# function call

1. LLM이 함수 사용 필요성 판단
> LLM이 사용자 질문을 보고
"이건 내가 가진 툴 중 하나를 써야겠는데?"
라고 판단하면…

* 미리 프롬프팅이 되어 있어야 함.

2. 지정된 포맷으로 응답

```
{
  "function_call": {
    "name": "get_weather",
    "arguments": "{ \"city\": \"서울\" }"
  }
}
```

3. 함수 매핑 & 실행

```
func_map = {
    "get_weather": get_weather
}

# 함수 이름에 맞는 실제 Python 함수 찾아서 실행
result = func_map["get_weather"](**{"city": "서울"})
```

4. 결과를 LLM에게 전달하거나 최종 응답으로 반환

- 단순 function call 구조라면 → 사용자에게 바로 결과 반환
- 멀티턴 구조면 → 함수 결과를 다시 LLM에게 전달하여 자연스러운 문장으로 구성된 응답 생성
