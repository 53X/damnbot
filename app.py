# import flask dependencies
from flask import Flask, make_response, jsonify, request

# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return 'Hello World!'

# function for getting the response from the webhook
def results():
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    action = req.get('queryResult').get('action')
    if action == 'mug':
        parameters = req.get('queryResult').get('parameters')
        deliverytime = parameters['deliverytime']
        quantity = parameters['quantity']
        return {'fulfillmentText': 'Your order for {} mugs with desired delivery time as {} has been successfully placed!!!'.format(quantity, deliverytime)}
    
    if action == 'folder.folder-yes' or action == 'folder.folder-no':
        parameters = req.get('queryResult').get('outputContexts')[0].get('parameters')
        deliverytime = parameters['deliverytime']
        pouchprint = parameters['pouchprint']
        foldersize = parameters['foldersize']
        quantity = parameters['quantity']
        papertype = parameters['papertype']
        pouch = parameters['pouch']
        return {'fulfillmentText': 'Your order for {} folders has been placed. It will be delivered by {}!!!!'.format(quantity, deliverytime)}

    # return a fulfillment response
    return {'fulfillmentText': 'This is a response from webhook.'}    


# create a route for webhook
@app.route('/webhook',  methods=['GET', 'POST'])
def webhook():
     # return response
    return make_response(jsonify(results()))

# run the app
if __name__ == '__main__':
   app.run()
