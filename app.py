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
    if action == 'mug' or action == 'lanyard' or action == 'insidewall':
        parameters = req.get('queryResult').get('parameters')
        deliverytime = parameters['deliverytime']
        quantity = int(parameters['quantity'])
        return {'fulfillmentText': 'Your order for {} {} with desired delivery time as {} has been successfully placed!!!'.format(quantity, action, deliverytime)}
    
    if action == 'folder.folder-yes' or action == 'folder.folder-no':
        parameters = req.get('queryResult').get('outputContexts')[0].get('parameters')
        deliverytime = parameters['deliverytime']
        pouchprint = parameters['pouchprint']
        foldersize = parameters['foldersize']
        quantity = int(parameters['quantity'])
        papertype = parameters['papertype']
        pouch = parameters['pouch']
        return {'fulfillmentText': 'Your order for {} folders of size {} has been placed. It will be delivered by {}. Your choice for having "a pouch" and "print on the pouch" in your folder is "{}" and "{}" respectively!!!!'.format(quantity, foldersize, deliverytime, pouch,  pouchprint)}
    

    if action == 'idcard':
        parameters = req.get('queryResult').get('parameters')
        printkind = parameters['printkind']
        deliverytime = parameters['deliverytime']
        quantity = int(parameters['quantity'])
        return {'fulfillmentText': 'Your order for {} {} side printed ID cards with desired delivery time as {} has been successfully placed!!!'.format(quantity,  printkind, deliverytime)}

    if action == 'flyer':
        parameters = req.get('queryResult').get('parameters')
        papersize = parameters['papersize']
        printkind = parameters['printkind']
        colortype = parameters['colortype']
        flyerpaperthick = parameters['flyerpaperthick']
        deliverytime = parameters['deliverytime']
        quantity = parameters['quantity']
        return {'fulfillmentText': 'Your order for {} {} sized {} flyers with desired delivery time as {} has been successfully placed!!! The print kind of your choice is {} and the thickness of your flyer paper is {}'.format(quantity, papersize, colortype,  deliverytime,  printkind,  flyerpaperthick)}
    # return a fulfillment response
    
    if action == 'front':
        parameters = req.get('queryResult').get('parameters')
        papersize = parameters['papersize']
        stickerkind = parameters['stickerkind']
        deliverytime = parameters['deliverytime']
        quantity = parameters['quantity']
        return {'fulfillmentText': 'Your order for {} {} sized , {} front gumming stickers with desired delivery time as {} has been successfully placed!!!'.format(quantity, papersize, stickerkind, deliverytime)}

    if action == 'tentcard':
        parameters = req.get('queryResult').get('parameters')
        papersize = parameters['papersize']
        deliverytime = parameters['deliverytime']
        quantity = parameters['quantity']
        return {'fulfillmentText': 'Your order for {} {} sized , tent cards with desired delivery time as {} has been successfully placed!!!'.format(quantity, papersize, deliverytime)}

    if action == 'notebook':
        parameters = req.get('queryResult').get('parameters')
        papersize = parameters['papersize']
        paperthick = parameters['paperthick']
        pages = parameters['pages']
        bindingtype = parameters['bindingtype']
        foiling = parameters['foiling']
        spotuv = parameters['spotuv']
        deliverytime = parameters['deliverytime']
        quantity = parameters['quantity']
        
        return {'fulfillmentText': 'Your order for {} {} sized , {} paged {} notebooks with desired delivery time as {} has been successfully placed!!! The paper thickness of your choice is {}. Your opted "{}" for Foiling and "{}" for SpotUV.'.format(quantity, papersize, pages, bindingtype, deliverytime, paperthick,  foiling,  spotuv)}

    if action == 'sticker':
        parameters = req.get('queryResult').get('parameters')
        papersize = parameters['papersize']
        stickerkind = parameters['stickerkind']
        deliverytime = parameters['deliverytime']
        quantity = parameters['quantity']
        cuttingkind = parameters['cuttingkind']
        laminationkind  = parameters['laminationkind']
        return {'fulfillmentText': 'Your order for {} {} sized , {} stickers with desired delivery time as {} has been successfully placed!!! The cutting kind of your choice is {} and lamination kind of your choice is {}. Do you want to order anything else ?'.format(quantity, papersize, stickerkind, deliverytime, cuttingkind, laminationkind)}

    if action == 'paperbag':
        parameters = req.get('queryResult').get('parameters')
        papersize = parameters['papersize']
        thicknesstype = parameters['thicknesstype']
        deliverytime = parameters['deliverytime']
        quantity = parameters['quantity']
        return {'fulfillmentText': 'Your order for {} {} sized , {} thick paperbag with desired delivery time as {} has been successfully placed!!!'.format(quantity, papersize, thicknesstype, deliverytime)}
    
    if action == 'poster':
        parameters = req.get('queryResult').get('parameters')
        papersize = parameters['papersize']
        sunboard = parameters['sunboard']
        deliverytime = parameters['deliverytime']
        quantity = parameters['quantity']
        pregum = parameters['pregum']
        laminationkind  = parameters['laminationkind']
        return {'fulfillmentText': 'Your order for {} {} sized , {} posters with desired delivery time as {} has been successfully placed!!! Your choice for "pre-gumming" is "{}"" and that for "opting SunBoard" is {}. Do you want to order anything else ?'.format(quantity, papersize, laminationkind, deliverytime, pregum, sunboard)}
    
    if action == 'sticker':
        parameters = req.get('queryResult').get('parameters')
        papersize = parameters['papersize']
        stickerkind = parameters['stickerkind']
        deliverytime = parameters['deliverytime']
        quantity = parameters['quantity']
        cuttingkind = parameters['cuttingkind']
        laminationkind  = parameters['laminationkind']
        return {'fulfillmentText': 'Your order for {} {} sized , {} stickers with desired delivery time as {} has been successfully placed!!! The cutting kind of your choice is {} and lamination kind of your choice is {}. Do you want to order anything else ?'.format(quantity, papersize, stickerkind, deliverytime, cuttingkind, laminationkind)}

    if action == 'banner':
        parameters = req.get('queryResult').get('parameters')
        sunboard = parameters['sunboard']
        startdate = parameters['startdate']
        enddate = parameters['enddate']
        return {'fulfillmentText': 'Your order for banner has been successfully placed!!! The start date of your choice is {}, end date of your choice is {}. Your choice for "opting SunBoard" is {}. Do you want to order anything else ?'.format(startdate, enddate, sunboard)}
    
    if action == 'scribblepad':
        parameters = req.get('queryResult').get('parameters')
        papersize = parameters['papersize']
        scribblepadthick = parameters['scribblepadthick']
        pages = parameters['pages']
        foiling = parameters['foiling']
        spotuv = parameters['spotuv']
        deliverytime = parameters['deliverytime']
        quantity = parameters['quantity']
        
        return {'fulfillmentText': 'Your order for {} {} sized , {} paged scribble pads with desired delivery time as {} has been successfully placed!!! The paper thickness of your choice is {}. Your opted "{}" for Foiling and "{}" for SpotUV.'.format(quantity, papersize, pages, deliverytime, scribblepadthick, foiling, spotuv)}

    if action == 'billbook':
        parameters = req.get('queryResult').get('parameters')
        papersize = parameters['papersize']
        pouch = parameters['paperthick']
        colortype = parameters['colortype']
        startdate = parameters['startdate']
        enddate = parameters['enddate']
        deliverytime = parameters['deliverytime']
        quantity = parameters['quantity']
        
        return {'fulfillmentText': 'Your order for {} {} sized , {} bill-books with desired delivery time as {} has been successfully placed!!! The start date of your choice is {} and the desired end date is {}. Your opted "{}" for "Pouch" '.format(quantity, papersize, colortype, deliverytime, startdate, enddate, pouch)}

    
    
    return {'fulfillmentText': 'This is a response from webhook.'}    


# create a route for webhook
@app.route('/webhook',  methods=['GET', 'POST'])
def webhook():
     # return response
    return make_response(jsonify(results()))

# run the app
if __name__ == '__main__':
   app.run()
