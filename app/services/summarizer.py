summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text:str):
    summary=summarizer(text,do_sample=false)
    return summary[0]['summary_text']
    


