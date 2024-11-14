




def contains_suspicious_words(sentence):
    suspicious_keywords = ['hostage', 'explos', 'explosive']
    return any(keyword in sentence.lower() for keyword in suspicious_keywords)


def reorder_sentences(sentences):
    suspicious_sentences = [sentence for sentence in sentences if contains_suspicious_words(sentence)]
    safe_sentences = [sentence for sentence in sentences if not contains_suspicious_words(sentence)]
    return suspicious_sentences + safe_sentences