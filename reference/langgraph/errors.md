# Web Content Collection

> A collection of 1 web pages converted to Markdown format. Generated on 2025-11-15 15:03:33.

## Converted Web Pages

### Errors | LangChain Reference

**Source:** https://reference.langchain.com/python/langgraph/errors/

Skip to content 

[ ](https://github.com/langchain-ai/docs/tree/main/reference/python/docs/langgraph/errors.md "Edit this page")

# Errors

##  `` langgraph.errors ¶

###  `` EmptyChannelError ¶

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Raised when attempting to get the value of a channel that hasn't been updated for the first time yet.

###  `` GraphRecursionError ¶

Bases: `[RecursionError](https://docs.python.org/3/library/exceptions.html#RecursionError)`

Raised when the graph has exhausted the maximum number of steps.

This prevents infinite loops. To increase the maximum number of steps, run your graph with a config specifying a higher `recursion_limit`.

Troubleshooting guides:

  * [`GRAPH_RECURSION_LIMIT`](https://docs.langchain.com/oss/python/langgraph/GRAPH_RECURSION_LIMIT)



Examples:
    
    
    graph = builder.compile()
    graph.invoke(
        {"messages": [("user", "Hello, world!")]},
        # The config is the second positional argument
        {"recursion_limit": 1000},
    )
    

###  `` InvalidUpdateError ¶

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Raised when attempting to update a channel with an invalid set of updates.

Troubleshooting guides:

  * [`INVALID_CONCURRENT_GRAPH_UPDATE`](https://docs.langchain.com/oss/python/langgraph/INVALID_CONCURRENT_GRAPH_UPDATE)
  * [`INVALID_GRAPH_NODE_RETURN_VALUE`](https://docs.langchain.com/oss/python/langgraph/INVALID_GRAPH_NODE_RETURN_VALUE)



###  `` GraphInterrupt ¶

Bases: `GraphBubbleUp`

Raised when a subgraph is interrupted, suppressed by the root graph. Never raised directly, or surfaced to the user.

###  `` NodeInterrupt `deprecated` ¶

Bases: `GraphInterrupt`

Deprecated

NodeInterrupt is deprecated. Please use [`interrupt`](../types/#langgraph.types.interrupt "<code class="doc-symbol doc-symbol-heading doc-symbol-function"></code>            <span class="doc doc-object-name doc-function-name">interrupt</span>") instead.

Raised by a node to interrupt execution.

###  `` EmptyInputError ¶

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Raised when graph receives an empty input.

###  `` TaskNotFound ¶

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Raised when the executor is unable to find a task (for distributed mode).

Back to top

---
