from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import get_retriever

retriever = get_retriever()

model = OllamaLLM(
    model="llama3.2",
    temperature=0
)

template = """ 
Sen bir Roma seyahat asistanısın.

Sadece verilen içerikten yararlanarak cevap ver.
Asla ek yorum yapma.
Asla davetkar veya blog tarzı cümle kurma.
"TIKLAYIN" gibi ifadeleri kesinlikle yazma.
Cevap maksimum 3-4 cümle olsun.
Eğer içerikte bilgi yoksa: "Bu konuda içerikte bilgi bulunmuyor." yaz.

Bu yazının içeriği: {reviews}

Bu da cevaplanacak sorular: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

while True:
    print("\n---------------------------")
    question = input("Sorunuzu sorunuz. (Çıkış için q'a basınız.): ")
    print()

    if question == "q":
        break

    # 🔎 Retriever'dan ilgili chunkları çek
    docs = retriever.invoke(question)

    filtered_docs = [
    doc for doc in docs
    if "TIKLAYIN" not in doc.page_content
    ]


    # 📄 Sadece metinleri birleştir
    reviews = "\n\n".join([doc.page_content for doc in filtered_docs])

    # 🤖 LLM'e gönder
    result = chain.invoke({
        "reviews": reviews,
        "question": question
    })

    print(result)