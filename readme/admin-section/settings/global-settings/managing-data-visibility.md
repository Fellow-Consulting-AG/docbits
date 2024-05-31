# Managing Data Visibility

## Introduction Effectively managing dashboard data loading options is critical to achieving a balance between instant data availability and system performance.&#x20;

### Here are some best practices and strategies to achieve this.

### Data Loading Options&#x20;

### **Real-time Data Refresh**

**Description:**&#x20;

* Refreshes data on the dashboard in real-time as soon as changes occur in the data source.

**Usage:**&#x20;

* Ideal for dashboards that display critical and time-sensitive information, e.g. monitoring or financial dashboards.

**Impact on System Performance:**&#x20;

* Can impact system performance, especially with large amounts of data or many concurrent users.&#x20;

### **Periodic Refresh**

**Description:**&#x20;

* Refreshes data at set intervals (e.g. every 5 minutes, hourly, daily).&#x20;

**Use:**&#x20;

* Suitable for less critical applications where real-time data is not required, e.g. reporting or analytics dashboards.&#x20;

**Impact on system performance:**&#x20;

* Less burdensome than real-time refreshes, but can still consume significant resources at frequent intervals.&#x20;

### On-demand refresh

**Description:**&#x20;

* Refreshes data only when the user requests it (e.g. by clicking refresh button).&#x20;

**Usage:**&#x20;

* Useful for dashboards that occasionally need updated data and for users who want to manually trigger specific updates.&#x20;

**Impact on system performance:**&#x20;

* Low system burden as data is only retrieved when needed.&#x20;

### Lazy loading

**Description:**&#x20;

* Loads data only when it is actually needed (e.g. when a user views a specific widget).&#x20;

**Use:**&#x20;

* Effective for dashboards with many widgets where not all data is needed immediately.&#x20;

**Impact on system performance:**&#x20;

* Reduces initial load times and saves resources, but can cause delays when data is reloaded.&#x20;

### Strategies for optimizing data loading options&#x20;

### Data Prioritization

**Important Data First:**&#x20;

* Load the most critical and frequently used data first.

**Background Loading:**&#x20;

* Less important data can be loaded in the background while the user interacts with the dashboard.&#x20;

### Caching

**Data Caching:**&#x20;

* Store frequently used data locally to reduce loading time and reduce the load on the data source.

**Invalidation:**&#x20;

* Implement a cache invalidation strategy to ensure users are not working with stale data.&#x20;

### Data Compression

**Compressed Data Transfer:**&#x20;

* Reduce the amount of data being transferred by using compression techniques.

**Decompression:**&#x20;

* Ensure that the decompressed data is processed quickly and efficiently.&#x20;

### Asynchronous Data Processing

**Asynchronous Fetches:**&#x20;

* Use asynchronous data fetches to avoid blocking the UI while data is loading.

**Notifications:**&#x20;

* Inform users about loading progress or when data is fully loaded.&#x20;

### Data Partitioning

**Large Data Segmentation:**&#x20;

* Divide large data sets into smaller, manageable chunks that can be loaded and viewed independently.

**Layered Data Access:**&#x20;

* Allow users to navigate through layers of data instead of loading all the data at once.



Effectively managing dashboard data loading options at DocBits is critical to balancing instant data availability and system performance. Implementing and optimizing strategies such as real-time refresh, periodic refresh, on-demand refresh, lazy loading, caching, data compression, asynchronous data processing, and data partitioning can significantly improve user experience and optimize system performance.

