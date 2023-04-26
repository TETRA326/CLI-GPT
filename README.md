![CLI-GPT Image](/images/CLI-GPT.png)

Simple easy-to-setup way of using OpenAi's ChatGPT in Python, specifically for Google Cloud Shell.

## Setup
### 1. Create an OpenAI Account
If you do not know how to do this, follow [THIS](https://www.youtube.com/watch?v=0b49O19FyC8) tutorial.

### 2. Make a new API Key
Go to https://platform.openai.com/account/api-keys and make sure you are signed in. Then, create a new key by clicking '+ Create new secret key'.
Give it any name and press 'Create secret key'. Click the copy button and save your key:

![Copy button image](/images/copy.png)

DO NOT GIVE YOUR KEY TO ANYONE.

### 3. Log into Google Cloud Shell
Go to https://shell.cloud.google.com/
Let the terminal at the bottom load.

In the terminal, you should see something like: `account@cloudshell:~/`

*Tip:*
You can un-check the 'Editor' button to full-screen the Terminal:

![Close-Editor](/images/pencil.png)

### 4. Clone into Github Repo
Follow this command:
```
git clone https://github.com/TETRA326/CLI-GPT.git
```
When that is finished, run these commands:
```
cd CLI-GPT
chmod +x ./setup
```

### 5. Run ./setup and insert API Key
Run this command:
```
./setup
```
When prompted, paste your OpenAI Secret Key. REMEMBER! Use `CTRL + SHIFT + V` to paste in the terminal.
Press enter to continue.

## Using ChatGPT in the Terminal

Run this command:
```
gpt
```
or use this if you are experiencing problems:
```
bash ~/CLI-GPT/gpt
```
This will give you a similar interface to talk to ChatGPT with. You can bookmark the tab to return later. Cloud Shell should recover your session.

*Hint:* You can use the `clear` command to remove all the text in the terminal and clear your workspace.

## Update
Run this every-so-often to make sure your code is up-to-date. Or, if you experience issues, you can run 'gpt-update' to reset everything. *Note: You will have to re-enter an Open AI Secret Key*
```
gpt-update
```

## Uninstall
Follow these 2 commands:
```
cd ~
rm -rf CLI-GPT
```

## Support
Join our public [Discord](https://discord.gg/NCXRYSmx2a) or DM TΞTRΛ#9264 for any help.
