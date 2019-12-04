import string

def load_words(file_name):
   
    print('Loading word list from file...')
   
    in_file = open(file_name, 'r')
    line = in_file.readline()
    
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list


def is_word(word_list, word):
    
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


def get_story_string():
    
    f = open("E:\python\problem set 5\ps6\story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'E:\python\problem set 5\ps6\words.txt'

class Message(object):
   
    def __init__(self, text):
        
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
   
    def get_message_text(self):
        
        return self.message_text
   
    def get_valid_words(self):
       
        return self.valid_words[:]
    
    
    def build_shift_dict(self, shift):
        
        l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',\
             'q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F',\
             'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V',\
             'W','X','Y','Z']
       
        
        a = {}
        
        for i in range(0,26):
            t = shift + i
            if t >= 26:
                a[l[i]] = l[t-26]
            else:
                a[l[i]] = l[t]
                
        for j in range(26,52):
            t = shift + j
            if t >= 52:
                a[l[j]] = l[t-26]
            else:
                a[l[j]] = l[t]
            
       
        return a
        
        
    def apply_shift(self, shift):
       
        a = Message.build_shift_dict(self, shift)
        s=''
        for e in self.message_text:
            
            if e in string.punctuation or e in string.digits or e == ' ':
                s += e
            else:
                s += a[e]
    
        return s
        
class PlaintextMessage(Message):
    
    def __init__(self, text, shift):
        
        Message.__init__(self,text)
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self,shift)
        self.message_text_encrypted = Message.apply_shift(self,shift)
        

    def get_shift(self):
        
        return self.shift

    def get_encrypting_dict(self):
        
        return self.encrypting_dict[:]

    def get_message_text_encrypted(self):
        
        return self.message_text_encrypted

    def change_shift(self, shift):
        
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self,shift)
        self.message_text_encrypted = Message.apply_shift(self,shift)


class CiphertextMessage(Message):
    def __init__(self, text):
       
        Message.__init__(self,text)

    def decrypt_message(self):
        
        validWordNumber = 0
        x = 0
        t = 0
        
        for i in range(0,27):
            t = 0
            s = Message.apply_shift(self, 26-i)
            s = s.split(' ')
            
            for j in range(0,len(s)):
                if is_word(self.valid_words, s[j]) == True:
                    t += 1
            
            if t > validWordNumber:
                validWordNumber = t
                x = i
        
        
        y = (26-x, self.apply_shift( 26-x))
        return y
        
    
        

#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())
