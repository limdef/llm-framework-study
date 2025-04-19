# LangChain

Function calling, Tool, Agent, LLM 을 포함해서 편하게 LLM 앱을 구현하도록 하는 프레임 워크

### 흐름 이해

1. 프롬프트 정의  

LLM이 도구를 사용할 수 있도록 형식을 명시적으로 지정

```
Question: 사용자의 질문
Thought: 어떤 도구를 써야 할지 생각
Action: 사용할 도구 이름
Action Input: 도구에 넘길 인자
Observation: (LangChain이 채움)
Final Answer: 최종 답변
```

2. 사용자가 질문 입력 시 LLM이 초기 출력 생성

```
Thought: 날씨를 확인해야겠다.
Action: get_weather
Action Input: "서울"
```

3. LangChain이 Action 실행
* Action 이름과 Action Input으로 함수 호출 후 호출 결과를 Observation으로 생성

4. 다시 LLM에 전달  
이전까지의 대화 + Observation: ... 까지 포함해서 다시 LLM에 입력

5. LLM이 다음 단계 판단  
Final Answer를 바로 낼 수도 있고, 다른 도구를 또 쓸 수도 있음  
-> 반복 수행

6. Final Answer가 생성되면 응답 종료 



** 위 과정을 프레임워크로 만들어 놓은게 LangChain  
