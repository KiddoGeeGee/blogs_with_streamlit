import openai


openai.api_key='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'

class Chatbot:
    
    def __init__(self, ENGINE, temperature, max_tokens):
        self.engine = ENGINE
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.history = ''
        
    def chat(self, ask):
        if self.history!='':
            real_ask = self.history + f'{ask}\n\n'
        else:
            real_ask = f'{ask}\n\n'
        response = openai.Completion.create(engine=self.engine,
                                            prompt=real_ask,
                                            max_tokens=self.max_tokens,
                                            temperature=self.temperature)
        answer = response.choices[0]['text'].lstrip()
        return answer
        #self.save_chat(ask, answer)
        #return self.history
        
    def save_chat(self, ask, answer):
        self.history += f'{ask}\n\n'
        self.history += f'{answer}\n\n'
        
    #def new_conversation(self):
    #    self.history = ''