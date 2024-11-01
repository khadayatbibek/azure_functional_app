# azure_functional_app
azure_functional_app is a  solution designed to deploy simple Azure time trigger function app that is scheduled to fetch the data from datalake and save it in csv file.

fetch_datalake is a  solution designed to extract, process, and manage csv datasets from Azure Data Lake. 

This repository provides a set of Python scripts and utilities that make it easy to query and retrieve data from a data lake, offering flexible configurations, and config to deploy azure function app.

## Getting Started

Clone the Repository:

    ```bash
    git clone https://github.com/khadayatbibek/azure_functional_app.git
    cd fetch_datalake
    ```

Install Dependencies: Use pip to install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

Configure Your Environment: Set up the necessary environment variables for your cloud provider.

Fetch Data: Modify the config.json to specify your target data lake, file format, and other parameters. Then run the fetch script:

    ```bash
    python fetch_data.py
    ```
Azure Function App : Modify the local.setting.json to specify your configs for your function app. Then deploy it after it run without a bug locally.
