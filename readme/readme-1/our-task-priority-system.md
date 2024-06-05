# Our Task Priority System

In our document processing system, we handle a large volume of tasks from multiple customers daily. To ensure that every customer's documents are processed in a timely manner, we have implemented a sophisticated priority system. This system dynamically adjusts priorities based on the number of pending tasks a customer has, ensuring fairness and efficiency. Let's dive into how this priority system works and when the task counter is reset.

**Key Concepts of the Priority System**

Our priority system revolves around a few key concepts:

1. **Pending Tasks**: This is a count of the documents a customer has submitted but are yet to be processed.
2. **Reset Interval**: The system periodically resets the pending tasks count to zero to ensure that no customer can monopolize the processing resources indefinitely.

**How the Priority is Determined**

Here's a step-by-step explanation of how the priority for processing tasks is determined:

1. **Tracking Pending Tasks**: Each customer has a count of pending tasks. This count helps us know how many documents are waiting to be processed for each customer.
2. **Resetting the Count**: To maintain fairness, we reset the pending tasks count to zero if a set amount of time (the reset interval) has passed since the last update. This interval is set to 1500 seconds (or 25 minutes) by default.
3. **Updating the Count**: If the reset interval hasn't passed, we reduce the pending tasks count by one each time we check, simulating the processing of a document.
4. **Setting Priorities**: The priority for processing tasks is based on the number of pending tasks. The fewer the pending tasks, the higher the priority, meaning those tasks will be processed sooner. We have specific thresholds to assign priority levels from 1 (highest priority) to 9 (lowest priority).

**Priority Levels**

The priority levels are assigned based on the pending tasks count as follows:

* **Priority 9**: If the pending tasks count is less than -20
* **Priority 8**: If the pending tasks count is less than -14
* **Priority 7**: If the pending tasks count is less than -12
* **Priority 6**: If the pending tasks count is less than -10
* **Priority 5**: If the pending tasks count is less than -8
* **Priority 4**: If the pending tasks count is less than -6
* **Priority 3**: If the pending tasks count is less than -4
* **Priority 2**: If the pending tasks count is less than -2
* **Priority 1**: If the pending tasks count is greater than or equal to -2

In simpler terms, as the number of pending tasks increases, the priority level lowers, meaning those tasks are processed later compared to others with higher priorities.

**When the Counter is Reset**

The pending tasks counter is reset to zero if more than the reset interval (1500 seconds) has passed since the last update. This mechanism ensures that no customer can accumulate pending tasks endlessly and hog the system resources. By periodically resetting the counter, we guarantee that every customer gets a fair share of processing time.
