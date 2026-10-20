#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
===============================================================================
재난관리연구방법론 Chapter 2: 사회적 네트워크 구조 (Social Network Structure)
파이썬 서브노트 & 자가진단 퀴즈 애플리케이션 (Standard Library Only)
===============================================================================
"""

import sys
import os
import json
import argparse
import webbrowser
import http.server
import socketserver

# Chapter 2 Subnote Structured Knowledge Base
SUBNOTE_DATA = {
    "title": "재난관리연구방법론 Chapter 2: 사회적 네트워크 구조",
    "pages": "17 ~ 21 쪽",
    "original_title": "Social Network Structure: Moving Beyond Social Capital and Communitas",
    "sections": [
        {
            "id": 1,
            "title": "제1절. 네트워크 밀도(Density)와 코뮤니타스의 한계",
            "page": "17쪽",
            "content": """
[1. 밀도(Density)의 정의 및 수식]
- 개념: 네트워크 내 알터(Alters) 사이에 실제로 존재하는 연결 수를 이론적으로 가능한 최대 연결 수로 나눈 비율.
- 수식 (무방향 자아중심 기준): Density = 2L / [N * (N - 1)] (N: 알터 수, L: 실제 연결선 수)
- 의미: 밀도가 1.0(100%)에 가까울수록 전원이 서로를 아는 조밀한(Close-knit) 상태.

[2. 위험 완화를 위한 의도적 구축]
- 네트워크 밀도는 자연발생적 결과가 아니며, 개인이 위험 완화(Risk Mitigation)를 위해 의식적으로 확장함.
- 사례: 케냐 서부 포코트(Pokot)족 목축민들이 가뭄 시 식량 지원망 확보를 위해 평소 가축을 선물하여 밀도를 높임.

[3. 체르네아(Michael Cernea)의 '사회적 단절(Social Disarticulation)' 방지 노력]
- 강제 이주 및 재정착 시 사회적 자본과 상호부조 망이 깨지는 '사회적 단절' 위험을 피하기 위해 고밀도 비공식 연대를 유지하려 노력함.
- 그러나 자원이 결핍된 상태에서의 고밀도 유대는 '밀도의 역설'로 직결됨.

[4. 지원 성격의 분리 (Hurlbert et al., 2001)]
- 고밀도·소규모 망: 비공식 사회 지원(감정 위로, 돌봄, 친밀 나눔) 우세.
- 저밀도·대규모 망: 공식 제도 지원(외부 공공기관, 구호단체) 더 많이 활용.
- 외부 단절 문제: 고밀도 망에 깊이 매몰(Embedded)될수록 외부 공식 지원 접근성은 가장 저하됨.

[5. 밀도의 역설 (Paradox of Density)과 정신건강 악화]
- 통념 파괴: 끈끈한 고밀도 망이 웰빙을 증진시킨다는 통념을 뒤엎고, 멕시코 이주지 연구 등에서 고밀도 망 보유 집단이 가장 최악의 웰빙(정신건강 악화)을 기록함.
- 3대 원인: 1) 만성 자원 결핍, 2) 과도한 부양 의무, 3) 관계적 번아웃(Burnout).
            """
        },
        {
            "id": 2,
            "title": "제2절. 구조적 다양성과 하위 집단 (Structural Diversity & Subgroups)",
            "page": "18쪽",
            "content": """
[1. 도입 배경]
- 단순 유대 수(규모)나 밀도에만 매몰되지 않고 가교(Bridging), 중심성(Centrality), 중앙화, 하위집단(Subgroups) 등 위상 구조를 종합 분석.

[2. 가교(Bridging)와 중개자(Brokers)]
- 서로 연결되지 않은 집단을 이어주는 가교 행위자는 비중복적 자원과 정보를 유입시키는 핵심 통로임.

[3. 4가지 네트워크 유형론]
- 밀집형(dense), 확장형(extending), 하위집단형(subgroups), 희소형(sparse).
- 맥락 의존성: 국가, 재정착 여부, 피해 심각도에 따라 동일 구조라도 위험 인식 및 젠더별 정신건강 영향이 다름.

[4. 응집력 있는 하위 집단(Subgroups/Cliques)의 역설]
- 이론적 기대와 달리 하위 집단 존재와 실제 사회적 지원 교환 간 상관관계가 없었음.
- 오히려 하위 집단을 가진 재정착 여성은 전반적 정신건강 점수 최악, 남성은 우울 점수 최고치를 기록.

[5. 대표 실증 사례: 멕시코 ABC 어린이집 참사 유가족 파벌 분열 (Jones & Murphy, 2015)]
- 1년 차: 사망 아동 부모 vs 부상 아동 부모로 2개 집단 분열.
- 2년 차: 각각 정치적·사법적 강경파 vs 온건 비정치파로 재분화되어 총 4개 하위 파벌로 파편화됨.
            """
        },
        {
            "id": 3,
            "title": "제3절. 표면 구조와 심층 구조 (Surface Structure vs Deep Structure)",
            "page": "19쪽",
            "content": """
[1. 개념적 기원]
- 소쉬르, 촘스키, 레비-스트로스의 구조주의 사상에 기원. Hoffman은 재난 문화를 두 층위로 구분.
- 심층 구조 (Deep Structure): 보이지 않는 무의식적 기틀 및 문법 (Grammar).
- 표면 구조 (Surface Structure): 재난 시 개인이 의식적으로 동원하는 행동 및 관습 패턴.

[2. 조작화 및 데이터 추출 방식]
- 심층 구조: '무맥락 이름 생성기 (Context-free Name Generator)'로 측정.
- 표면 구조: '맥락 특화 질문 (Context-specific Questions)'으로 측정.

[3. 실증 분석 결과 (460개 표본 분석)]
- 표면 구조: 연구 전반에 걸쳐 높은 일관성과 재현성을 보임.
- 심층 구조: 심층 구조 지표와 재난 복구 결과(웰빙, 위험 인식) 간 관계는 비일관적이며 변동이 심함.

[4. 핵심 결론: 문법적 결정론의 한계]
- 심층 구조는 인간의 행동을 기계적으로 규정하는 문법이 아니며, 역사적 상호작용, 제도의 매개, 문화적 레퍼토리 속에서 동적으로 발현됨.
            """
        },
        {
            "id": 4,
            "title": "제4절. 재난의 각 단계에 걸친 네트워크 내의 개인 (Individuals in Disaster Phases)",
            "page": "20쪽",
            "content": """
[1. 앤서니 월리스 (Anthony Wallace, 1956)의 시공간 및 심리 모형]
- 8단계 시간 체계: 1.재난 전(Steady State) -> 2.경보(Warning) -> 3.위협(Threat) -> 4.영향(Impact) -> 5.격리(Isolation) -> 6.구조(Rescue) -> 7.구제(Remedy) -> 8.복구(Recovery)
- 3대 휴리스틱 공간 체계: 
  1) 충격 지역 (Impact Area): 직접적 파괴 지대
  2) 인접/필터 지역 (Filter Area): 구호 물자 및 정보 흐름 필터링·매개 지대
  3) 조직화된 지원 지역 (Organized Help Area): 외부 전문 구호자원 배후지
- 재난 증후군 (Disaster Syndrome): 충격 직후 겪는 멍함, 방향감각 상실, 수동성 등 심리적 반응 체계.

[2. 수잔나 호프만 (Hoffman, 1999)의 3단계 주기 모델]
- 1단계: 개인 -> 집단 지원 (이타주의 파도)
- 2단계: 집단 지원 -> 파벌 경쟁 (자원 분배 갈등 & Oliver-Smith의 사회적 균열 재점화)
- 3단계: 종결 (Closure, 각 가계 일상 복귀)

[3. 지원 고갈과 사회적 매몰성의 역설 (Weil et al., 2012 / 카트리나)]
- 단기적: 유대가 깊을수록 타인 부양 부담으로 초기 스트레스 가중.
- 장기적: 풍부한 관계 자원 덕분에 복구 회복 속도가 훨씬 빠름.

[4. 사회적 시간과 Vital Phase (Casagrande et al., 2015 / 미시시피강 홍수)]
- 생사 결정 단계 (Vital Phase): 신체 생존 직결 시점에서는 친족(Kin 유대) 지원이 100% 독점.
- 비치명적 & 장기 복구 단계: 공식/제도적 지원이 지배적.
            """
        },
        {
            "id": 5,
            "title": "제5절. 종합 비판: 사회적 자본과 코뮤니타스를 넘어 (Beyond Communitas)",
            "page": "21쪽",
            "content": """
[1. 체르네아의 사회적 단절 극복 시도의 이면]
- 사회적 단절(Social Disarticulation)을 예방하려 고밀도망을 유지하지만 자원 결핍 시 밀도의 역설로 직결됨.

[2. 기존 문화적 위계의 재의인화 (Reifying Inequalities)]
- 강한 연대(Communitas) 강조가 기존 인종, 계급, 성별 위계를 비판 없이 답습하고 고착화할 위험.

[3. 수혜 자격의 정치 (Politics of Deservingness)와 취약층 배제 (Faas, 2015a)]
- 에콰도르 재정착지에서 전통 품앗이 '밍가(Minga)' 참여를 주택 지원 조건으로 강제하자, 생계형 임금 노동을 해야 했던 가난한 취약 가구가 배제됨.

[4. 구조적 권력 독점]
- 여성이 가교(Bridging) 역할을 수행하더라도 권력과 위상은 남성이 독점하는 젠더 불평등 포착 필요.
            """
        }
    ],
    "scholars": [
        {"name": "Anthony Wallace", "year": "1956", "page": "20-21p", "topic": "8단계 시간 체계, 3대 휴리스틱 공간 영역(충격/필터/도움), 재난 증후군"},
        {"name": "Michael Cernea", "year": "1997", "page": "18p", "topic": "강제 이주 및 재정착 시 사회적 단절 (Social Disarticulation) 위험 지적"},
        {"name": "Hurlbert et al.", "year": "2001", "page": "17p", "topic": "고밀도망(비공식 지원) vs 저밀도망(공식 제도 지원) 지원 성격 분리"},
        {"name": "Susanna Hoffman", "year": "1999", "page": "19-20p", "topic": "재난 문화 표면/심층 구조, 개인 지원 -> 파벌 경쟁 -> 종결 3단계 모델"},
        {"name": "Jones & Murphy", "year": "2015", "page": "18-19p", "topic": "하위 집단 파편화 및 멕시코 ABC 어린이집 참사 유가족 4개 파벌 분열 규명"},
        {"name": "Casagrande et al.", "year": "2015", "page": "21p", "topic": "사회적 시간 정립, 생사 결정 단계(Vital Phase) 친족(Kin) 지원 독점 입증"},
        {"name": "Weil et al.", "year": "2012", "page": "21p", "topic": "사회적 매몰성의 역설 (초기 스트레스 가중 vs 장기 회복 속도 촉진)"},
        {"name": "A. J. Faas", "year": "2015a", "page": "17-18p", "topic": "수혜 자격의 정치 (Politics of Deservingness) 및 에콰도르 밍가 사례"}
    ],
    "quizzes": [
        {
            "id": 1,
            "question": "앤서니 월리스(Anthony Wallace, 1956)가 제시한 공간 영역 중 구호 물자 및 정보를 선별·전달하는 매개 지대는?",
            "options": ["1) 충격 지역 (Impact Area)", "2) 인접 / 필터 지역 (Filter Area)", "3) 조직화된 지원 지역 (Organized Help Area)", "4) 격리 지역 (Isolation Area)"],
            "answer": 2,
            "explanation": "Wallace의 모형에서 Filter Area는 직접 피해 지대 주변에서 정보와 물자 흐름을 선별·매개하는 영역입니다."
        },
        {
            "id": 2,
            "question": "마이클 체르네아(Michael Cernea)가 강제 이주 및 재정착 시 기존 사회적 자본과 상호부조 망이 해체되는 위험을 일컬은 용어는?",
            "options": ["1) 수혜 자격의 정치", "2) 사회적 단절 (Social Disarticulation)", "3) 밀도의 역설", "4) 재난 증후군"],
            "answer": 2,
            "explanation": "Cernea는 이주로 공동체 유대망이 깨지는 현상을 'Social Disarticulation(사회적 단절)'로 지목했습니다."
        },
        {
            "id": 3,
            "question": "재난 발생 직후 신체 생존과 안전 확보가 직결된 Vital Phase(생사 결정 단계)에서 지원을 거의 독점하는 유대는?",
            "options": ["1) 이웃 유대", "2) 친족 (Kin) 유대", "3) 공무원 및 소방관 유대", "4) NGO 자원봉사자 유대"],
            "answer": 2,
            "explanation": "Casagrande et al.(2015)에 따르면, 생존 직결 단계에서는 친족 유대가 다른 모든 원천을 독점합니다."
        },
        {
            "id": 4,
            "question": "네트워크 '밀도의 역설 (Paradox of Density)'에 관한 설명으로 옳은 것은?",
            "options": [
                "1) 네트워크가 조밀할수록 외부 공공 지원 수혜량이 증가한다.",
                "2) 네트워크가 조밀할수록 자원 부족과 과도한 부양 부담으로 정신건강이 최악으로 악화될 수 있다.",
                "3) 밀도가 높은 네트워크는 우울 증상을 완벽하게 차단한다.",
                "4) 밀도는 개인의 의식적 노력으로 절대로 확대될 수 없다."
            ],
            "answer": 2,
            "explanation": "밀도가 높은 결속망은 만성 자원 결핍과 부양 중압감, 감정적 번아웃으로 웰빙 악화를 유발합니다."
        }
    ]
}


def safe_input(prompt=""):
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        print("\n입력이 종료되었습니다.")
        return ""


def print_header(title):
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def display_sections_menu():
    print_header("📚 챕터 2 섹션별 서브노트 읽기")
    for sec in SUBNOTE_DATA["sections"]:
        print(f" [{sec['id']}] {sec['title']} ({sec['page']})")
    print(" [0] 메인 메뉴로 돌아가기")
    
    choice = safe_input("\n읽으실 섹션 번호를 입력하세요: ").strip()
    if choice == '0' or not choice:
        return
    
    for sec in SUBNOTE_DATA["sections"]:
        if str(sec["id"]) == choice:
            print_header(f"{sec['title']} ({sec['page']})")
            print(sec["content"].strip())
            safe_input("\n[Enter 키를 누르면 이전 메뉴로 돌아갑니다...]")
            return display_sections_menu()
    
    print("\n⚠️ 올바른 번호를 입력해 주세요.")
    display_sections_menu()


def search_subnote():
    print_header("🔍 키워드 및 학자 검색")
    query = safe_input("검색할 단어(예: Cernea, Wallace, 밀도, Vital Phase): ").strip().lower()
    
    if not query:
        return

    found = False
    print("\n--- [검색 결과] ---")
    
    # Search in scholars
    for sch in SUBNOTE_DATA["scholars"]:
        if query in sch["name"].lower() or query in sch["topic"].lower():
            print(f"🎓 [학자] {sch['name']} ({sch['year']}, {sch['page']}): {sch['topic']}")
            found = True

    # Search in sections
    for sec in SUBNOTE_DATA["sections"]:
        if query in sec["title"].lower() or query in sec["content"].lower():
            print(f"\n📖 [섹션 {sec['id']}] {sec['title']}")
            lines = sec["content"].strip().split("\n")
            matching_lines = [line for line in lines if query in line.lower()]
            for line in matching_lines[:5]:
                print(f"   - {line.strip()}")
            found = True

    if not found:
        print("❌ 일치하는 결과를 찾지 못했습니다.")
    
    safe_input("\n[Enter 키를 누르면 메인 메뉴로 돌아갑니다...]")


def run_quiz():
    print_header("📝 자가진단 퀴즈 (Interactive CLI Quiz)")
    score = 0
    total = len(SUBNOTE_DATA["quizzes"])

    for q in SUBNOTE_DATA["quizzes"]:
        print(f"\nQ{q['id']}. {q['question']}")
        for opt in q["options"]:
            print(f"   {opt}")
        
        user_in = safe_input("\n정답 번호를 선택하세요 (1-4): ").strip()
        try:
            ans = int(user_in)
            if ans == q["answer"]:
                print("✅ 정답입니다!")
                score += 1
            else:
                print(f"❌ 오답입니다. (정답: {q['answer']}번)")
            print(f"💡 해설: {q['explanation']}")
        except ValueError:
            print("⚠️ 숫자로 입력하지 않아 오답 처리되었습니다.")
        
        print("-" * 50)

    print(f"\n🎉 퀴즈 종료! 최종 점수: {score} / {total}점 (맞춘 비율: {int(score/total*100)}%)")
    safe_input("\n[Enter 키를 누르면 메인 메뉴로 돌아갑니다...]")


def open_web_subnote():
    print_header("🌐 웹 브라우저에서 서브노트 열기")
    project_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(project_dir, "index.html")

    if os.path.exists(html_file):
        url = f"file://{html_file}"
        print(f"🚀 브라우저를 실행합니다: {url}")
        webbrowser.open(url)
    else:
        print("❌ index.html 파일을 찾을 수 없습니다.")
    
    safe_input("\n[Enter 키를 누르면 메인 메뉴로 돌아갑니다...]")


def start_local_server(port=8080):
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)
    handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            print_header(f"🌐 로컬 웹 서버 실행 중: http://localhost:{port}")
            print(f"웹 브라우저에서 http://localhost:{port} 주소로 접속 가능합니다.")
            print("서버를 종료하려면 Ctrl + C 를 누르세요.")
            webbrowser.open(f"http://localhost:{port}")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 웹 서버가 종료되었습니다.")
    except Exception as e:
        print(f"\n❌ 서버 실행 중 오류 발생: {e}")


def main_menu():
    while True:
        print_header("📘 재난관리연구방법론 Chapter 2 파이썬 서브노트")
        print(" [1] 📚 챕터 2 섹션별 본문 읽기")
        print(" [2] 🔍 키워드 및 학자 검색 (Cernea, Wallace 등)")
        print(" [3] 📝 자가진단 퀴즈 풀기")
        print(" [4] 🌐 웹 브라우저에서 인터랙티브 HTML 서브노트 열기")
        print(" [5] 🖥️ 로컬 웹 서버 구동하기 (http://localhost:8080)")
        print(" [0] 👋 프로그램 종료")
        
        choice = safe_input("\n메뉴 선택: ").strip()
        
        if choice == '1':
            display_sections_menu()
        elif choice == '2':
            search_subnote()
        elif choice == '3':
            run_quiz()
        elif choice == '4':
            open_web_subnote()
        elif choice == '5':
            start_local_server()
        elif choice == '0' or not choice:
            print("\n프로그램을 종료합니다. 열공하세요! 🎓")
            sys.exit(0)
        else:
            print("\n⚠️ 올바른 번호를 선택해 주세요.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="재난관리연구방법론 Chapter 2 서브노트 CLI")
    parser.add_argument("--cli", action="store_true", help="CLI 터미널 메뉴 실행")
    parser.add_argument("--quiz", action="store_true", help="자가진단 퀴즈 즉시 실행")
    parser.add_argument("--search", type=str, help="키워드/학자명 즉시 검색")
    parser.add_argument("--web", action="store_true", help="브라우저에서 웹 서브노트 즉시 열기")
    parser.add_argument("--server", action="store_true", help="로컬 웹 서버 구동")
    
    args = parser.parse_args()
    
    if args.quiz:
        run_quiz()
    elif args.search:
        search_subnote()
    elif args.web:
        open_web_subnote()
    elif args.server:
        start_local_server()
    else:
        main_menu()
