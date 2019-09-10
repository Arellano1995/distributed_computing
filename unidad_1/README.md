
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

#Video 6 - https://youtu.be/_e4wNoTV3Gw
Byzantine Fault Tolerance  

This fault tolerance system is very useful, especially in distributed systems where there are a large number of components or nodes in the game, so when some of these nodes fail or are violated, algorithms such as: PoW (Job Test) are used. and PoS (Stake Test), these works with the logic of the Byzantine generals, that in a nutshell, each node receives an order, and, in turn, this node issues the same order to the other nodes, even if a node will fail and deliver a different result, the correct result can be determined, assuming that the result that appears most frequently is correct.

#7 SLIs SLOs and SLAs https://youtu.be/LKpIirL8f-I
Usually, we create a distributed system to improve the performance and reliability unlike a centralized system. SLIs, SLOs, and SLAs help us to measuring the reliability and performance of the system, if you don't measure how wll you're doing you'll never know wheter you've achied this goal or not.
SLAs can be interpreted by the user as a message that tells how the operation is. For example, how often do you check that the system is up? and, what does it mean to be up?. If you promise to fix a system failure within 22 minutes. The time you mentioned must be precise and reliable by the end user. 
Never promise that you will take less time to repair a system failure if you really can't.

# Video 8 Class project https://youtu.be/QyKK8lcpzVQ
Creating a chat 
A example of a distributed chat
Go to distribuitedchat.appspot.com
Login with your Google account
And you can look up the page and see how it works.
It looks easy than it is, the chat uses Google's app engine infrastructure.
The chat works through two parts. The client side, which uses HTML and Javascript code and the server side which uses Python.
In addition the information is stored in a database. The infrastructure also provides a channel termination which allows communication between the app engine and the chat messages.
Also, use user authentication, a search engine and the billing system.
An advantage of using the Google engine is that it keeps the system running. The disadvantage is that it has a cost.

However, if we do not want Google to be the means of login. Check the follow link.
distributedsystemscourse.com/dschat
This is the uWSGI version. By using socket you can transmit the messages from client to server. This version also has its advantages it fits a fixed cost, it's a very simple system. It's disadvantage, it doesn't have authentication and have a problem with scalability.


# Video 9 - https://youtu.be/SRsK-ZXTeZ0
Paxos simplified

The simplified Paxos algorithm is an adapted version of the Byzantine algorithm, in order to be tolerant of stop failures, the number of nodes that must ratify the operation must be (2f + 1), where `` f '' is the number of system failures, this is a 25% improvement over Byzantine, and Paxos maintains an instant failover.

# Video 10 - https://youtu.be/GX4595KeZyc
How Counterstrike Works (Time in Distributed Systems)

Uno de los grandes problemas que presenta el cómputo distribuido es el LAG, por ejemplo en el sistema distribuido más sencillo, donde la información va del PC al Servidor y después regresa, podemos apreciar un LAG importante, el cual aumenta de forma proporcional a la distancia existente entre el cliente y el servidor. Para solucionar este inconveniente se han desarrollado una serie de trucos, por ejemplo; la predicción de eventos, donde el servidor realiza una predicción de las instrucciones siguientes del cliente, si acierta el sistema funciona con mayor fluidez, de no ser así, el sistema rectifica la decisión. Otra forma de combatir el LAG es mediante la compensación del LAg, el servidor mantiene un buffer de la información anterior de los clientes.

# Video 11 Introduction to Blockchain Consensus Link: https://youtu.be/LFZDpF_A-BE

This video gives us a introduction to Blockchain.
Blockchain says that you don't need to understand the paxos algorithm or that it solves problems like the byzantine fault.Also, explains the bitcoin blockchain data structure, how to create blockchain in one computer and move it to another computer forming what its called a consensus.

# Video 12 - https://youtu.be/Jp7T9qtuRIE
What is a Blockchain?

It is a considerably simple data structure, in this the information is divided into blocks, the first of these blocks is assigned an empty header, a second block will be formed with the new data, the second block will be placed in the header a cryptographic hash of the first block, and so on. Thanks to the ease of recalculating and being almost impossible to violate a block without detecting it with the validation of the next block.

# Video 13 Bitcoin Blockchain Consensus https://youtu.be/f1ZJPEKeTEY
Consensus algorithms
Paxos
Raft
Practical Byzantine fault tolerance
Use one of this algorithms to make a consensus.
A problem would be if several computers left you on the road could not achieve consensus since they would not have the votes or worse, if they are in several bad computers and vote in arbitrary ways and stop your system in achieving consensus.
If this happens, it will be necessary to use a new consensus. Bitcoin needs an algorithm that is resistant to attacks.

Solving livelock
One solution to the problem of adding blocks and not causing livelock is by adding a timer, although it's not the most optimal solution. If it is long, the system will take longer to reach consensus. Long timers are bad because they slow us down but long timers are good because they decrease the number of forks.
Another problem that may arise is that there is a partition and it cannot communicate with the other blocks.
The other blocks will continue to add blocks just as the partition will add its own blocks, when the communication has been resumed, the changes will be added to the partition and the blocks that it has had will die.

Now, what happens if a computer cheats? Can you build a cheat-resistant timer?
You can use cryptography or trusted computing module.
