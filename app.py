import google.generativeai as genai
import streamlit as st

# タイトル
st.title("📈 友だち専用：ゆるっと資産形成ナビ")
st.caption("あなたの状況や興味に合わせた投資のヒントを提案します（※投資は自己責任でね！）")

# API設定（StreamlitのSecretsまたは直接指定）
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# 入力フォーム
age_group = st.selectbox("年代", ["20代", "30代", "40代", "50代以上"])
risk_style = st.radio("運用スタンス", ["手堅く守り重視", "標準（バランス型）", "多少リスクを取って攻めたい"])
interest = st.text_input("今気になっていること・キーワード", placeholder="例：新NISAの選び方、半導体、高配当株")

if st.button("アドバイスをもらう"):
    if not interest:
        st.warning("気になっていることを入力してね！")
    else:
        with st.spinner("Geminiが考え中..."):
            prompt = f"""
            あなたは親身で分かりやすい投資学習のアドバイザーです。友人にアドバイスするトーンで優しく答えてください。
            特定の個別銘柄の購入を断言するのではなく、考え方や参考になる選択肢（インデックス、ETF、業界の動向など）を整理してあげてください。

            【相談者の情報】
            - 年代: {age_group}
            - 運用スタンス: {risk_style}
            - 気になっていること: {interest}

            【回答の構成】
            1. その興味に対する今の市場のざっくりした見どころ
            2. 年代・スタンスに合わせたおすすめのアプローチ（例: コア・サテライト戦略など）
            3. 調べてみると面白い投資信託やETFのジャンル・着眼点
            4. 友だちへの一言アドバイス（注意点など）
            """
            response = model.generate_content(prompt)
            st.markdown(response.text)
