from github import Github
from langchain.document_loaders import GitHubIssuesLoader
import os

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
REPOSITORY = os.environ.get("REPOSITORY")
g = Github(ACCESS_TOKEN)
repo = g.get_repo(REPOSITORY)

# Set this parameter to True if you want to print the patch, otherwise set it to False.
print_patch = False

loader = GitHubIssuesLoader(
    repo=REPOSITORY,
    access_token=ACCESS_TOKEN,
)

docs = loader.load()
for i, doc in enumerate(docs):
    title = doc.metadata.get("title", "")
    label = doc.metadata.get("label", "")
    number = doc.metadata.get("number", "")
    creator = doc.metadata.get("creator", "")

    print(f"Document {i + 1} - Title: {title}")
    print(f"Number: {number}")
    print(f"Creator: {creator}")

    print(doc.page_content)

    # Check if print_patch is True and there is a pull request
    if print_patch:
        pull_request = repo.get_pull(number)
        files = pull_request.get_files()

        for file in files:
            patch = file.patch
            print(f"File: {file.filename}\nPatch:\n{patch}\n")

    print("-" * 40)
