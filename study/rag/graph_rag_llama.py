from llama_index.graph_stores import Neo4jGraphStore
from llama_index.indices.knowledge_graph import KGIndex
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms import OpenAI

# Neo4j 설정
graph_store = Neo4jGraphStore(
    username="neo4j",
    password="your_password",
    url="bolt://localhost:7687",
)

# LlamaIndex에 연동된 Graph 객체 생성 / Graph가 이미 구축되어 있어야 함
kg_index = KGIndex.from_graph_store(graph_store=graph_store)

# 사용자 질문
query = "전자기파는 어디에 사용되나요?"

# LLM 설정
llm = OpenAI(model="gpt-4o-mini")

# 질의 → 그래프 기반으로 관련 노드와 경로 검색
response = kg_index.query(query, llm=llm)

print(response)
