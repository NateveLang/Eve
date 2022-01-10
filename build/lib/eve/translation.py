from    eve.error import   NotFoundError
import  eve.grammar as     gr
from    eve.token import   get_token_ID

def translate(lexema, errors, tp):

    if get_token_ID(lexema, tp) == tp.identifier:
        return lexema, errors

    elif lexema in tp.protected:
        index = tp.protected.index(lexema)
        return gr.protected[index], errors

    else:
        errors += NotFoundError(None, "Not found name: " + lexema)
        return "404", errors
