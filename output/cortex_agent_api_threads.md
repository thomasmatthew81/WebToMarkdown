# Web Content Collection

> A collection of 1 web pages converted to Markdown format. Generated on 2025-09-28 14:44:38.

## Converted Web Pages

### Threads API | Snowflake Documentation

**Source:** https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-threads-rest-api

# Threads API¶

[](../../_images/logo-snowflake-black.png) [Preview Feature](../../release-notes/preview-features) — Open

Available to all accounts.

Use this API to create threads that are used to interact with Cortex Agents.

## Create thread¶

`POST /api/v2/cortex/threads`

Creates a new thread and returns the thread UUID.

### Request¶

#### Request headers¶

Header | Description  
---|---  
`Authorization` | (Required) Authorization token. For more information, see [Authentication](cortex-agents.html#label-chat-api-authenticate-example).  
`Content-Type` | (Required) application/json  
  
#### Request body¶

The request body can include the following field:

Field | Type | Description  
---|---|---  
`origin_application` | string | (Optional) Name of the application that created the thread. Allows grouping threads by application. Limited to 16 bytes.  
  
Example:
    
    
    {
      "origin_application": "my_app"
    }
    

Copy

### Response¶

Returns the thread UUID as a string.
    
    
    "1234567890"
    

Copy

## Describe thread¶

`GET /api/v2/cortex/threads/{id}`

Describes a thread and returns a batch of messages in that thread, based on the page_size and the last_message_id, in descending order of creation. This request is only successful if the thread ID belongs to the user.

### Request¶

#### Path parameters¶

Parameter | Type | Description  
---|---|---  
`id` | integer | (Required) UUID for the thread.  
  
#### Query parameters¶

Parameter | Type | Description  
---|---|---  
`page_size` | integer | (Optional) Number of messages to return (default: 20, max: 100).  
`last_message_id` | integer | (Optional) The ID of the last message received. Used to set the offset for next batch. Can be empty for the first batch of messages.  
  
#### Request headers¶

Header | Description  
---|---  
`Authorization` | (Required) Authorization token.  
`Content-Type` | (Required) application/json  
  
### Response¶

Returns a thread metadata object and an array of messages.

Field | Type | Description  
---|---|---  
metadata | object | Metadata for the thread, including the name, application that created the thread, and the time that it was created.  
`messages` | array | Array of message objects.  
  
#### metadata¶

Field | Type | Description  
---|---|---  
`thread_id` | integer | UUID for the thread.  
`thread_name` | string | Name of the thread.  
`origin_application` | string | The name of the application that created the thread.  
`created_on` | integer | Time when the thread was created (milliseconds since UNIX epoch).  
`updated_on` | integer | Time when the thread was last updated (milliseconds since UNIX epoch). An update includes adding any new messages to the thread.  
  
#### Messages¶

Field | Type | Description  
---|---|---  
`message_id` | integer | UUID for the message.  
`parent_id` | integer | UUID for the parent message.  
`created_on` | integer | Time when the message was created (milliseconds since UNIX epoch).  
`role` | string | The role that generated this message.  
`message_payload` | string | Message payload.  
`request_id` | string | Request ID for the original message.  
  
Example:
    
    
    {
      "metadata": {
        "thread_id": 1234567890,
        "thread_name": "Support Chat",
        "origin_application": "my_app",
        "created_on": 1717000000000,
        "updated_on": 1717000100000
      },
      "messages": [
        {
          "message_id": 1,
          "parent_id": null,
          "created_on": 1717000000000,
          "role": "user",
          "message_payload": "Hello, I need help.",
          "request_id": "req_001"
        },
        {
          "message_id": 2,
          "parent_id": 1,
          "created_on": 1717000001000,
          "role": "assistant",
          "message_payload": "How can I assist you?",
          "request_id": "req_002"
        }
      ]
    }
    

Copy

## Update thread¶

`POST /api/v2/cortex/threads/{id}`

Updates a thread.

### Request¶

#### Path parameters¶

Parameter | Type | Description  
---|---|---  
`id` | integer | (Required) UUID for the thread.  
  
#### Request headers¶

Header | Description  
---|---  
`Authorization` | (Required) Authorization token.  
`Content-Type` | (Required) application/json  
  
#### Request body¶

Field | Type | Description  
---|---|---  
`thread_name` | string | (Optional) Name of the thread.  
  
Example:
    
    
    {
      "thread_name": "New Thread Name"
    }
    

Copy

### Response¶

Returns the status of the thread update.
    
    
    {"status": "Thread xxxx successfully updated."}
    

Copy

## List threads¶

`GET /api/v2/cortex/threads`

Lists all threads belonging to the user.

### Request¶

#### Query parameters¶

Parameter | Type | Description  
---|---|---  
`origin_application` | string | (Optional) Filter the list of threads by this origin application. Without specifying this field, all threads are returned.  
  
#### Request headers¶

Header | Description  
---|---  
`Authorization` | (Required) Authorization token.  
`Content-Type` | (Required) application/json  
  
### Response¶

Returns an array of thread metadata objects.

#### Thread metadata¶

Field | Type | Description  
---|---|---  
`thread_id` | integer | UUID for the thread.  
`thread_name` | string | Name of the thread.  
`origin_application` | string | The name of the application that created the thread.  
`created_on` | integer | Time when the thread was created (milliseconds since UNIX epoch).  
`updated_on` | integer | Time when the thread was last updated (milliseconds since UNIX epoch). An update includes adding any new messages to the thread.  
  
Example:
    
    
    [
      {
        "thread_id": 1234567890,
        "thread_name": "Support Chat",
        "origin_application": "my_app",
        "created_on": 1717000000000,
        "updated_on": 1717000100000
      }
    ]
    

Copy

## Delete thread¶

`DELETE /api/v2/cortex/threads/{id}`

Deletes a thread and all the messages in that thread.

### Request¶

#### Path parameters¶

Parameter | Type | Description  
---|---|---  
`id` | integer | (Required) UUID for the thread.  
  
#### Request headers¶

Header | Description  
---|---  
`Authorization` | (Required) Authorization token.  
`Content-Type` | (Required) application/json  
  
### Response¶

Returns a success response if the thread is deleted.
    
    
    {
      "success": true
    }
    

Copy

On this page

  1. Create thread
  2. Request
  3. Response
  4. Describe thread
  5. Request
  6. Response
  7. Update thread
  8. Request
  9. Response
  10. List threads
  11. Request
  12. Response
  13. Delete thread
  14. Request
  15. Response



Related content

  1. [Cortex Agents](/user-guide/snowflake-cortex/cortex-agents)



Language: **English**

  * [English](/en/user-guide/snowflake-cortex/cortex-agents-threads-rest-api)
  * [Français](/fr/user-guide/snowflake-cortex/cortex-agents-threads-rest-api)
  * [Deutsch](/de/user-guide/snowflake-cortex/cortex-agents-threads-rest-api)
  * [日本語](/ja/user-guide/snowflake-cortex/cortex-agents-threads-rest-api)
  * [한국어](/ko/user-guide/snowflake-cortex/cortex-agents-threads-rest-api)
  * [Português](/pt/user-guide/snowflake-cortex/cortex-agents-threads-rest-api)

---
