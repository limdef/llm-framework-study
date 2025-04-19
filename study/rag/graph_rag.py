import openai
from neo4j import GraphDatabase
import os

# OpenAI API 키 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

# 문서 예시
DOCUMENTS = {
    "doc_1": "Electromagnetic waves are used in communication systems.",
    "doc_2": "Photons are a form of light.",
    "doc_3": "Electromagnetic waves are based on photons.",
}

# LLM을 이용한 triple 추출 함수
def extract_triples_llm(text):
    prompt = f"""
You are an information extraction system. Extract subject-relation-object triples from the sentence below.
Respond in JSON format like: [{{"subject": "...", "relation": "...", "object": "..."}}]

Sentence: "{text}"
"""
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
        temperature=0,
    )
    try:
        result = eval(response.choices[0].message.content)
        triples = [(t["subject"], t["relation"], t["object"], text) for t in result]
        return triples
    except Exception as e:
        print("Parsing error:", e)
        return []

# Neo4j 연결 / Neo4j를 띄어야 함
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "your_password"))

# Triple 저장 함수
def store_triple(tx, s, r, o, doc_id, sentence):
    tx.run("""
    MERGE (a:Concept {name: $s})
    MERGE (b:Concept {name: $o})
    MERGE (a)-[rel:RELATION {type: $r}]->(b)
    SET rel.doc_id = $doc_id,
        rel.snippet = $sentence
    """, s=s, r=r, o=o, doc_id=doc_id, sentence=sentence)

# Neo4j 연결 및 트리플 저장
with driver.session() as session:
    for doc_id, text in DOCUMENTS.items():
        triples = extract_triples_llm(text)
        for s, r, o, sentence in triples:
            print(f"[{doc_id}] {s} -{r}-> {o} / \"{sentence}\"")
            session.write_transaction(store_triple, s, r, o, doc_id, sentence) # sentence == 원본 문서
