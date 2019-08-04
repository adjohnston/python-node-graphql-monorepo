import requests
import graphene
from flask import Flask
from flask_graphql import GraphQLView
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={"/graphql": {"origins": "http://localhost:3001"}})


class Account(graphene.ObjectType):
    accountId = graphene.ID()
    name = graphene.String()
    org = graphene.String()
    pod = graphene.String()


class AccountInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    org = graphene.String(required=True)
    pod = graphene.String(required=True)


class CreateAccount(graphene.Mutation):
    class Arguments:
        input = AccountInput(required=True)

    account = graphene.Field(Account)

    def mutate(self, root, info=None, input=None):
        response = requests.post(
            'http://localhost:3000/accounts', data=input).json()
        print(response)
        account = Account(response)
        return CreateAccount(account=account)


class Query(graphene.ObjectType):
    account = graphene.Field(Account)

    def resolve_account(self, root):
        response = requests.get('http://localhost:3000/accounts').json()
        return response


class Mutation(graphene.ObjectType):
    create_account = CreateAccount.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

app.add_url_rule(
    '/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run()
