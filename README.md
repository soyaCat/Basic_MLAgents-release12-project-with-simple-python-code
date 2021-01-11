# Basic_MLAgents-release12-project-with-simple-python-code
>This repository include simple ML-Agents release12 project and simple python code to use ML-Agents


This is useful basic code repository who want to use ML-Agent with custom python code

if you Don't know ML-Agent project that unity released, please see this Link:
https://github.com/Unity-Technologies/ml-agents

---

Recently, Unity release ML-Agents project Version Release12,
They also provide ML-Agents guide Link with This Release

But The guide Documents examples are little old, 
so They occur some error if you just use examples code to your python code

This repository's python code has revised code that corrected this errors. 
Not all error in examples, But They are useful if you are Novice Developer and not familiar with ML-agent

---

This is my environment

- Unity 2020.1.3f1
- MLAgents Release 12
- python 3.8.5
- MLAgents API ver 0.23.0

(Just followed this guide: https://github.com/Unity-Technologies/ml-agents/blob/release_12_docs/docs/Readme.md)

**/unity-project**

unity-project folder has unity project that can use with this repogistorys python code. 
Due to capacity problem, I'm using .gitignore file to reduce repogistory size. 
you can use this project by import "\unity-project\FallingStar\Assets\ML-Agents\Examples\FallingStar" to your unity project

**test_mlAgents.py**

You can get information about How to communicate with unity ML-Agents Environment. This code include 
some method how to get Agent information, how to send action to unity ml_agents, how to get observation from agent...ect. 
you can understand how to connect with ML-Agent, By reading this code and unity-projects C# code that located "\unity-project\FallingStar\Assets\ML-Agents\Examples\FallingStar". 

if you run this code, please set game directory before run this code
```python
if __name__ == "__main__":
  game = YOUR GAME DIRECTORY
```

**test_mlAgents_side_chennel.py**

To know about ML-Agents side chennel, please see this:
https://github.com/Unity-Technologies/ml-agents/blob/release_12_docs/docs/Custom-SideChannels.md

you can use side chennel to update parameter of Unity Environment.
Link guide work very well except little probelm. 
I implemented This guide for my Unity project and python code, 
and Add Text UI for my unity project so you can see message sended by python code

if you want to run this code, Dont forget set game directory to run this code
```python
# We start the communication with the Unity Editor and pass the string_log side channel as input
game = YOUR GAME DIRECTORY
```


