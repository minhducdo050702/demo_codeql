import json

# Load the SARIF file
with open('python-results.sarif', 'r') as file:
    sarif_data = json.load(file)

# Extract tool information
tool_name = sarif_data['runs'][0]['tool']['driver']['name']
tool_version = sarif_data['runs'][0]['tool']['driver']['semanticVersion']

print(f'Tool Name: {tool_name}')
print(f'Tool Version: {tool_version}')

# Extract rules information
rules = sarif_data['runs'][0]['tool']['driver']['rules']
for rule in rules:
    rule_id = rule['id']
    rule_name = rule['name']
    rule_severity = rule['defaultConfiguration']['level']

    print(f'Rule ID: {rule_id}')
    print(f'Rule Name: {rule_name}')
    print(f'Severity: {rule_severity}')

# Extract invocation details
invocations = sarif_data['runs'][0]['invocations']
for invocation in invocations:
    tool_execution_notifications = invocation['toolExecutionNotifications']
    for notification in tool_execution_notifications:
        message = notification['message']['text']
        level = notification['level']
        time = notification['timeUtc']

        print(f'Message: {message}')
        print(f'Level: {level}')
        print(f'Time: {time}')

# Extract results (if any)
results = sarif_data['runs'][0]['results']
if results:
    print("Results:")
    for result in results:
        rule_id = result['ruleId']
        message = result['message']['text']
        level = result['level']
        locations = result['locations']

        print(f'Rule ID: {rule_id}')
        print(f'Message: {message}')
        print(f'Level: {level}')
        print(f'Locations: {locations}')

# You can further process and analyze the extracted information as needed
