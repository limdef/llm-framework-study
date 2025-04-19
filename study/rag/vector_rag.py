from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.settings import Settings

openai.api_key = os.getenv("OPENAI_API_KEY")

# 1. 모델 설정 (LLM + 임베딩)
Settings.llm = OpenAI(model="gpt-4")
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")  # 또는 "text-embedding-ada-002"

# 2. 문서 불러오기
documents = SimpleDirectoryReader("data").load_data()

# 3. 인덱스 생성
chroma_client = Client()
chroma_collection = chroma_client.create_collection("my_docs")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

index = VectorStoreIndex.from_documents(documents, vector_store=vector_store)

# 4. 쿼리 엔진 생성 및 질문
query_engine = index.as_query_engine()
response = query_engine.query("이 문서에서 중요한 내용이 뭐야?")
print(response)
