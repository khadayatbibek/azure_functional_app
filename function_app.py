import logging
import azure.functions as func
import datetime
from fetch_datalake_functional import main

app = func.FunctionApp()

@app.schedule(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def timer_trigger(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')


@app.schedule(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=True, use_monitor=False) 
def download_datalake(myTimer: func.TimerRequest) -> None:
    logging.info("Function app started!")
    utc_timestamp = datetime.datetime.now().replace(tzinfo=datetime.timezone.utc).isoformat()
    main()
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')