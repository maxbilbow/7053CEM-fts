from injector import singleton

# Import rest endpoints
import app.rest.PoiScoreResource
import app.rest.PoiReviewResource
import app.rest.IndexController
import app.rest.DbRestTest
import app.rest.AuthController

def configure(binder):
    # binder.bind(MyService, to=MyService, scope=singleton)
    # binder.bind(DatabaseBase, to=MySqlDatabase, scope=singleton)
    print("Hello!")
