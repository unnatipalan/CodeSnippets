## Introduction to Snowflake

---
Salient features of Snowflake:
- cloud native, no on-premise option
- separates storage and compute
- Storage keeps data in Immutable Blob Storage(Amazon S3, Azure Blob Storage)
- compute layer consists of ***warehouses***
- ***warehouses*** are analogous to VMs which do computation on data.

![](https://www.mssqltips.com/tutorialimages/9286_introduction-to-warehouses.001.png)
*Snowflake Architecture Diagram*

#### Cloud Services

Central application of Snowflake that manages resources like accounts, metadata, authentication and access control, transactions etc.

#### Warehouses

Elastic Virtual Machines responsible for Compute.

#### Data Storage

Hybrid columnar storage using micro-partitions.