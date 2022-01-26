import time
import traceback
import exceptions


def terminate_run(e):
    close_all_thread = True
    if close_all_thread:
        # Here we close the logger/other threads
        del close_all_thread

    print "CODE ENDED WITH ERROR:"
    print "-" * 100
    print "{}".format(e)
    print "-" * 100
    time.sleep(0.2)
    raise exceptions.Exception(e)


def bad_foo(x):
    try:

        result = 3 / x

    except Exception as e:
        ret = dict()
        ret['INPUT'] = x
        ret['ERROR'] = traceback.format_exc()
        return ret

    ret = dict()
    ret['ERROR'] = None
    ret['INPUT'] = x
    ret['Result'] = result
    return ret


if __name__ == '__main__':
    print "Start of code"

    result_vector = list()
    error_vector = list()

    for idx in range(20):
        res = bad_foo(idx)
        if res['ERROR'] is None:
            result_vector.append(res)
        else:
            error_vector.append(res)

    for res_e in error_vector:
        terminate_run(res_e['ERROR'])

    print "Start of code"
