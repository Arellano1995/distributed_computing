# UNIDAD 2
## Introduction
Asynchronous programming is a type of parallel programming where multiple processes can be executed at the same time. Asynchronous programming has been growing thanks to its advantages, mainly being efficiency and speed.

## Multiple Threads
When using threads for the realization of an asynchronous system allows us to assign threads to different processes and to better use the time of use of the processor, it is important to mark the closing of the thread at the end of its task.

## Corutins with performance
Corutins are generalizations of subroutines. They are used for multiprocessing where a process voluntarily cedes control periodically or when it is idle to allow multiple applications to run simultaneously.
Corutins resemble generators, while generators produce data for iteration, corutins can also consume data.

##Asynchronous Programming
With Asynchronous Programming the OS is not envolved. Python introduced a new concurrency model named Asyncio. Asyncio is designed to use coroutines and futures to simplify asynchronous code and make it almost as readable as synchronous code as there are no callbacks.