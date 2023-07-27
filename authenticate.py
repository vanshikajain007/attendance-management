from chalice import Chalice, UnauthorizedError
import jwt


secret_key_final = 'alaska'


def authenticate(app):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # print(app.current_request.headers)
            token = app.current_request.headers.get('Authorization')
            # print(token)
            if token:
                try:
                    # Verify and decode the JWT token
                    payload = jwt.decode(token, secret_key_final, algorithms=['HS256'])
                    # Add the decoded token to the request context
                    app.current_request.context['token_payload'] = payload
                    return func(*args, **kwargs)
                except jwt.exceptions.InvalidTokenError:
                    raise UnauthorizedError('Invalid token')
            else:
                raise UnauthorizedError('Token not provided')

        return wrapper
    return decorator


#
# @app.route('/my-post-endpoint', methods=['POST'])
# @authenticate
# def my_post_endpoint():
#     # Access the token payload from the request context
#     token_payload = app.current_request.context['token_payload']
#     print(token_payload)
