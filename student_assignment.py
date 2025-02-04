from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)


q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
     # 使用 PyPDFLoader 加載 PDF 文件
    loader = PyPDFLoader(q1_pdf)
    # 讀取每頁的內容
    documents = loader.load()
    # 初始化 CharacterTextSplitter，按頁分割文本
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=2000, chunk_overlap=0)
    # 將每頁的文本分割成 chunks
    chunks = []
    for i , doc in enumerate(documents):
        split_chunks = text_splitter.split_text(doc.page_content)
        for chunk in split_chunks:
            chunks.append({
                "file_name": q1_pdf,   # 檔名
                "page_number": i + 1,  # 頁碼（從 1 開始）
                "content": chunk       # 內容
            })
    
    # 回傳最後一個 chunk 物件
    return chunks[-1] if chunks else None

def hw02_2(q2_pdf):
    pass

pdf_path = "OpenSourceLicenses.pdf"
last_chunk = hw02_1(pdf_path)

print(last_chunk)