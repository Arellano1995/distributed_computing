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
    - [Other Features: async for and Async Generators + Comprehensions](#Other-Features:-async-for-and-Async-Generators-+-Comprehensions)
    - [The Event Loop and asyncio.run()](#The-Event-Loop-and-asyncio.run())
  - [A Full Program: Asynchronous Requests](#A-Full-Program:-Asynchronous-Requests)
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

## The 10,000-Foot View of Async IO
### Where Does Async IO Fit In?
### Async IO Explained
### Async IO Is Not Easy


