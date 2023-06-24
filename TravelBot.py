import re
import random

class Chatbot:
        name = "You: "
        botName = "TravelBot: "
        negativeResponse = ("no", "nope", "nah", "not yet", "not a chance", "don't know")
        positiveResponse = ("yes", "great", "of course", "good", "go ahead")
        exitCommands = ("quit", "pause", "exit", "goodbye", "bye", "later", 'stop', 'bubye')
        nameQuestions = (
                "Whats your name? \n",
                "What should I call you? \n",
                "I'm curious, what's your name? \n",
                "Would you be so kind as to reveal your name to me? \n"
        )

        niceToMeet = (
                "Nice to meet you ",
                "It's a pleasure to meet you ",
                "Happy to help you "
        )

        starterQuestions = (
                "Do you already have a country in mind? \n",
                "Do you already have an idea of where you want to go? \n",
                "Have you decided on a particular country you'd like to go? \n"
        )

        byeMessages = (
                "Ok, have a nice day! \n",
                "Happy to help you another time! Enjoy your day! \n",
                "Ok, see you soon! \n"
        )

        countries = ("France","Germany","Austria","Liechtenstein","Italy")

        France = ("Paris", "Marseille", "Lyon", "Strasbourg")
        Germany = ("Berlin", "Hamburg", "Stuttgart", "Bremen", "Munich")
        Austria = ("Graz", "Salzburg", "Wien", "Innsbruck", "Linz")
        Liechtenstein = ("Vaduz")
        Italy = ("Milan", "Florence", "Rome", "Venice", "Naples")      

        def __init__(self):
                self.dialog = {
                        'france': r'^\s*france.*',
                        'germany': r'^\s*germany.*',
                        'austria': r'^\s*austria.*',
                        'liechtenstein': r'^\s*liechentenstein.*',
                        'italy': r'^\s*italy.*',
                }
                
        
        def chat(self):
                print(self.botName + "Welcome to Travelbot! Let me help you find a destination for your journey.")
                self.name = input(self.botName + random.choice(self.nameQuestions) + self.name)
                print(self.botName + random.choice(self.niceToMeet) + self.name + "!")
                self.start()
                

        def start(self):
                reply = input(self.botName + random.choice(self.starterQuestions) + self.name + ": ")
                if not self.exit(reply) and not self.noIdea(reply):
                        reply = input(self.matchReply(reply))
                        

        def exit(self, reply):
                for exitMessage in self.exitCommands:
                        if exitMessage in reply.lower():
                                print("TravelBot:" + random.choice(self.byeMessages))
                                return True
                        return False
                                
        
        def noIdea(self, reply):
                country = random.choice(self.countries)
                responses =(
                        "No worries, I'll help you. It would be a great idea to go to " + country + ".",
                        "Ok, Let me give you an idea: " + country + " is very beautiful and would be a great choice.",
                        country + " would be a great place to visit!",
                        country + " would be a good choice!"
                )
                for negativeMessage in self.negativeResponse:
                        if negativeMessage in reply.lower():
                                print(self.botName + random.choice(responses))
                                return self.cityReply(country)
                return None

                
        def matchReply(self, reply):
                for key, value in self.dialog.items():
                        intent = key
                        regexPattern = value
                        foundMatch = re.match(regexPattern, reply)

                        if foundMatch and intent == 'france':
                                country = "France"
                                print(self.countryReply(country))

                        elif foundMatch and intent == 'germany':
                                country = "Germany"
                                print(self.countryReply(country))
                        
                        elif foundMatch and intent == 'austria':
                                country = "Austria"
                                return (self.countryReply(country))
                        
                        elif foundMatch and intent == 'liechtenstein':
                                country = "Liechtenstein"
                                return (self.countryReply(country))
                        
                        elif foundMatch and intent == 'italy':
                                country = "Italy"
                                return (self.countryReply(country))
                        

        def countryReply(self, country):
                responses = (
                        "It's a great idea to go to " + country + "! ",
                        country + " is a great choice!"
                )
                print ("TravelBot: " + random.choice(responses))
                return self.cityReply(country)
        

        def cityReply(self, country):  
                if country == "France":
                        city = random.choice(self.France)
                elif country == "Austria":
                        city = random.choice(self.Austria)
                elif country == "Italy":
                        city = random.choice(self.Italy)
                elif country == "Liechtenstein":
                        city = random.choice(self.Liechtenstein)
                elif country == "Germany":
                        city = random.choice(self.Germany)

                responses = (
                        "You could go to " + city + ". It is very nice there!",
                        city + " would be an amazing choice!",
                        "I can recommend you to go to " + city + "!"
                )
                reply = input(self.botName + "Would you like me to propose you a city in " + country +"? \n" + self.name + ": ")
                if not self.exit(reply):
                        if self.negResponse(reply):
                                return self.again()
                        elif self.posResponse(reply):
                                print(self.botName + random.choice(responses))
                                return self.again()
                        else: return self.noMatch()
                
        def again(self):
                responses = (
                        "Would you like to start again? \n",
                        "Can I assist you with another idea? \n"
                )
                againMessage = (
                        "Ok, let's find another idea specifically for you!",
                        "Sure, I'm happy to help you again!"
                )
                reply = input(self.botName + random.choice(responses) + self.name + ": ")
                if not self.exit(reply):
                        if self.negResponse(reply):
                                print(self.botName + random.choice(self.byeMessages))
                                exit()
                        elif self.posResponse(reply):
                                print(self.botName + random.choice(againMessage))
                                return self.start()
                        else: self.noMatch()


        def negResponse(self, reply):
                for negativeReply in self.negativeResponse:
                        if negativeReply in reply.lower():
                                return True
                        return False

        def posResponse(self, reply):
                for positiveReply in self.positiveResponse:
                        if positiveReply in reply.lower():
                                return True
                        return False


        def noMatch(self):
                responses =(
                        "I'm sorry, I didn't understand that. Please try again \n",
                        "Unfortunately I cannot understand your answer. Please try again. \n"
                )
                return (self.botName + random.choice(responses))


# create intance and start chat
chatbotInstance = Chatbot()
chatbotInstance.chat()