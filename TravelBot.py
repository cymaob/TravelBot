import re
import random

class Chatbot:
        #negative responses
        negativeResponses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
        #exit commands
        exitCommands = ("quit", "pause", "exit", "goodbye", "bye", "later", 'stop', 'bubye')
        #random starter questions
        starterQuestions = (
                "Where would you like to travel to? \n",
                "What country would you like to go? \n"
                #"Is there anything I can do for you? \n",
                #"What would yo like me to help you with? \n"
        )
        byeMessages = (
                "Ok, have a nice day! \n",
                "Happy to help you another time! Enjoy your day! \n",
                "See you soon! \n"
        )


        def __init__(self):
                self.dialog = {
                        'france': r'.*\s*france.*',
                        'germany': r'.*\s*germany.*',
                        'austria': r'.*\s*austria.*',
                        'liechtenstein': r'.*\s*liechentenstein.*',
                        'italy': r'.*\s*italy.*',
                }
                
        
        def chat(self):
                reply = input("TravelBot: " + random.choice(self.starterQuestions)).lower()
                if not self.exit(reply):
                        reply = input(self.matchReply(reply))             


        def exit(self, reply):
                for exitMessage in self.exitCommands:
                        if exitMessage in reply.lower():
                                print("TravelBot:" + random.choice(self.byeMessages))
                                return True
                        return False
                                

        def matchReply(self, reply):
                for key, value in self.dialog.items():
                        intent = key
                        regexPattern = value
                        foundMatch = re.match(regexPattern, reply)

                        if foundMatch and intent == 'france':
                                country = "France"
                                print(self.countryReply(country))
                                print(self.cityReply(country))

                        elif foundMatch and intent == 'germany':
                                country = "Germany"
                                return self.countryReply(country)
                        
                        elif foundMatch and intent == 'austria':
                                country = "Austria"
                                return self.countryReply(country)
                        
                        elif foundMatch and intent == 'liechtenstein':
                                country = "Liechtenstein"
                                return self.countryReply(country)
                        
                        elif foundMatch and intent == 'italy':
                                country = "Italy"
                                return self.countryReply(country)
                        

        def countryReply(self, country):
                responses = (
                        "It's a great idea to go to " + country + "! ",
                )
                return ("TravelBot: " + random.choice(responses))
        
        def cityReply(self, country):
                France = ("Paris", "Marseille", "Lyon", "Nice")
                Germany = ("Berlin", "Hamburg", "Stuttgart", "Bremen", "Munich")
                Austria = ("Graz", "Salzburg", "Wien", "Innsbruck", "Linz")
                Liechtenstein = ("Vaduz")
                Italy = ("Milan", "Florence", "Rome", "Venice", "Naples")        

                responses = (
                        "You could go to " + random.choice(France) + ". It is very nice there!",
                )

                return "TravelBot: " + random.choice(responses)
                




# create intance and start chat
chatbotInstance = Chatbot()
chatbotInstance.chat()