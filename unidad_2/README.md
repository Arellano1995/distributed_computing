# Asynchronous programming

## Table Of Contents
- [Asynchronous programming with python](#asynchronous-programming-with-python)
  - [Introduction](#Introduction)
  - [Multiple Threads](#Multiple-Threads)
  - [Corutins with performance](#Corutins-with-performance)
  - [Asynchronous Programming](#Asynchronous-Programming)
- [Async-io complete](#Async-io-complete)
  - [ Setting Up Your Environment](#Setting-Up-Your-Environment)
  - [The 10,000-Foot View of Async IO](#The-10,000-Foot-View-of-Async-IO)
    - [Where Does Async IO Fit In?](#Where-Does-Async-IO-Fit-In?)
    - [Async IO Explained](#Async-IO-Explained)
    - [Async IO Is Not Easy](#Async-IO-Is-Not-Easy)
  - [The asyncio Package and async/await](#The-asyncio-Package-and-async/await)
    - [The async/await Syntax and Native Coroutines](#The-async/await-Syntax-and-Native-Coroutines)
    - [The Rules of Async IO](#The-Rules-of-Async-IO)
  - [Async IO Design Patterns](#Async-IO-Design-Patterns)
    - [Chaining Coroutines](#Chaining-Coroutines)
    - [Using a Queue](#Using-a-Queue)
  - [Async IO’s Roots in Generators](#Async-IO’s-Roots-in-Generators)
    - [Other Features: async for and Async Generators + Comprehensions](#Other-Features-async-for-and-Async-Generators-+-Comprehensions)
    - [The Event Loop and asyncio.run()](#The-Event-Loop-and-asyncio.run())
  - [A Full Program: Asynchronous Requests](#A-Full-Program-Asynchronous-Requests)
  - [Async IO in Context](#Async-IO-in-Context)
    - [When and Why Is Async IO the Right Choice?](#When-and-Why-Is-Async-IO-the-Right-Choice?)
    - [Async IO It Is, but Which One?](#Async-IO-It-Is,-but-Which-One?)
  - [Odds and Ends](#Odds-and-Ends)
    - [Other Top-Level asyncio Functions](#Other-Top-Level-asyncio-Functions)
    - [The Precedence of await](#The-Precedence-of-await)
  - [Conclusion](#Conclusion)
  - [Resources](#Resources)
    - [Python Version Specifics](#Python-Version-Specifics)
    - [Articles](#Articles)
    - [Related PEPs](#Related-PEPs)
    - [Libraries That Work With async/await](#Libraries-That-Work-With-async/await)


# Asynchronous programming with python
## Introduction
Asynchronous programming is a type of parallel programming where multiple processes can be executed at the same time. Asynchronous programming has been growing thanks to its advantages, mainly being efficiency and speed.

## Multiple Threads
When using threads for the realization of an asynchronous system allows us to assign threads to different processes and to better use the time of use of the processor, it is important to mark the closing of the thread at the end of its task.

## Corutins with performance
Corutins are generalizations of subroutines. They are used for multiprocessing where a process voluntarily cedes control periodically or when it is idle to allow multiple applications to run simultaneously.
Corutins resemble generators, while generators produce data for iteration, corutins can also consume data.

## Asynchronous Programming
With Asynchronous Programming the OS is not envolved. Python introduced a new concurrency model named Asyncio. Asyncio is designed to use coroutines and futures to simplify asynchronous code and make it almost as readable as synchronous code as there are no callbacks.

# Async-io complete
## Setting Up Your Environment
This section of the course will require Python 3 and the configuration of a virtual environment and the AioHttp and AioFiles packages
### Basic Concepts

-Parallelism. It consists of performing multiple operations at the same time.
-Concurrence. Concurrence is when two tasks can begin, execute and complete overlapping time periods. (There is a saying that concurrence does not imply parallelism).

-Multiprocessing is a means to effect parallelism, and it entails spreading tasks over a computer’s central processing units (CPUs, or cores). Multiprocessing is well-suited for CPU-bound tasks: tightly bound for loops and mathematical computations usually fall into this category.

-Threading is a concurrent execution model whereby multiple threads take turns executing tasks.

### Where Does Async IO Fit In?
Over the last few years, a separate design has been more comprehensively built into CPython: Async IO. This works as a library to write concurrent code. However, Async IO does not use Threading, nor is it multiprocessing. It is not built on any of these.

### Async IO Explained
Async IO may seem contradictory and paradoxical. How can you provide concurrent code, if you use only one thread and a single CPU core?
Async IO allows the cycle of events of a program to communicate with multiple tasks, to allow each one to take turns at the OPTIMAL MOMENT.
Async IO entails long waiting periods in which the functions would be locked and allows other functions to be executed during that downtime.

### Async IO Is Not Easy
Be warned, the truth is that building durable multithreaded code can be hard and error-prone, async programming can be difficult too. But that’s not to say that async IO in Python is easy.

## The asyncio Package and async/await
Let’s explore Python’s implementation. Python’s asyncio package (introduced in Python 3.4) and its two keywords, async and await, serve different purposes but come together to help

### The async/await Syntax and Native Coroutines
#### Example1.py
The order of this output is the heart of async IO. Talking to each of the calls to count() is a single event loop, or coordinator. When each task reaches await asyncio.sleep(1). In contrast the synchronous version, time.sleep() and asyncio.sleep() may seem banal, they are used as stand-ins for any time-intensive processes that involve wait time. The benefit of awaiting something, including asyncio.sleep(), is that the surrounding function can temporarily cede control to another function that’s more readily able to do something immediately. In contrast, time.sleep() or any other blocking call is incompatible with asynchronous Python code.

### The Rules of Async IO
The syntax async def introduces either a native coroutine or an asynchronous generator. The expressions async with and async for are also valid. 
The keyword await passes function control back to the event loop. If Python encounters an await f() expression in the scope of g(), this is how await tells the event loop, “Suspend execution of g() until whatever I’m waiting on—the result of f()—is returned. In the meantime, go let something else run.”

async def g():
    //Pause here and come back to g() when f() is ready
    r = await f()
    return r
    
#### Example2.py
IO cuts down on wait time: given a coroutine makerandom() that keeps producing random integers in the range [0, 10], until one of them exceeds a threshold, you want to let multiple calls of this coroutine not need to wait for each other to complete in succession.

## Async IO Design Patterns
### Chaining Coroutines
#### Example3.py
A key feature of coroutines is that they can be chained together. This allows you to break programs into smaller, manageable, recyclable coroutines.

part1() sleeps for a variable amount of time, and part2() begins working with the results as they become available. In this setup, the runtime of main() will be equal to the maximum runtime of the tasks that it gathers together and schedules.

### Using a Queue
The asyncio package provides queue classes that are designed to be similar to classes of the queue module. There is an alternative structure that can also work with async IO: a number of producers, which are not associated with each other, add items to a queue. In this design, there is no chaining of any individual consumer to a producer. It takes an individual producer or consumer a variable amount of time to put and extract items from the queue, respectively.
#### queue.py
The challenging part of this workflow is that there needs to be a signal to the consumers that production is done. Otherwise, await q.get() will hang indefinitely.

The first few coroutines are helper functions that return a random string, a fractional-second performance counter, and a random integer.
