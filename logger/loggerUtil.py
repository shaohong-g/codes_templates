import logging
import os
import inspect

# https://www.machinelearningplus.com/python/python-logging-guide/
# https://stackoverflow.com/questions/13733552/logger-configuration-to-log-to-file-and-print-to-stdout


# https://docs.python.org/3/howto/logging.html
def get_logger(production=False, fixed_logfile=True):
    """Create a logger object that writes to both stdout and a file.

    Parameters
    ----------
    production : bool, optional (default=False)
        Set stricter level if production is True.

    fixed_logfile: bool, optional (default=True)
        If True, log to '/tmp/output.log'. If False, log to '/tmp/{file}.log'.

    Returns
    -------
    logger
        A logger object.
    """
    # Get file name
    try:
        file_name = os.path.basename(inspect.stack()[1].filename)
    except Exception as e:
        file_name = os.path.basename(__file__)
    base_name = os.path.splitext(file_name)[0] 

    # Create logger
    logger = logging.getLogger(base_name)
    
    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler(f"/tmp/output.log") if fixed_logfile else logging.FileHandler(f"/tmp/{base_name}.log")

    # Set level
    if production:
        logger.setLevel(logging.INFO)
        c_handler.setLevel(logging.WARNING)
        f_handler.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.DEBUG)
        c_handler.setLevel(logging.DEBUG)
        f_handler.setLevel(logging.DEBUG)

    # Create formatters and add to handlers
    c_format = logging.Formatter('%(asctime)s::%(name)s::%(levelname)s - %(message)s', datefmt='%m-%d %H:%M:%S')
    f_format = logging.Formatter('%(asctime)s::%(name)s::%(funcName)s::%(lineno)d::%(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger


if __name__ == '__main__':
    logger = get_logger(production=True)

    logger.debug("Hello debug")
    logger.info("Hello info")
    logger.warning("Hello warning")
    logger.error("Hello error")
    logger.critical("Hello critical")
