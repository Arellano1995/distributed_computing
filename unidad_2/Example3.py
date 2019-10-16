def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    try : 
        while True:
                # Search matches
                # yeild used to create coroutine
                name = (yield)
                if prefix in name:
                    print(name)
    except GeneratorExit:
                # finish the coroutine
            print("Closing coroutine!!") 
 
corou = print_name("Lannister")
corou.__next__()
#corou.send("James")
#corou.send("Giovanni Lannister")
corou.send("Dear James")
corou.send("Paolo Sakatori")
corou.send("Miguel Lannister")
corou.close()
