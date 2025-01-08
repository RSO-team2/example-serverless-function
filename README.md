# Serverless function for geolocation
The serverless function example project is made with Digital Ocean CLI tool (doctl).

After installing doctl, make sure serverless is installed running the comand `doctl serverless status`.
It should return `Error: serverless support is installed but not connected to a functions namespace (use doctl serverless connect).`
Otherwise install serverless by running comand `doctl serverless install`. 

Sample project in Python made with comand `doctl serverless init --language python example-serverless-function`.

Project.yaml file can be changed to add triggers and configuration. 
Current cofniguration triggeres the function periodically every minute (now disabled trough Digital Ocean), however later implementation will have it be triggered on API call for login to user-management.

Invoking function trough cli: `doctl serverless functions invoke sample/hello`

Checking the logs (limited to 5 logs): `doctl serverless activations logs  --limit 5`

Deploying the fucntion: `doctl serverless deploy example-serverless-function`

This function recieves the IP address of the user as a parameter and return a JSON object containing the geolocation of the user. If no IP is provided, it will resort to a default public IP "8.8.8.8". 
It calls to an external API [ip-api](https://ip-api.com/docs). This API does not provide SSL encryption in the free tier.

