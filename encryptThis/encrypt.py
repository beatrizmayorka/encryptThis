def encryptThis(message):
    words = message.split()
    encrypted_words = []
    
    for word in words:
        if len(word) > 1:
            encrypted_word = str(ord(word[0])) + word[-1] + word[2:-1] + word[1]
        elif len(word) == 1:
            encrypted_word = str(ord(word))
        else:
            encrypted_word = ""
        
        encrypted_words.append(encrypted_word)
    
    encrypted_message = ' '.join(encrypted_words)
    
    return encrypted_message