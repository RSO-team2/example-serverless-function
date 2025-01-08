# Serverless function
The serverless function example project is made with Digital Ocean CLI tool (doctl).

After installing doctl, make sure serverless is installed running the comand 'doctl serverless status'.
It should return 'Error: serverless support is installed but not connected to a functions namespace (use `doctl serverless connect`).'
Otherwise install serverless by running comand 'doctl serverless install'. 

Sample project in Python made with comand 'doctl serverless init --language python example-serverless-function'.

Project.yaml file can be changed to add triggers and configuration. 
Current cofniguration triggeres the function periodically every minute (now disabled trough Digital Ocean).

Invoking function trough cli: 'doctl serverless functions invoke sample/hello'

Checking the logs (limited to 5 logs): 'doctl serverless activations logs  --limit 5'