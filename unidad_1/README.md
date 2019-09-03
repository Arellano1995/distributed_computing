#Summary of the videos

#1st video https://youtu.be/7VbL89mKK3M
The first video is an introduction to distributed computing, it gives us the definition of distributed computing and its advantages,
and the difference between centralized and distributed.
Pros of centralized computing:
Because it's just one computer it's easy to use and therefore fast.
Pros of distribuited computing:
-Can support many user(computers)
-Tolerate failures

#2nd video - https://youtu.be/pMQzLVK39Kk
10 reasons to use a distributed system.
-At the request of the boss.
-It's fun, because it makes work easier.
-It is necessary to be able to access information where, when necessary, it is no longer a luxury.
-For legal, privacy and political reasons, sometimes you must have a backup of the information, or avoid being within the reach of a physical team, which is easily vulnerable.
-For times of activity, the server will always be active even if the offices are not open.

#3rd video - https://youtu.be/BkSdD5VtyRM
How to learn distributed systems?
It is important to understand that distributed systems are an experimental science and not just something theoretical.That is why current distributed systems are born and from debugging and modifying systems and modifications.

Systems fail! That is why our system must have fault tolerance.

One of the great challenges in distributed computing is to get computers to communicate with each other correctly. for which two models have been developed, the shared memory model and the message passing model.

#4th video - https://youtu.be/C8nLSLs0fNw 
What could go wrong?
If you want to develop a system with fault tolerance, prime should know what are the possible failures.
Some of these failures are:
- Crash.
- Crashloop.
- Data Corruption.
- Server Down.
- Query of Death.
- Broken Dependency.
- Cystiner Reported Failure.
- Data Loss.
- Time Travel.
- 0wned
- Natural Disaster
- Cause Infrastructure failure.
- Police Raid.
- Operator Error.
- RunaWay Automation.
- Certificate Expires.
- Fail to Pay Bills.
- Non-Linear Rsponse to Change.
- Performance Cliffs.
- VIP.
- DoS Attack.
- Cascading Failure.
- Heisenbug.
- Neon-Hermetic Builds.
- Firewalls.
- Kernel Memory Leak.
- Hash Collision.
- Incorrect Algorithm.

Some of these failures are anecdotal in terms of frequency of occurrence, while others occur on a regular basis and therefore we must consent to our efforts to solve them in our system.

#5 The many types of fail https://youtu.be/MnYlwjuGcg8
How to Divide many failures into categories
- Network failures
- Backup fail most common failure
- Security warranty like criptography
- Two things you it can gave you
1. A warranty that the network will always get to you and 2. Performance warranties problems.
- Loss of connectivity
Consider a network where a node is connected to a different node. If a node goes down, we loss connectivity between one sub graph and the other sub graph. The components of system can run but can't communicate each other. You can create a code where when Communication resumes, the processes they had may somehow, weave the system back again it's called "tolerating a consistent state".

