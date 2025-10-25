# Web Content Collection

> A collection of 1 web pages converted to Markdown format. Generated on 2025-10-24 21:31:35.

## Converted Web Pages

### Connecting to Snowflake with the Python Connector | Snowflake Documentation

**Source:** https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-connect

# Connecting to Snowflake with the Python Connector¶

This topic explains the various ways you can connect to Snowflake with the Python connector.

Important

Beginning with Snowflake version 8.24, network administrators have the option to require multi-factor authentication (MFA) for all connections to Snowflake. If your administrator decides to enable this feature, you must configure your client or driver to use MFA when connecting to Snowflake. For more information, see the following resources:

  * [8.24 release notes](../../release-notes/2024/8_24.html#label-authentication-policies-new-multi-factor-authentication-parameters)

  * [Multi-factor authentication (MFA)](../../user-guide/security-mfa)

  * [Troubleshooting service users authentication issues with Snowflake MFA](https://community.snowflake.com/s/article/Troubleshooting-service-users-authentication-issues-with-Snowflake-MFA) Knowledge Base article




## Verifying the network connection to Snowflake with SnowCD¶

After configuring your driver, you can evaluate and troubleshoot your network connectivity to Snowflake using [SnowCD](../../user-guide/snowcd).

You can use SnowCD during the initial configuration process and on-demand to evaluate and troubleshoot your network connection to Snowflake.

## Importing the `snowflake.connector` module¶

To import the `snowflake.connector` module, execute the following command:
    
    
    import snowflake.connector
    

Copy

You can get login information from environment variables, the command line, a configuration file, or another appropriate source. For example:
    
    
    PASSWORD = os.getenv('SNOWSQL_PWD')
    WAREHOUSE = os.getenv('WAREHOUSE')
    ...
    

Copy

For the ACCOUNT parameter, use your [account identifier](../../user-guide/gen-conn-config). Note that the account identifier does not include the `snowflakecomputing.com` suffix.

For details and examples, see [Usage notes for the account parameter (for the connect method)](python-connector-api.html#label-account-format-info).

Note

For descriptions of available connector parameters, see the `snowflake.connector` [methods](python-connector-api.html#label-snowflake-connector-methods).

If you copy data from your own Amazon S3 bucket, then you need the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY.
    
    
    import os
    
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    

Copy

Note

If your data is stored in a Microsoft Azure container, provide the credentials directly in the COPY statement.

After reading the connection information, connect using either the default authenticator or federated authentication (if enabled).

## Setting session parameters¶

You can set session parameters, such as QUERY_TAG, in multiple ways when using the Python Connector:

  * You can set session-level parameters at the time you connect to Snowflake by passing the optional connection parameter named `session_parameters`, as follows:
        
        con = snowflake.connector.connect(
            user='XXXX',
            password='XXXX',
            account='XXXX',
            session_parameters={
                'QUERY_TAG': 'EndOfMonthFinancials',
            }
        )
        

Copy

The `session_parameters` dictionary passed to the [snowflake.connector.connect](python-connector-api.html#label-snowflake-connector-methods-connect) method can contain one or more session-level parameters.

Note

You cannot set the [SEARCH_PATH](../../sql-reference/parameters.html#label-search-path) parameter within a Python connection. You must establish a session before setting a search path.

  * You can also set session parameters by executing the ALTER SESSION SET SQL statement after connecting:
        
        con.cursor().execute("ALTER SESSION SET QUERY_TAG = 'EndOfMonthFinancials'")
        

Copy




For more information about session parameters, see the descriptions of individual parameters on the general [Parameters](../../sql-reference/parameters) page.

## Connecting using the default authenticator¶

Connect to Snowflake using the login parameters:
    
    
    conn = snowflake.connector.connect(
        user=USER,
        password=PASSWORD,
        account=ACCOUNT,
        warehouse=WAREHOUSE,
        database=DATABASE,
        schema=SCHEMA
        )
    

Copy

You might need to extend this with other information available in the [snowflake.connector.connect](python-connector-api.html#label-snowflake-connector-methods-connect) method.

## Connecting using the `connections.toml` file¶

The Python connector lets you add connection definitions to a `connections.toml` configuration file. A connection definition refers to a collection of connection-related parameters. Snowflake Python libraries currently support TOML version 1.0.0.

For more information about `toml` file formats, see [TOML (Tom’s Obvious Minimal Language)](https://toml.io/en/).

The Python connector looks for the `connections.toml` file in the following locations, in order:

  * If a `~/.snowflake` directory exists on your machine, the Python Connector uses the `~/.snowflake/connections.toml` file. You can override the default `~/.snowflake` directory by setting the location in the `SNOWFLAKE_HOME` environment variable.

  * Otherwise, the Python Connector uses the `connections.toml` file in the one of the following locations, based on your operating system:

>     * Linux: `~/.config/snowflake/connections.toml`, but you can update it with XDG vars
> 
>     * Windows: `%USERPROFILE%\AppData\Local\snowflake\connections.toml`
> 
>     * Mac: `~/Library/Application Support/snowflake/connections.toml`




To add credentials in a connections configuration file:

  1. In a text editor, open the `connections.toml` file for editing. For example, to open the file in the Linux **vi** editor:
         
         $ vi connections.toml
         

Copy

  2. Add a new Snowflake connection definition.

You can generate the basic settings for the TOML configuration file in Snowsight. For information, see [Configuring a client, driver, library, or third-party application to connect to Snowflake](../../user-guide/gen-conn-config).

For example, to add a Snowflake connection called `myconnection` with the account `myaccount`, user `johndoe`, and password credentials, as well as database information, add the following lines to the configuration file:
         
         [myconnection]
         account = "myorganization-myaccount"
         user = "jdoe"
         password = "******"
         warehouse = "my-wh"
         database = "my_db"
         schema = "my_schema"
         

Copy

Connection definitions support the same configuration options available in the [snowflake.connector.connect](python-connector-api.html#label-snowflake-connector-methods-connect) method.

  3. Optional: Add more connections, as shown:
         
         [myconnection_test]
         account = "myorganization-myaccount"
         user = "jdoe-test"
         password = "******"
         warehouse = "my-test_wh"
         database = "my_test_db"
         schema = "my_schema"
         

Copy

  4. Save changes to the file.

  5. In your Python code, supply the connection name to `snowflake.connector.connect`, similar to the following:
         
         with snowflake.connector.connect(
               connection_name="myconnection",
         ) as conn:
         

Copy

You can also override values defined for the connection in the `connections.toml` file, as follows:
         
         with snowflake.connector.connect(
               connection_name="myconnection",
               warehouse="test_xl_wh",
               database="testdb_2"
         ) as conn:
         

Copy




## Setting a default connection¶

You can set a connection as the default, so you don’t have to specify one every time you call `snowflake.connector.connect()` to connect to Snowflake. You can define a default connection in any of the following ways, which are listed in increasing order of precedence:

  * Create a connection definition named `default`.

    1. In the `connections.toml` file, create the connection definition and give it the name `default`, as shown:
           
           [default]
           account = "myorganization-myaccount"
           user = "jdoe-test"
           password = "******"
           warehouse = "my-test_wh"
           database = "my_test_db"
           schema = "my_schema"
           

Copy

    2. Save the file.

  * Specify a named connection as the default connection in the Snowflake `config.toml` file, in the same directory as the `connections.toml` file.

    1. Open the `config.toml` file for editing; then:

    2. Set the `default_connection_name` parameter similar to the following:
           
           default_connection_name = "myaccount"
           

Copy

    3. Save the file.

  * Set the `SNOWFLAKE_DEFAULT_CONNECTION_NAME` environment variable.

Sometimes you might want to override the default connection temporarily, such as trying a test connection, without needing to change the normal default connection. You can override the default connection specified in the `connections.toml` and `config.toml` files by setting the `SNOWFLAKE_DEFAULT_CONNECTION_NAME` environment variable as follows:
        
        SNOWFLAKE_DEFAULT_CONNECTION_NAME = myconnection_test
        

Copy




To use the default connection, execute Python code similar to the following:

> 
>     with snowflake.connector.connect() as conn:
>         with conn.cursor() as cur:
>             print(cur.execute("SELECT 1;").fetchall())
>     
> 
> Copy

Note

If you choose to rely on a default connection, you cannot override connection parameters, such as `username`, `database`, or `schema`.

## Using single sign-on (SSO) for authentication¶

If you have [configured Snowflake to use single sign-on (SSO)](../../user-guide/admin-security-fed-auth-overview), you can configure your client application to use SSO for authentication. See [Using SSO with client applications that connect to Snowflake](../../user-guide/admin-security-fed-auth-use.html#label-sso-with-command-line-clients) for details.

## Using multi-factor authentication (MFA)¶

Snowflake supports caching MFA tokens, including combining MFA token caching with SSO.

For more information, see [Using MFA token caching to minimize the number of prompts during authentication — optional](../../user-guide/security-mfa.html#label-mfa-token-caching).

## Using key-pair authentication and key-pair rotation¶

The Python connector supports key pair authentication and key rotation.

For more information on how to configure key pair authentication and key rotation, see [Key-pair authentication and key-pair rotation](../../user-guide/key-pair-auth).

  1. After completing the key pair authentication configuration, set the `private_key_file` parameter in the `connect` function to the path to the private key file. Also, set the `private_key_file_pwd` parameter to the passphrase of the private key file.

  2. Modify and execute the sample code, below:




>   * Update the security parameters:
>
>>     * `_path_`: Specifies the local path to the private key file you created.
> 
>   * Update the connection parameters:
>
>>     * `user`: Specifies your Snowflake login name.
>> 
>>     * `account_identifier`: Specifies your [account identifier](../../user-guide/gen-conn-config).
>> 
>> For more details, see [Usage notes for the account parameter (for the connect method)](python-connector-api.html#label-account-format-info).
> 
> 

>
>> **Sample code**
>>     
>>     
>>     import os
>>     import snowflake.connector as sc
>>     
>>     private_key_file = '<path>'
>>     private_key_file_pwd = '<password>'
>>     
>>     conn_params = {
>>         'account': '<account_identifier>',
>>         'user': '<user>',
>>         'authenticator': 'SNOWFLAKE_JWT',
>>         'private_key_file': private_key_file,
>>         'private_key_file_pwd':private_key_file_pwd,
>>         'warehouse': '<warehouse>',
>>         'database': '<database>',
>>         'schema': '<schema>'
>>     }
>>     
>>     ctx = sc.connect(**conn_params)
>>     cs = ctx.cursor()
>>     
>> 
>> Copy

## Using a proxy server¶

To use a proxy server, configure the following environment variables:

  * HTTP_PROXY

  * HTTPS_PROXY

  * NO_PROXY




For example:

Linux or macOS:
    
    
    
    export HTTP_PROXY='http://username:password@proxyserver.example.com:80'
    export HTTPS_PROXY='http://username:password@proxyserver.example.com:80'
    

Copy

Windows:
    
    
    
    set HTTP_PROXY=http://username:password@proxyserver.example.com:80
    set HTTPS_PROXY=http://username:password@proxyserver.example.com:80
    

Copy

Tip

Snowflake’s security model does not allow Secure Sockets Layer (SSL) proxies (using an HTTPS certificate). Your proxy server must use a publicly-available Certificate Authority (CA), reducing potential security risks such as a MITM (Man In The Middle) attack through a compromised proxy.

If you must use your SSL proxy, we strongly recommend that you update the server policy to pass through the Snowflake certificate such that no certificate is altered in the middle of communications.

Optionally `NO_PROXY` can be used to bypass the proxy for specific communications. For example, access to Amazon S3 can bypass the proxy server by specifying `NO_PROXY=".amazonaws.com"`.

`NO_PROXY` does not support wildcards. Each value specified should be one of the following:

  * The end of a hostname (or a complete hostname), for example:

    * .amazonaws.com

    * myorganization-myaccount.snowflakecomputing.com

  * An IP address, for example:

    * 192.196.1.15




If more than one value is specified, values should be separated by commas, for example:

> 
>     localhost,.example.com,.snowflakecomputing.com,192.168.1.15,192.168.1.16
>     
> 
> Copy

## Connecting with OAuth¶

To connect using OAuth, the connection string must include the `authenticator` parameter set to `oauth` and the `token` parameter set to the `oauth_access_token`. For more information, see [Clients, drivers, and connectors](../../user-guide/oauth-intro.html#label-oauth-intro-clients-drivers-conns).
    
    
    ctx = snowflake.connector.connect(
        user="<username>",
        host="<hostname>",
        account="<account_identifier>",
        authenticator="oauth",
        token="<oauth_access_token>",
        warehouse="test_warehouse",
        database="test_db",
        schema="test_schema"
    )
    

Copy

### Enable the OAuth 2.0 Authorization Code flow¶

The OAuth 2.0 Authorization Code flow is a secure method for a client application to obtain an access token from an authorization server on behalf of a user, without revealing the user’s credentials.

To enable the OAuth 2.0 Authorization Code flow:

  * Set the `authenticator` connection parameter to `OAUTH_AUTHORIZATION_CODE`.

  * Set the following OAuth connection parameters:

    * `oauth_client_id`: Value of `client id` provided by the Identity Provider for Snowflake integration (Snowflake security integration metadata).

    * `oauth_client_secret`: Value of the `client secret` provided by the Identity Provider for Snowflake integration (Snowflake security integration metadata).

    * `oauth_authorization_url`: Identity Provider endpoint supplying the authorization code to the driver. When using Snowflake as an Identity Provider ,this value is derived from the `server` or `account` parameters.

    * `oauth_token_request_url`: Identity Provider endpoint supplying the access tokens to the driver. When using Snowflake as an Identity Provider ,this value is derived from the `server` or `account` parameters.

    * `oauth_scope`: Scope requested in the Identity Provider authorization request. By default, it is derived from the role. When multiple scopes are required, the value should be a space-separated list of multiple scopes.

    * `oauth_redirect_uri`: URI to use for authorization code redirection (Snowflake security integration metadata). Default: `http://127.0.0.1:{randomAvailablePort}`.

    * `oauth_disable_pkce:` Disables Proof Key for Code Exchange (PKCE), a security enhancement that ensures that even if malicious attackers intercept an Authorization Code, they won’t be able to change it to a valid access token.

    * `oauth_enable_refresh_token:` Enables a silent re-authentication when the actual access token becomes outdated, providing it’s supported by the Authorization Server and `client_store_temporary_credential` is set to `True`.

    * `oauth_enable_single_use_refresh_tokens:` Whether to opt-in to single-use refresh token semantics.




### Enable the OAuth 2.0 Client Credentials flow¶

The OAuth 2.0 Client Credentials flow provides a secure way for machine-to-machine (M2M) authentication, such as the Snowflake Connector for Python connecting to a backend service. Unlike the OAuth 2.0 Authorization Code flow, this method does not rely on any user-specific data.

To enable the OAuth 2.0 Client Credentials flow:

  * Set the `authenticator` connection parameter to `OAUTH_CLIENT_CREDENTIALS`.

  * Set the following OAuth connection parameters:

    * `oauth_client_id`: Value of `client id` provided by the Identity Provider for Snowflake integration (Snowflake security integration metadata).

    * `oauth_client_secret`: Value of the `client secret` provided by the Identity Provider for Snowflake integration (Snowflake security integration metadata)

    * `oauth_token_request_url`: Identity Provider endpoint supplying the access tokens to the driver. When using Snowflake as an Identity Provider, this value is derived from the `server` or `account` parameters.

    * `oauth_scope`: Scope requested in the Identity Provider authorization request. By default, it is derived from the role. When multiple scopes are required, the value should be a space-separated list of multiple scopes.




## Authenticating with workload identity federation (WIF)¶

[Workload identity federation](../../user-guide/workload-identity-federation) provides a service-to-service authentication method for Snowflake. This method enables applications, services, or containers to authenticate with Snowflake by leveraging their cloud provider’s native identity system, such as AWS IAM, Microsoft Entra ID, or Google Cloud service accounts. This approach eliminates the need for managing long-lived credentials and simplifies credential acquisition compared to other methods like External OAuth. Snowflake connectors are designed to automatically obtain short-lived credentials from the platform’s identity provider.

To enable the workload identity federation authenticator, do the following:

  1. Set the `authenticator` connection parameter to `WORKLOAD_IDENTITY`.

  2. Set the `workload_identity_provider` connection parameter to `AWS`, `AZURE`, `GCP`, or `OIDC`, based on your platform.

  3. For OpenID Connect (OIDC), specify the `token` connection parameter.




## Authenticating with a programmatic access token (PAT)¶

Programmatic Access Token (PAT) is a Snowflake-specific authentication method. The feature must be enabled for the account before usage (see the [Prerequisites](../../user-guide/programmatic-access-tokens.html#label-pat-prerequisites) for more information). Authentication with PAT doesn’t involve any human interaction.

For more information about PATs, see [Using programmatic access tokens for authentication](../../user-guide/programmatic-access-tokens).

## Managing connection timeouts¶

Calling `snowflake.connector.connect` submits a login request. If a login request fails, the connector can resend the connection request. The following parameters set time limits after which the connector stops retrying requests:

  * `login_timeout`: Specifies how long, in seconds, to keep resending the connection request. If the connection is unsuccessful within that time, the connector fails with a timeout error after completing the current attempt instead of continuing to retry the login request. After the timeout passes, further retries are prevented. However, the current ongoing attempt terminates naturally.

  * `network_timeout`: Specifies how long to wait for network issues to resolve for other requests, such as query requests from `cursor.execute`. When `network_timeout` seconds have passed, if the current attempt fails, a timeout occurs, and the request in question is not retried. After `network_timeout` seconds pass, the current attempt is still allowed to finish (fail on its own), after which the timeout occurs.

  * `socket_timeout`: Specifies the connection and request timeouts at the socket level.




The following example overrides the `socket_timeout` for the SNOWFLAKE_JWT authenticator:
    
    
    # this request itself stops retrying after 60 seconds as it is a login request
    conn = snowflake.connector.connect(
    login_timeout=60,
    network_timeout=30,
    socket_timeout=10
    )
    
    # this request stops retrying after 30 seconds
    conn.cursor.execute("SELECT * FROM table")
    

Copy

The following example demonstrates the effect of setting `socket_timeout` to a large value:
    
    
    # even though login_timeout is 1, connect will take up to n*300 seconds before failing
    # (n depends on possible socket addresses)
    # this issue arises because socket operations cannot be cancelled once started
    conn = snowflake.connector.connect(
    login_timeout=1,
    socket_timeout=300
    )
    

Copy

The following example shows how to override the socket timeout for the SNOWFLAKE_JWT authenticator:
    
    
    # socket timeout for login request overriden by env variable JWT_CNXN_WAIT_TIME
    conn = snowflake.connector.connect(
    authenticator="SNOWFLAKE_JWT",
    socket_timeout=300
    )
    
    # socket timeout for this request is still 300 seconds
    conn.cursor.execute("SELECT * FROM table")
    

Copy

Note that the `MAX_CON_RETRY_ATTEMPTS` environment variable limits the maximum number of retry attempts for login requests. If a request has not timed out but the maximum number of retry attempts is reached, the request immediately fails. The default value is 1, meaning the connector makes only one retry attempt.

## Managing connection backoff policies for retries¶

In some situations, you might want to vary the rate or frequency the connector uses to retry failed requests due to timeouts. For example, if you notice that very large numbers of attempts occur concurrently, you can spread those requests out by defining a retry backoff policy. A backoff policy specifies the time to wait between retry attempts.

The Snowflake Connector for Python implements backoff policies with the `backoff_policy` connection parameter that specifies a Python generator function. The generator function lets you specify how long to wait (back off) before sending the next retry request.

Snowflake provides the following helpers to create predefined generator functions with your desired parameters. You can use these if you do not want to create your own:

  * `linear_backoff`, which increases the backoff duration by a constant each iteration.

  * `exponential_backoff`, which multiplies the backoff duration by a constant each iteration.

  * `mixed_backoff`, which randomly chooses between incrementing the backoff duration with `exponential_backoff` and leaving it unchanged each iteration.




These predefined generator functions use the following parameters to specify their behaviors:

  * `base`: Initial backoff time, in seconds (default = `1`).

  * `factor`: Coefficient for incrementing the backoff time. The effect depends on implementation (default = `2`); `linear_backup` adds the value, while `exponential_backup` multiplies the value.

  * `cap`: Maximum backoff time, in seconds (default = `16`).

  * `enable_jitter`: Whether to enable jitter on computed durations (default = `True`).

For more information about jitter in exponential backoff, see the [AWS Exponential Backoff And Jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/) article.




For example, you can use the `exponential_backoff` policy with default values or with custom values, as shown:
    
    
    from snowflake.connector.backoff_policies import exponential_backoff
    
    # correct, no required arguments
    snowflake.connector.connect(
    backoff_policy=exponential_backoff()
    )
    
    # correct, parameters are customizable
    snowflake.connector.connect(
    backoff_policy=exponential_backoff(
        factor=5,
        base=10,
        cap=60,
        enable_jitter=False
      )
    )
    

Copy

You can also create your own backoff policy generator functions, similar to the following that defines the `my_backoff_policy` generator function:
    
    
    def my_backoff_policy() -> int:
      while True:
        # yield the desired backoff duration
    

Copy

You then set the `backoff_policy` connection parameter to the name of your generator function as follows:
    
    
    snowflake.connector.connect(
      backoff_policy=constant_backoff
    )
    

Copy

## OCSP¶

When the driver connects, Snowflake sends a certificate to confirm that the connection is to Snowflake rather than to a host that is impersonating Snowflake. The driver sends that certificate to an OCSP (Online Certificate Status Protocol) server to verify that the certificate has not been revoked.

If the driver cannot reach the OCSP server to verify the certificate, the driver can [“fail open” or “fail closed”](../../user-guide/ocsp.html#label-ocsp-fail-open-or-fail-close).

### Choosing fail-open or fail-close mode¶

Versions of the Snowflake Connector for Python prior to 1.8.0 default to fail-close mode. Versions 1.8.0 and later default to fail-open. You can override the default behavior by setting the optional connection parameter `ocsp_fail_open` when calling the connect() method. For example:
    
    
    con = snowflake.connector.connect(
        account=<account_identifier>,
        user=<user>,
        ...,
        ocsp_fail_open=False,
        ...);
    

Copy

### Verifying the OCSP connector or driver version¶

The driver or connector version and its configuration both determine the OCSP behavior. For more information about the driver or connector version, their configuration, and OCSP behavior, see [OCSP Configuration](../../user-guide/ocsp).

### Caching OCSP responses¶

To ensure all communications are secure, the Snowflake Connector for Python uses the HTTPS protocol to connect to Snowflake, as well as to connect to all other services (e.g. Amazon S3 for staging data files and Okta for federated authentication). In addition to the regular HTTPS protocol, the connector also checks the TLS/SSL certificate revocation status on each connection via OCSP (Online Certificate Status Protocol) and aborts the connection if it finds the certificate is revoked or the OCSP status is not reliable.

Because each Snowflake connection triggers up to three round trips with the OCSP server, multiple levels of cache for OCSP responses have been introduced to reduce the network overhead added to the connection:

  * Memory cache, which persists for the life of the process.

  * File cache, which persists until the cache directory (e.g. `~/.cache/snowflake`) is purged.

  * OCSP response server cache.




Caching also addresses availability issues for OCSP servers (i.e. in the event the actual OCSP server is down). As long as the cache is valid, the connector can still validate the certificate revocation status.

If none of the cache layers contain the OCSP response, the client attempts to fetch the validation status directly from the CA’s OCSP server.

#### Modifying the OCSP response file cache location¶

By default, the file cache is enabled in the following locations, so no additional configuration tasks are required:

Linux:
    

`~/.cache/snowflake/ocsp_response_cache.json`

macOS:
    

`~/Library/Caches/Snowflake/ocsp_response_cache.json`

Windows:
    

`%USERPROFILE%\AppData\Local\Snowflake\Caches\ocsp_response_cache.json`

However, if you want to specify a different location and/or file name for the OCSP response cache file, the `connect` method accepts the `ocsp_response_cache_filename` parameter, which specifies the path and name for the OCSP cache file in the form of a URI.

#### OCSP response cache server¶

Note

The OCSP response cache server is currently supported by the Snowflake Connector for Python 1.6.0 and higher.

The memory and file types of OCSP cache work well for applications connected to Snowflake using one of the clients Snowflake provides, with a persistent host. However, they don’t work in dynamically-provisioned environments such as AWS Lambda or Docker.

To address this situation, Snowflake provides a third level of caching: the OCSP response cache server. The OCSP response cache server fetches OCSP responses hourly from the CA’s OCSP servers and stores them for 24 hours. Clients can then request the validation status of a given Snowflake certificate from this server cache.

Important

If your server policy denies access to most or all external IP addresses and web sites, you must allow the cache server address to allow normal service operation. The cache server URL is `ocsp*.snowflakecomputing.com:80`.

If you need to disable the cache server for any reason, set the `SF_OCSP_RESPONSE_CACHE_SERVER_ENABLED` environment variable to `false`. Note that the value is case-sensitive and must be in lowercase.

## Running connectivity tests and diagnostics¶

Note

Running diagnostics for a connection requires the following:

  * Snowflake Connector for Python version 3.9.1 or newer.

  * Python version 3.9 (deprecated) or newer.




If you encounter connectivity issues, you can run diagnostics directly within the connector. Snowflake Support might also request this information to help you with connectivity issues.

The diagnostics collection uses the following [connection](python-connector-api.html#label-snowflake-connector-methods-connect) parameters:

  * `enable_connection_diag`: Whether to generate a diagnostic report.

  * `connection_diag_log_path`: Absolute path for the generated report.

  * `connection_diag_allowlist_path`: Absolute path to a JSON file containing the output of `SYSTEM$ALLOWLIST()` or `SYSTEM$ALLOWLIST_PRIVATELINK()`. Required only if the user defined in the connection does not have permission to run the system allowlist functions or if connecting to the account URL fails.




To configure a connection to generate diagnostics:

  1. Configure the connection parameters:

     * Set your Snowflake account credential parameters.

     * Set `enable_connection_diag=True` in your `connect` parameters.

     * If desired, change the location for the generated report by setting the `connection_diag_log_path` parameter.

For example:
    
    from snowflake import connector
    
    ctx = connector.connect(
            user=<user>,
            password=<password>,
            account=<account>,
            enable_connection_diag=True,
            connection_diag_log_path="<HOME>/diag-tests",
            )
    print('connected')
    

Copy

  2. Execute the code snippet.

  3. Review the diagnostic test output of the generated `SnowflakeConnectionTestReport.txt` file located in the specified log path.




You can review the report for any connectivity issues and discuss them with your network team. You can also provide the report to Snowflake Support for additional assistance.

On this page

  1. Verifying the network connection to Snowflake with SnowCD
  2. Importing the snowflake.connector module
  3. Setting session parameters
  4. Connecting using the default authenticator
  5. Connecting using the connections.toml file
  6. Setting a default connection
  7. Using single sign-on (SSO) for authentication
  8. Using multi-factor authentication (MFA)
  9. Using key-pair authentication and key-pair rotation
  10. Using a proxy server
  11. Connecting with OAuth
  12. Enable the OAuth 2.0 Authorization Code flow
  13. Enable the OAuth 2.0 Client Credentials flow
  14. Authenticating with workload identity federation (WIF)
  15. Authenticating with a programmatic access token (PAT)
  16. Managing connection timeouts
  17. Managing connection backoff policies for retries
  18. OCSP
  19. Choosing fail-open or fail-close mode
  20. Verifying the OCSP connector or driver version
  21. Caching OCSP responses
  22. Running connectivity tests and diagnostics



Related content

  1. [SnowCD (Connectivity Diagnostic Tool)](/developer-guide/python-connector/../../user-guide/snowcd)
  2. [snowflake.connector.connect method](/developer-guide/python-connector/python-connector-api#label-snowflake-connector-methods-connect)



Language: **English**

  * [English](/en/developer-guide/python-connector/python-connector-connect)
  * [Français](/fr/developer-guide/python-connector/python-connector-connect)
  * [Deutsch](/de/developer-guide/python-connector/python-connector-connect)
  * [日本語](/ja/developer-guide/python-connector/python-connector-connect)
  * [한국어](/ko/developer-guide/python-connector/python-connector-connect)
  * [Português](/pt/developer-guide/python-connector/python-connector-connect)

---
