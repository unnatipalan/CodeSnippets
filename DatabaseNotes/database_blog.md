# Notes in SQL Insights

June 2,2020

## Importance of updating Statistics

### Overview

It is important to realize the impact of updated statistics on a table that undergoes frequent changes.

This video https://youtu.be/gZOtiOfwZNg explains with helpful code samples.

### Notes to Self
- Always check if the statistics on a table are upto date.
- Incase it is not, then the query can reuse an out of date execution plan 
- Usually SQL Server uses the following thumb rule to update statistics on a table:
>     20% or 800 rows are changed then SQL Server.

June 2, 2020
## Execution Plan Analysis when Row Level Security is enabled on a table!

### Overview

This video
https://youtu.be/8Kc7fPpjc4E?list=PLoM-GGCV9ZrJ3ysEqMEHHN8piAR3AIF5G illustrates how simple execution plans for select may invoke functions that are bound by row level security policies on a table.

### Notes to self
 - Study the execution plans from right to left
 - Look for output references & list as columns
 - Look for predicates(filters) used
 - Look for Properties in SQL Execution plans and check if security policies have been enabled.
 - Look for **row level security** policies under the policies folder(SQL Server 2016 and above)

 ### Conclusion

 Very insightful analysis. Important note is to study the execution plan closely for details.