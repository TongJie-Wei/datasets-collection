# URL handler to remove a user from all subscriptions
@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    db = get_db_connection()
    # using the given email, remove it from all subscriptions in the database
    # and return the number of subscriptions removed
