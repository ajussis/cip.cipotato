from getpaid.core.options import PersistentOptions
from cip.cipotatotheme.getpaid.interfaces import IEmailOptions

EmailOptions = PersistentOptions.wire("EmailOptions",
                                      "cip.cipotatheme.getpaid",
                                      IEmailOptions)