This is the replication package of the work: 
### "Code Review Automation: Strengths and Weaknesses of the State of the Art".


## Resources
- `valid_instances.xlsx` : contains the valid instances inspected during the manual analysis and the respective labels.
- `discarded_instances.xlsx` : contains the instances discared during the manual analysis and the respective reason for the discard.
- `chatgpt_analysis.xlsx` : contains the instances used to evaluate the performances of ChatGpt-3 on the two considered code review automation tasks and its predictions.
- `statistical_analysis_instance_complexity.xlsx` : contains the results of the statistical analysis on the instances complexity.
- `code_comment_to_code_labels.xlsx`, `code_to_comment_labels.xlsx` : contain information, such as number of total istances, number of correct/wrong predictions, percentage of correct predictions, for each label used, for _code&comment-to-code_ and _code-to-comment_ task respectively.
- `chatgpt_analysis_code-to-comment_labels.xlsx`, `chatgpt_analysis_code&comment-to-code_labels.xlsx` : contain information showing how the success and failure instances of ChatGPT are spread in our taxonomies, for _code&comment-to-code_ and _code-to-comment_ task respectively.
- `code_complexity` : contains all the necessary to compute the code generation complexity based on AST-changes between the input code (code submitted for review) and the code to generate in order to implement the reviewer comment (code revised).
