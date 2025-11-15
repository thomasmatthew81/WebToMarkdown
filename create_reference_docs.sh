#!/bin/bash

# Exit immediately if any command returns a non-zero status
set -e

# --- CONFIGURATION ---

PROJECT_DIR="/Users/thomasmathew/Dev/WebToMarkdown"
OUTPUT_DIR="reference"
COMMIT_MSG="Auto-update: Generated new artifacts via web2llms"

# --- URL MAPPING (Bash 3.2 Compatible) ---
# Syntax: "URL | SUBDIRECTORY/FILENAME"
# Note: Use the pipe character '|' to separate the URL and the Filepath

URL_LIST=(
    # Top level
    "https://reference.langchain.com/python/deepagents/ | deepagents.md"

    # Integrations
    "https://reference.langchain.com/python/integrations/langchain_openai/ChatOpenAI/ | integrations/ChatOpenAI.md"
    "https://reference.langchain.com/python/integrations/langchain_openai/BaseChatOpenAI/ | integrations/BaseChatOpenAI.md"
    "https://reference.langchain.com/python/integrations/langchain_aws/ | integrations/langchain_aws.md"
    
    # LangChain (Library)
    "https://reference.langchain.com/python/langchain/agents/ | langchain/agents.md"
    "https://reference.langchain.com/python/langchain/middleware/ | langchain/middleware.md"
    "https://reference.langchain.com/python/langchain/messages/#langchain.messages | langchain/messages.md"
    "https://reference.langchain.com/python/langchain/tools/ | langchain/tools.md"
    
    # LangChain Core
    "https://reference.langchain.com/python/langchain_core/caches/ | langchain_core/caches.md"
    "https://reference.langchain.com/python/langchain_core/callbacks/ | langchain_core/callbacks.md"
    "https://reference.langchain.com/python/langchain_core/documents/ | langchain_core/documents.md"
    "https://reference.langchain.com/python/langchain_core/prompts/ | langchain_core/prompts.md"
    "https://reference.langchain.com/python/langchain_core/retrievers/ | langchain_core/retrievers.md"
    
    # LangGraph
    "https://reference.langchain.com/python/langgraph/graphs/ | langgraph/graphs.md"
    "https://reference.langchain.com/python/langgraph/func/ | langgraph/func.md"
    "https://reference.langchain.com/python/langgraph/pregel/ | langgraph/pregel.md"
    "https://reference.langchain.com/python/langgraph/checkpoints/ | langgraph/checkpoints.md"
    "https://reference.langchain.com/python/langgraph/store/ | langgraph/store.md"
    "https://reference.langchain.com/python/langgraph/cache/ | langgraph/cache.md"
    "https://reference.langchain.com/python/langgraph/types/ | langgraph/types.md"
    "https://reference.langchain.com/python/langgraph/runtime/ | langgraph/runtime.md"
    "https://reference.langchain.com/python/langgraph/config/ | langgraph/config.md"
    "https://reference.langchain.com/python/langgraph/errors/ | langgraph/errors.md"
    "https://reference.langchain.com/python/langgraph/constants/ | langgraph/constants.md"
    "https://reference.langchain.com/python/langgraph/channels/ | langgraph/channels.md"
    "https://reference.langchain.com/python/langgraph/agents/ | langgraph/agents.md"
    "https://reference.langchain.com/python/langgraph/supervisor/ | langgraph/supervisor.md"
)

# --- EXECUTION START ---

echo ">>> Starting Workflow..."

# 1. Change Directory
echo ">>> Moving to project directory: $PROJECT_DIR"
cd "$PROJECT_DIR"

# 2. Activate Venv
echo ">>> Activating Python virtual environment..."
source venv/bin/activate

# 3. Loop through the list and run the Python command
echo ">>> Processing ${#URL_LIST[@]} URLs..."

for item in "${URL_LIST[@]}"; do
    # Split the string by " | "
    # ${item%% | *} gets everything BEFORE the separator (The URL)
    # ${item##* | } gets everything AFTER the separator (The Path)
    
    url="${item%% | *}"
    relative_path="${item##* | }"
    
    # Combine with the main output directory
    full_output_path="$OUTPUT_DIR/$relative_path"
    
    # Get the directory part of the path
    target_dir=$(dirname "$full_output_path")
    
    # Ensure the specific subdirectory exists
    if [ ! -d "$target_dir" ]; then
        mkdir -p "$target_dir"
    fi
    
    echo " -> Processing: $url"
    echo "    Target: $full_output_path"
    
    # Run the python command
    python web2llms.py "$url" -o "$full_output_path"
done

# 4. Git Operations
echo ">>> Performing Git operations..."

# Add all changes
git add .

# Check if there are actually changes to commit
if ! git diff-index --quiet HEAD; then
    git commit -m "$COMMIT_MSG"
    
    echo ">>> Pushing to remote..."
    git push
    
    echo ">>> Success! Changes pushed."
else
    echo ">>> No changes detected. Skipping commit and push."
fi

echo ">>> Workflow complete."
