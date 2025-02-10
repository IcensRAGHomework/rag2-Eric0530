from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)
from langchain_core.documents import Document

#q1_pdf = "OpenSourceLicenses.pdf"
#q2_pdf = "勞動基準法.pdf"


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
            chunks.append(Document(
                page_content=chunk,  # 內容
                metadata={
                    "file_name": q1_pdf,   # 檔名
                    "page_number": i + 1   # 頁碼（從 1 開始）
                }
            ))
    
    # 回傳最後一個 chunk 物件
    return chunks[-1] if chunks else None

def hw02_2(q2_pdf):
    # 使用 PyPDFLoader 讀取 PDF 文件
    loader = PyPDFLoader(q2_pdf)
    documents = loader.load()

    # 先把所有頁面的文字合併成一個大段落
    full_text = "\n".join([doc.page_content for doc in documents])

    # 初始化 RecursiveCharacterTextSplitter，根據章節與條文進行分割
    text_splitter = RecursiveCharacterTextSplitter(
        #separators = [r"\s*第\s*[\u4e00-\u9fa5]+\s*章\s*", r"\s*第\s*\d+(-\d+)?\s*條\s*\n"],
        separators = [r"第\s+[\u4e00-\u9fa5\d-]+\s+[章條]\s+"],
        chunk_size=10,
        chunk_overlap=6,
        is_separator_regex=True
    )

    # 使用 split_text() 分割文本
    split_texts = text_splitter.split_text(full_text)
    number = len(split_texts)
    # 轉換成 Document 物件，確保 metadata 保留
    chunks = [Document(page_content=chunk, metadata={"source": q2_pdf}) for chunk in split_texts]
    for i in range(0,len(chunks),1):
        print("chunks",i,"\n")        
        print(chunks[i],"\n")

    # 回傳 chunks 數量（整數值）
    return len(chunks)

#pdf1_path = "OpenSourceLicenses.pdf"
#last_chunk = hw02_1(pdf1_path)

#print(last_chunk)

# 執行 hw02_2 並獲取 chunk 數量
pdf2_path = "勞動基準法.pdf"
num_chunks = hw02_2(pdf2_path)
print(num_chunks)