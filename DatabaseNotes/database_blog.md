# Notes in SQL Insights

June 4, 2020

## What are Data Lakes?

source: https://www.youtube.com/watch?v=2NZxSz0hzE0

![DataLakes](https://entrigna.com/wp-content/uploads/2018/07/Data-Lake-Chart-4-1.png)

Relational databases are widely used for transaction data but data exists outside transactions that are required by applications through out any organization.

**Data Lakes** are used as raw data stores for applications, sensors etc. where different source systems can dump data which can then serve as source to reporting, analytics and data warehouse systems.

---

June 3, 2020

## Deadlocks in SQL

Deadlocks occurs when two queries are waiting for each other and neither can proceed.

For example:

* **Transaction1** has an exclusive lock on **Table1**
* **Transaction2** has an exclusive lock on **Table2**
* **Transaction1** requests for an exclusive lock on **Table2**, which it cannot acquire as **Transaction2** has not yet released the lock from **Table2**, so **Transaction1** enters into a waiting state.
* **Transaction2** meanwhile, while still having an exclusive lock on **Table2**, requests for a exclusive lock on **Table1** which has not yet been released from **Transaction1**

![Deadlock Visualised](https://dotnettutorials.net/wp-content/uploads/2018/12/c-users-pranaya-pictures-sql-server-deadlock-exam.png)

> This situation results into a deadlock when both queries cannot proceed and are permanently in a waiting state.

---

June 3, 2020

## Execution Plan

### Overview

> What is an Execution Plan?

* Compiled before execution
    * Not adaptable until 2017(limited use cases)
* Execution Plan is based on:
    * Statistics about data distribution
    * Sniffed values for parameters
* Queries maybe slow if the resources they are trying to access have locks on them. In which case, there is very little you can do with the execution plan. However, the **actual execution plan** may have details of Wait Statistics.
* 

---

June 2,2020

## Use cases for Cross Joins

### Overview

I have understood what a cross join results into but never came across real world use cases for using cross joins

This video https://www.youtube.com/watch?v=hrupP3jjG5Q is very helpful.

---

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

---

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
 - Look for warnings in Execution Plan
 - Look for estimated number of rows vs actual number of rows
 - Look for **row level security** policies under the policies folder(SQL Server 2016 and above)

 ### Conclusion

 Very insightful analysis. Important note is to study the execution plan closely for details.