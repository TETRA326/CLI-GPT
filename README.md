# CLI-GPT
Simple easy-to-setup way of using OpenAi's ChatGPT in Python, specifically for Google Cloud Shell.


## Setup
### 1. Create an OpenAI Account
If you do not know how to do this, follow [THIS](https://www.youtube.com/watch?v=0b49O19FyC8) tutorial.

### 2. Make a new API Key
Go to https://platform.openai.com/account/api-keys and make sure you are signed in. Then, create a new key by clicking '+ Create new secret key'.
Give it any name and press 'Create secret key'. Click the copy button and save your key:
![Copy button image](https://axispowers.rf.gd/source/images/copy.png)
DO NOT GIVE YOUR KEY TO ANYONE.

### 3. Log into Google Cloud Shell
Go to https://cloud.google.com/shell and click:
![Go-To-Console button image](https://axispowers.rf.gd/source/images/gotoconsole.png)
This will take you to your Cloud Shell Overview. If it is your first time in the Cloud Shell, you may have to accept Terms of Service and other legal documents.
If it hasn't already appeared, open the Terminal using this button:
![Open-Terminal button image](https://axispowers.rf.gd/source/images/console.png)

In the terminal, you should see something like: `account@cloudshell:~/`

### 4. Clone into Github Repo
Follow this command:
```
git clone https://github.com/TETRA326/CLI-GPT.git
```
When that is finished, run these commands:
```
cd CLI-GPT
chmod +x ./first-time
```

### 5. Run ./first-time and insert API Key
Run this command:
```
./first-time
```
When prompted, paste your OpenAi Secret Key. REMEMBER! Use `CTRL + SHIFT + V` to paste in the terminal.
Press enter to continue.

## Using ChatGPT in the Terminal

Run these 1 command:
```
gpt
```
or use this if you are experiencing problems:
```
~/CLI-GPT/gpt
```
This will give you a similar interface to talk to ChatGPT with. You can bookmark the tab to return later. Cloud Shell should recover your session.
