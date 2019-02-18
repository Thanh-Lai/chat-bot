## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. --> 
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - utter_greet <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 
 
## story_goodbye
* goodbye
 - utter_goodbye

## story_thanks
* thanks
 - utter_thanks
 
## story_joke_01
* joke
 - action_joke

## story_work_auth_status
* work_auth_status
 - utter_work_auth_status

## story_sponsorship
* sponsorship
 - utter_sponsorship
 
## story_joke_02
* greet
 - utter_greet
* joke
 - action_joke
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye
* work_auth_status
 - utter_work_auth_status
* sponsorship
 - utter_sponsorship
 