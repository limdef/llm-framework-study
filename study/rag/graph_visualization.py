import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib

# 폰트 설정 (이래도 한글이 깨짐)
font_path = '/System/Library/Fonts/Supplemental/AppleGothic.ttf'
font_prop = fm.FontProperties(fname=font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()
matplotlib.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 그래프 생성
G = nx.DiGraph()

triples = [
    ("전자기파", "사용", "통신"),
    ("전자기파", "기반", "광자"),
    ("광자", "형태", "빛"),
]

for s, r, o in triples:
    G.add_edge(s, o, label=r)

pos = nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G, 'label')

# 시각화
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=14)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, font_color='gray')
plt.title("📊 개념 그래프")
plt.show()
