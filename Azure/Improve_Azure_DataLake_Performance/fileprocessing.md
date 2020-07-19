## DataLake File Processing.

Extents are chunk of a file. 

* A big enough CSV file may have many extents
* Each extent is replicated 3 times for robustness & availibility. 
* More extents generate a higher chance of parallelism.
* A usql script is processed by the data lake as a batch job.
* units of compute used while processing a uSQL job is called *vertices*.
* Each vertex performs a particular task and works on a number of extents.
* The more extents you have, the more vertices you can use.


## Cost vs Speed

### What is a Vertex?

* Each vertex handles around 1 GB of data.
* Vertex is a VM with a dual core processor and 6 Gb of RAM.
* Microsoft reserves the right to change these specs at any time.
* Jobs reserve vertices to use while execution is in progress.
* Default number of vertices is 5, but can be increased to 250
* It is possible to request Microsoft to change the limit and jobs with 1000 vertices are not uncommon.

#### ADLAU - Azure Data Lake Analytics unit
