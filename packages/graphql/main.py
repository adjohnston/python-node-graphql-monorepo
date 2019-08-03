import requests
from flask import Flask
from flask_graphql import GraphQLView
from graphene import ObjectType, String, Schema

app = Flask(__name__)


class Query(ObjectType):
    main = String()

    def resolve_main(self, root, info=None):
        response = requests.get('http://localhost:3000/').json()
        return response


schema = Schema(query=Query)

app.add_url_rule(
    '/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run()
