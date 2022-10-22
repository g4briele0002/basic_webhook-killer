import requests

somethingowo = input("Input webhook to kill: ")

r = requests.delete(somethingowo)

print("Webhook killed successfully.")