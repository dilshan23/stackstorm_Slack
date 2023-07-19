# stackstorm_slack

Copy the example configuration in slack.yaml to /opt/stackstorm/configs/slack.yaml and edit as required.


Sensor: The sensor is responsible for monitoring a specific event source (e.g., Slack messages, file system changes, HTTP requests). When the sensor detects an event, it generates a trigger instance.

Trigger: The trigger represents the event that the sensor detected. It contains metadata about the event and may have a payload with relevant data.

Rule: The rule is used to define conditions and filters for when to execute an action based on a trigger. It specifies the criteria that the trigger payload must meet to trigger an action. Rules allow you to control the automation logic and define which actions should be executed in response to specific events.

Action: The action is the piece of code that performs a specific task or operation. It can be written in any programming language or script and can interact with external systems, APIs, or services.

When a sensor generates a trigger instance, the rules engine evaluates the trigger instance against the defined rules. If the trigger instance matches the criteria specified in a rule, the corresponding action(s) will be executed.




# https://docs.stackstorm.com/webhooks.html
Registering a Webhook
You can register a webhook in StackStorm by specifying the core.st2.webhook trigger inside a rule definition.

Here is an excerpt from a rule which registers a new webhook named sample:

...
trigger:
        type: "core.st2.webhook"
        parameters:
            url: "sample"
...
The url: parameter above is added as a suffix to /api/v1/webhooks/ to create the URL to POST data to. So once you have created the rule above, you can use this webhook by POST-ing data to your StackStorm server at https://{$ST2_IP}/api/v1/webhooks/sample.




## important
Ref : https://www.device42.com/blog/2016/11/02/automating-a-workflow-with-device42s-continuous-discovery-and-stackstorm/
st2 auth -t -p $ST2Password $ST2User   /// Ch@ngeMe  admin


root@da374dd15114:/opt/stackstorm/st2# st2 apikey create -k
ZWI1Y2Q0NDUyZjk1M2I2YmQyNGVjY2JkMjJiMTlkMTBhMmNkZTQ4ZWU4MDEzMmNhMGRkODkwYzEyZjI3YTQzNw



https://3f5d-112-134-61-244.ngrok-free.app/api/v1/webhooks/st2

 https://localhost/api/v1/webhooks/st2
