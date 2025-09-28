# Web Content Collection

> A collection of 1 web pages converted to Markdown format. Generated on 2025-09-28 15:03:03.

## Converted Web Pages

### Query a Cortex Search Service | Snowflake Documentation

**Source:** https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/query-cortex-search-service

# Query a Cortex Search Service¶

When you create a Cortex Search Service, the system provisions an API endpoint to serve queries at low latency. You can use three APIs for querying a Cortex Search Service:

  * The Python API

  * The REST API

  * The SQL SEARCH_PREVIEW Function




## Parameters¶

All APIs support the same set of query parameters:

| Parameter | Description  
---|---|---  
Required | `query` | The search query, to be searched for in the text column in the service.  
Optional | `columns` | A comma-separated list of columns to return for each relevant result in the response. These columns must be included in the source query for the service. If this parameter is not provided, only the search column is returned in the response.  
| `filter` | A filter object for filtering results based on data in the `ATTRIBUTES` columns. See Filter syntax for syntax.  
| `scoring_config` | Configuration object for customizing search ranking behavior. See Customizing search ranking for syntax.  
| `limit` | Maximum number of results to return in the response. Maximum accepted value is 1000. If not provided, the default value is 10.  
  
## Syntax¶

The following examples show how to query a Cortex Search Service using all three surfaces:

PythonREST APISQL
    
    
    import os
    from snowflake.core import Root
    from snowflake.snowpark import Session
    
    # connect to Snowflake
    CONNECTION_PARAMETERS = { ... }
    session = Session.builder.configs(CONNECTION_PARAMETERS).create()
    root = Root(session)
    
    # fetch service
    my_service = (root
        .databases["<service_database>"]
        .schemas["<service_schema>"]
        .cortex_search_services["<service_name>"]
    )
    
    # query service
    resp = my_service.search(
        query="<query>",
        columns=["<col1>", "<col2>"],
        filter={"@eq": {"<column>": "<value>"} },
        limit=5
    )
    print(resp.to_json())
    

Copy
    
    
    curl --location https://<ACCOUNT_URL>/api/v2/databases/<DB_NAME>/schemas/<SCHEMA_NAME>/cortex-search-services/<SERVICE_NAME>:query \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --header "Authorization: Bearer $PAT" \
    --data '{
      "query": "<search_query>",
      "columns": ["col1", "col2"],
      "filter": <filter>,
      "limit": <limit>
    }'
    

Copy
    
    
    SELECT PARSE_JSON(
      SNOWFLAKE.CORTEX.SEARCH_PREVIEW(
          'my_search_service',
          '{
             "query": "preview query",
             "columns":[
                "col1",
                "col2"
             ],
             "filter": {"@eq": {"col1": "filter value"} },
             "limit":10
          }'
      )
    )['results'] as results;
    

Copy

## Setup and authentication¶

### Python API¶

Cortex Search Services may be queried using version 0.8.0 or later of the Snowflake Python APIs. See [Snowflake Python APIs: Managing Snowflake objects with Python](../../../developer-guide/snowflake-python-api/snowflake-python-overview) for more information on the Snowflake Python APIs.

#### Install the Snowflake Python API library¶

First, install the latest version of the Snowflake Python APIs package from PyPI. See [Install the Snowflake Python APIs library](../../../developer-guide/snowflake-python-api/snowflake-python-installing) for instructions on installing this package from PyPI.
    
    
    pip install snowflake -U
    

Copy

#### Connect to Snowflake¶

Connect to Snowflake using either a Snowpark `Session` or a Python Connector `Connection` and create a `Root` object. See [Connect to Snowflake with the Snowflake Python APIs](../../../developer-guide/snowflake-python-api/snowflake-python-connecting-snowflake) for more instructions on connecting to Snowflake. The following example uses the Snowpark `Session` object and a Python dictionary for configuration.
    
    
    import os
    from snowflake.core import Root
    from snowflake.snowpark import Session
    
    CONNECTION_PARAMETERS = {
        "account": os.environ["snowflake_account_demo"],
        "user": os.environ["snowflake_user_demo"],
        "password": os.environ["snowflake_password_demo"],
        "role": "test_role",
        "database": "test_database",
        "warehouse": "test_warehouse",
        "schema": "test_schema",
    }
    
    session = Session.builder.configs(CONNECTION_PARAMETERS).create()
    root = Root(session)
    

Copy

Note

Version 0.8.0 or later of the Snowflake Python APIs library is required to query a Cortex Search Service.

### REST API¶

Cortex Search exposes a REST API endpoint in the suite of [Snowflake REST APIs](../../../developer-guide/snowflake-rest-api/snowflake-rest-api). The REST endpoint generated for a Cortex Search Service is of the following structure:
    
    
    https://<account_url>/api/v2/databases/<db_name>/schemas/<schema_name>/cortex-search-services/<service_name>:query
    

Copy

Where:

  * `<account_url>`: Your Snowflake Account URL. See [Finding the organization and account name for an account](../../admin-account-identifier.html#label-account-name-find) for instructions on finding your account URL.

  * `<db_name>`: Database in which the service resides.

  * `<schema_name>`: Schema in which the service resides.

  * `<service_name>`: Name of the service.

  * `:query`: The method to invoke on the service. In this case, the `query` method.




For additional details, see the REST API reference for [Cortex Search Service](https://docs.snowflake.com/developer-guide/snowflake-rest-api/reference/cortex-search-service).

#### Authentication¶

Snowflake REST APIs support authentication via programmatic access tokens (PATs), key pair authentication using JSON Web Tokens (JWTs), and OAuth. For details, see [Authenticating Snowflake REST APIs with Snowflake](../../../developer-guide/snowflake-rest-api/authentication).

### SQL SEARCH_PREVIEW function¶

The [SNOWFLAKE.CORTEX.SEARCH_PREVIEW](../../../sql-reference/functions/search_preview-snowflake-cortex) function allows you to preview the results of individual queries to a Cortex Search Service from within a SQL environment such as a worksheet or Snowflake notebook cell. This function makes it easy to quickly validate that a service is populated correctly and serving reasonable results.

Important

  * This function only operates on string literal queries. It does not accept batch text data.

  * This function incurs more latency than the REST or Python APIs. It is designed for testing/validation purposes. Don’t use this function for serving search queries in an end-user application that requires low latency.




## Filter syntax¶

Cortex Search supports filtering on the ATTRIBUTES columns specified in the [CREATE CORTEX SEARCH SERVICE](../../../sql-reference/sql/create-cortex-search) command.

Cortex Search supports five matching operators:

  * [TEXT](../../../sql-reference/data-types-text) or [NUMERIC](../../../sql-reference/data-types-numeric) equality: `@eq`

  * [ARRAY](../../../sql-reference/data-types-semistructured) contains: `@contains`

  * [NUMERIC](../../../sql-reference/data-types-numeric) or [DATE/TIMESTAMP](../../../sql-reference/data-types-datetime) greater than or equal to: `@gte`

  * [NUMERIC](../../../sql-reference/data-types-numeric) or [DATE/TIMESTAMP](../../../sql-reference/data-types-datetime) less than or equal to: `@lte`

  * [Primary key](cortex-search-overview.html#label-cortex-search-primary-keys) equality: `@primarykey`




These matching operators can be composed with various logical operators:

  * `@and`

  * `@or`

  * `@not`




### Usage notes¶

  * Matching against `NaN` (‘not a number’) values in the source query are handled as described in [Special values](../../../sql-reference/data-types-numeric).

  * Fixed-point numeric values with more than 19 digits (not including leading zeroes) do not work with `@eq`, `@gte`, or `@lte` and will not be returned by these operators (although they could still be returned by the overall query with the use of `@not`).

  * `TIMESTAMP` and `DATE` filters accept values of the form: `YYYY-MM-DD` and, for timezone aware dates: `YYYY- MM-DD+HH:MM`. If the timezone offset is not specified, the date is interpreted in UTC.

  * `@primarykey` is only supported for services configured with a [primary key](../../../sql-reference/constraints-overview). The value of the filter must be a JSON object mapping every primary key column to its corresponding value (or `NULL`).




These operators can be combined into a single filter object.

### Example¶

  * Filtering on rows where string-like column `string_col` is equal to value `value`.
        
        { "@eq": { "string_col": "value" } }
        

Copy

  * Filtering to a row with the specified primary key values `us-west-1` in the `region` column and `abc123` in the `agent_id` column:
        
        { "@primarykey": { "region": "us-west-1", "agent_id": "abc123" } }
        

Copy

  * Filtering on rows where ARRAY column `array_col` contains value `value`.
        
        { "@contains": { "array_col": "arr_value" } }
        

Copy

  * Filtering on rows where NUMERIC column `numeric_col` is between 10.5 and 12.5 (inclusive):
        
        {
          "@and": [
            { "@gte": { "numeric_col": 10.5 } },
            { "@lte": { "numeric_col": 12.5 } }
          ]
        }
        

Copy

  * Filtering on rows where TIMESTAMP column `timestamp_col` is between `2024-11-19` and `2024-12-19` (inclusive).
        
        {
          "@and": [
            { "@gte": { "timestamp_col": "2024-11-19" } },
            { "@lte": { "timestamp_col": "2024-12-19" } }
          ]
        }
        

Copy

  * Composing filters with logical operators:
        
        // Rows where the "array_col" column contains "arr_value" and the "string_col" column equals "value"
        {
          "@and": [
            { "@contains": { "array_col": "arr_value" } },
            { "@eq": { "string_col": "value" } }
          ]
        }
        
        // Rows where the "string_col" column does not equal "value"
        {
          "@not": { "@eq": { "string_col": "value" } }
        }
        
        // Rows where the "array_col" column contains at least one of "val1", "val2", or "val3"
        {
          "@or": [
            { "@contains": { "array_col": "val1" } },
            { "@contains": { "array_col": "val2" } },
            { "@contains": { "array_col": "val3" } }
          ]
        }
        

Copy




## Customizing search ranking¶

By default, queries to Cortex Search Services leverage semantic search and reranking to improve search result relevance. You can customize the scoring and ranking of search results in several ways:

  * Apply **numeric boosts** based on numeric metadata columns

  * Apply **time decays** based on timestamp metadata columns

  * Disable **reranking** to reduce query latency




### Numeric boosts and time decays¶

You can boost or apply decays search results based on numeric or timestamp metadata. This feature is useful when you have structured metadata (e.g., popularity or recency signals) per result that can help determine the relevance of documents at query time. You can specify two categories of ranking signals when making a query:

Type | Description | Applicable column types | Example metadata fields (illustrative)  
---|---|---|---  
Numeric boost | Numeric metadata that boosts results having more attention or activity. | [Numeric data type](../../../sql-reference/data-types-numeric) | `clicks`, `likes`, `comments`  
Time decay | Date or time metadata that boosts more recent results. The influence of recency signals decays over time. | [Date and time data type](../../../sql-reference/data-types-datetime) | `created_timestamp`, `last_opened_timestamp`, `action_date`  
  
Boost and decay metadata come from columns in the source table from which a Cortex Search Service is created. You specify the metadata columns to use for boosting or decaying when you make the query, but those columns must be included when creating the Cortex Search service.

**Querying a service with boost or decay signals**

When querying a Cortex Search Service, specify the columns to use for boosting or decaying in the optional `numeric_boosts` and `time_decays` fields in the `scoring_config.functions` field. You can also specify the weight for each boost or decay.
    
    
    {
      "scoring_config": {
        "functions": {
          "numeric_boosts": [
            {
              "column": "<column_name>",
              "weight": <weight>
            },
            // ...
          ],
          "time_decays": [
            {
              "column": "<column_name>",
              "weight": <weight>,
              "limit_hours": <limit_hours>
            },
            // ...
          ]
        }
      }
    }
    

Copy

**Properties:**

  * `numeric_boosts` (array, optional):

    * `<numeric_boost_object>` (object, optional):

      * `column_name` (string): Specifies the numeric column to which the boost should be applied.

      * `weight` (float): Specifies the weight or importance assigned to the boosted column in the ranking process. When multiple columns are specified, a higher weight increases the influence of the field.

  * `time_decays` (array, optional):

    * `<time_decay_object>` (object, optional):

      * `column_name` (string): Specifies the time or date column to which the decay should be applied.

      * `weight` (float): Specifies the weight or importance assigned to the decayed column in the ranking process. When multiple columns are specified, a higher weight increases the influence of the field.

      * `limit_hours` (float): Sets the boundary after which time starts to have less effect on the relevance or importance of the document. For example, a `limit_hours` value of 240 indicates that documents with timestamps greater than 240 hours (10 days) in the past from the `now` timestamp do not receive significant boosting, while documents with a timestamp within the last 240 hours should receive a more significant boost.

      * `now` (string, optional): Optional reference timestamp from which decays are calculated in ISO-8601 format `yyyy-MM-dd'T'HH:mm:ss.SSSXXX`. For example, `"2025-02-19T14:30:45.123-08:00"`. Defaults to the current timestamp if not specified.




Note

Numeric boosts are applied as weighted averages to the returned fields, while decays leverage a log-smoothed function to demote less recent values.

Weights are relative across the specified boost or decay fields. If only a single field is provided within a `boosts` or `decays` array, the value of its weight is irrelevant.

If more than one field is provided, the weights are applied relative to each other. A field with a weight of 10, for example, affects the record’s ranking twice as much as a field with a weight of 5.

### Reranking¶

By default, queries to Cortex Search Services leverage _semantic reranking_ to improve search result relevance. While reranking can measurably increase result relevance, it can also noticeably increase query latency. You can disable reranking in any Cortex Search query if you’ve found that the quality benefit that reranking provides can be sacrificed for faster query speeds in your business use case.

Note

Disabling reranking reduces query latency by 100-300ms on average, but the exact reduction in latency, as well as the magnitude of the quality degradation, varies across workloads. Evaluate results side-by-side, with and without reranking, before you decide to disable it in queries.

**Querying a Cortex Search Service without the reranker**

You can disable the reranker for an individual query at query time in the `scoring_config.reranker` field in the following format:
    
    
    {
      "scoring_config": {
          "reranker": "none"
    }
    

Copy

**Properties:**

  * `reranker` (string, optional): Parameter that can be set to “none” if the reranker should be turned off. If excluded or null, the default reranker is used.




## Access control requirements¶

The role that is querying the Cortex Search Service must have the following privileges to retrieve results:

Privilege | Object  
---|---  
USAGE | The Cortex Search Service  
USAGE | The database in which the Cortex Search Service resides  
USAGE | The schema in which the Cortex Search Service resides  
  
### Querying with owner’s rights¶

Cortex Search Services perform searches with [owner’s rights](../../../developer-guide/stored-procedure/stored-procedures-rights) and follow the same security model as other Snowflake objects that run with owner’s rights.

In particular, this means that any role with sufficient privileges to query a Cortex Search Service may query any of the data the service has indexed, regardless of that role’s privileges on the underlying objects (such as tables and views) referenced in the service’s source query.

For example, for a Cortex Search Service that references a table with row-level masking policies, querying users of that service will be able to see search results from rows on which the owner’s role has read permission, even if the querying user’s role cannot read those rows in the source table.

Use caution, for example, when granting a role with USAGE privileges on a Cortex Search Service to another Snowflake user.

## Known limitations¶

Querying a Cortex Search Service is subject to the following limitations:

  * **Response size** : The total size of the response payload returned from a search query to a Cortex Search Service must not exceed the following limits:

    * [REST API](https://docs.snowflake.com/developer-guide/snowflake-rest-api/reference/cortex-search-service) and [Python API](../../../developer-guide/snowflake-python-api/snowflake-python-overview): 10 Megabytes (MB)

    * [SQL SEARCH_PREVIEW Function](../../../sql-reference/functions/search_preview-snowflake-cortex): 300 Kilobytes (KB)




## Examples¶

This section provides comprehensive examples for querying Cortex Search Services across all three API methods.

### Setup for examples¶

The following examples use a table named `business_documents` with timestamp and numeric columns for demonstrating various features:
    
    
    CREATE OR REPLACE TABLE business_documents (
        document_contents VARCHAR,
        last_modified_timestamp TIMESTAMP,
        created_timestamp TIMESTAMP,
        likes INT,
        comments INT
    );
    
    INSERT INTO business_documents (document_contents, last_modified_timestamp, created_timestamp, likes, comments)
    VALUES
        ('Quarterly financial report for Q1 2024: Revenue increased by 15%, with expenses stable.',
         '2024-01-12 10:00:00', '2024-01-10 09:00:00', 10, 20),
    
        ('IT manual for employees: Instructions for usage of internal technologies, including hardware.',
         '2024-02-10 15:00:00', '2024-02-05 14:30:00', 85, 10),
    
        ('Employee handbook 2024: Updated policies on remote work, health benefits, and company culture.',
         '2024-02-10 15:00:00', '2024-02-05 14:30:00', 85, 10),
    
        ('Marketing strategy document: Target audience segmentation for upcoming product launch.',
         '2024-03-15 12:00:00', '2024-03-12 11:15:00', 150, 32),
    
        ('Product roadmap 2024: Key milestones for tech product development, including the launch.',
         '2024-04-22 17:30:00', '2024-04-20 16:00:00', 200, 45),
    
        ('Annual performance review process guidelines: Procedures for managers to conduct employee.',
         '2024-05-02 09:30:00', '2024-05-01 08:45:00', 60, 5);
    
    CREATE OR REPLACE CORTEX SEARCH SERVICE business_documents_css
        ON document_contents
        WAREHOUSE = <warehouse_name>
        TARGET_LAG = '1 minute'
    AS SELECT * FROM business_documents;
    

Copy

### Filter examples¶

#### Simple query with an equality filter¶

PythonREST APISQL
    
    
    resp = business_documents_css.search(
        query="technology",
        columns=["DOCUMENT_CONTENTS", "LIKES"],
        filter={"@eq": {"REGION": "US"}},
        limit=5
    )
    

Copy
    
    
    curl --location https://<ACCOUNT_URL>/api/v2/databases/<DB_NAME>/schemas/<SCHEMA_NAME>/cortex-search-services/<SERVICE_NAME>:query \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --header "Authorization: Bearer $PAT" \
    --data '{
      "query": "technology",
      "columns": ["DOCUMENT_CONTENTS", "LIKES"],
      "filter": {"@eq": {"REGION": "US"}},
      "limit": 5
    }'
    

Copy
    
    
    SELECT PARSE_JSON(
      SNOWFLAKE.CORTEX.SEARCH_PREVIEW(
          'business_documents_css',
          '{
             "query": "technology",
             "columns": ["DOCUMENT_CONTENTS", "LIKES"],
             "filter": {"@eq": {"REGION": "US"}},
             "limit": 5
          }'
      )
    )['results'] as results;
    

Copy

#### Range filter¶

PythonREST APISQL
    
    
    resp = business_documents_css.search(
        query="business",
        columns=["DOCUMENT_CONTENTS", "LIKES", "COMMENTS"],
        filter={"@and": [
            {"@gte": {"LIKES": 50}},
            {"@lte": {"COMMENTS": 50}}
        ]},
        limit=10
    )
    

Copy
    
    
    curl --location https://<ACCOUNT_URL>/api/v2/databases/<DB_NAME>/schemas/<SCHEMA_NAME>/cortex-search-services/<SERVICE_NAME>:query \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --header "Authorization: Bearer $PAT" \
    --data '{
      "query": "business",
      "columns": ["DOCUMENT_CONTENTS", "LIKES", "COMMENTS"],
      "filter": {"@and": [
        {"@gte": {"LIKES": 50}},
        {"@lte": {"COMMENTS": 50}}
      ]},
      "limit": 10
    }'
    

Copy
    
    
    SELECT PARSE_JSON(
      SNOWFLAKE.CORTEX.SEARCH_PREVIEW(
          'business_documents_css',
          '{
             "query": "business",
             "columns": ["DOCUMENT_CONTENTS", "LIKES", "COMMENTS"],
             "filter": {"@and": [
               {"@gte": {"LIKES": 50}},
               {"@lte": {"COMMENTS": 50}}
             ]},
             "limit": 10
          }'
      )
    )['results'] as results;
    

Copy

### Scoring examples¶

#### Numeric boosts¶

Apply numeric boosts to both the likes and comments columns, with twice the boost weight on comments values relative to likes values.

PythonREST APISQL
    
    
    resp = business_documents_css.search(
        query="technology",
        columns=["DOCUMENT_CONTENTS", "LIKES", "COMMENTS"],
        scoring_config={
            "functions": {
                "numeric_boosts": [
                    {"column": "comments", "weight": 2},
                    {"column": "likes", "weight": 1}
                ]
            }
        }
    )
    

Copy
    
    
    curl --location https://<ACCOUNT_URL>/api/v2/databases/<DB_NAME>/schemas/<SCHEMA_NAME>/cortex-search-services/<SERVICE_NAME>:query \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --header "Authorization: Bearer $PAT" \
    --data '{
      "query": "technology",
      "columns": ["DOCUMENT_CONTENTS", "LIKES", "COMMENTS"],
      "scoring_config": {
        "functions": {
          "numeric_boosts": [
            {"column": "comments", "weight": 2},
            {"column": "likes", "weight": 1}
          ]
        }
      }
    }'
    

Copy
    
    
    SELECT PARSE_JSON(
      SNOWFLAKE.CORTEX.SEARCH_PREVIEW(
          'business_documents_css',
          '{
             "query": "technology",
             "columns": ["DOCUMENT_CONTENTS", "LIKES", "COMMENTS"],
             "scoring_config": {
               "functions": {
                 "numeric_boosts": [
                   {"column": "comments", "weight": 2},
                   {"column": "likes", "weight": 1}
                 ]
               }
             }
          }'
      )
    )['results'] as results;
    

Copy

In the results, note:

>   * With the boosts, the “Product roadmap 2024:…” document is the top result because of its large number of likes and comments, even though it has slightly lower relevance to the query “technology”
> 
>   * Without any boosts, the top result for the query is “IT manual for employees:…”
> 
> 


#### Time decays¶

Apply time decays based on the LAST_MODIFIED_TIMESTAMP column, where:

>   * Documents with more recent LAST_MODIFIED_TIMESTAMP values, relative to the now timestamp, are boosted
> 
>   * Documents with a LAST_MODIFIED_TIMESTAMP value greater than 240 hours from the now timestamp receive little boosting
> 
> 


PythonREST APISQL
    
    
    resp = business_documents_css.search(
        query="technology",
        columns=["DOCUMENT_CONTENTS", "LAST_MODIFIED_TIMESTAMP"],
        scoring_config={
            "functions": {
                "time_decays": [
                    {"column": "LAST_MODIFIED_TIMESTAMP", "weight": 1, "limit_hours": 240, "now": "2024-04-23T00:00:00.000-08:00"}
                ]
            }
        }
    )
    

Copy
    
    
    curl --location https://<ACCOUNT_URL>/api/v2/databases/<DB_NAME>/schemas/<SCHEMA_NAME>/cortex-search-services/<SERVICE_NAME>:query \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --header "Authorization: Bearer $PAT" \
    --data '{
      "query": "technology",
      "columns": ["DOCUMENT_CONTENTS", "LAST_MODIFIED_TIMESTAMP"],
      "scoring_config": {
        "functions": {
          "time_decays": [
            {"column": "LAST_MODIFIED_TIMESTAMP", "weight": 1, "limit_hours": 240, "now": "2024-04-23T00:00:00.000-08:00"}
          ]
        }
      }
    }'
    

Copy
    
    
    SELECT PARSE_JSON(
      SNOWFLAKE.CORTEX.SEARCH_PREVIEW(
          'business_documents_css',
          '{
             "query": "technology",
             "columns": ["DOCUMENT_CONTENTS", "LAST_MODIFIED_TIMESTAMP"],
             "scoring_config": {
               "functions": {
                 "time_decays": [
                   {"column": "LAST_MODIFIED_TIMESTAMP", "weight": 1, "limit_hours": 240, "now": "2024-04-23T00:00:00.000-08:00"}
                 ]
               }
             }
          }'
      )
    )['results'] as results;
    

Copy

In the results, note:

>   * With the decays, the “Product roadmap 2024:…” document is the top result because of its recency to the now timestamp, even though it has slightly lower relevance to the query “technology”
> 
>   * Without any decays, the top result for the query is “IT manual for employees:…”
> 
> 


#### Disabling reranking¶

To disable reranking:

PythonREST APISQL
    
    
    resp = business_documents_css.search(
        query="technology",
        columns=["DOCUMENT_CONTENTS", "LAST_MODIFIED_TIMESTAMP"],
        limit=5,
        scoring_config={
            "reranker": "none"
        }
    )
    

Copy
    
    
    curl --location https://<ACCOUNT_URL>/api/v2/databases/<DB_NAME>/schemas/<SCHEMA_NAME>/cortex-search-services/<SERVICE_NAME>:query \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --header "Authorization: Bearer $PAT" \
    --data '{
      "query": "technology",
      "columns": ["DOCUMENT_CONTENTS", "LAST_MODIFIED_TIMESTAMP"],
      "scoring_config": {
        "reranker": "none"
      }
    }'
    

Copy
    
    
    SELECT PARSE_JSON(
      SNOWFLAKE.CORTEX.SEARCH_PREVIEW(
          'business_documents_css',
          '{
             "query": "technology",
             "columns": ["DOCUMENT_CONTENTS", "LAST_MODIFIED_TIMESTAMP"],
             "scoring_config": {
               "reranker": "none"
             }
          }'
      )
    )['results'] as results;
    

Copy

Tip

To query a service **with** the reranker, omit the `"reranker": "none"` parameter from the `scoring_config` object, as reranking is the default behavior.

On this page

  1. Parameters
  2. Syntax
  3. Setup and authentication
  4. Filter syntax
  5. Customizing search ranking
  6. Access control requirements
  7. Known limitations
  8. Examples



Related content

  1. [ALTER CORTEX SEARCH SERVICE](/user-guide/snowflake-cortex/cortex-search/../../../sql-reference/sql/alter-cortex-search)
  2. [CREATE CORTEX SEARCH SERVICE](/user-guide/snowflake-cortex/cortex-search/../../../sql-reference/sql/create-cortex-search)
  3. [DESCRIBE CORTEX SEARCH SERVICE](/user-guide/snowflake-cortex/cortex-search/../../../sql-reference/sql/desc-cortex-search)
  4. [DROP CORTEX SEARCH SERVICE](/user-guide/snowflake-cortex/cortex-search/../../../sql-reference/sql/drop-cortex-search)
  5. [SHOW CORTEX SEARCH SERVICES](/user-guide/snowflake-cortex/cortex-search/../../../sql-reference/sql/show-cortex-search)



Language: **English**

  * [English](/en/user-guide/snowflake-cortex/cortex-search/query-cortex-search-service)
  * [Français](/fr/user-guide/snowflake-cortex/cortex-search/query-cortex-search-service)
  * [Deutsch](/de/user-guide/snowflake-cortex/cortex-search/query-cortex-search-service)
  * [日本語](/ja/user-guide/snowflake-cortex/cortex-search/query-cortex-search-service)
  * [한국어](/ko/user-guide/snowflake-cortex/cortex-search/query-cortex-search-service)
  * [Português](/pt/user-guide/snowflake-cortex/cortex-search/query-cortex-search-service)

---
