Both threads take almost the same time to process.
- Note: It takes a little longer for a CPU bound ops running off the CPU to execute on multi as compared to a single thread.
In the multithread version the GIL - Global Interpreter Lock - prevents the CPU bound threads from executing in Parallel.
GIL however does not have impact on the performance of I/O bound multi-threaded programs as the lock is shared between threads while they are still waiting for I/O.