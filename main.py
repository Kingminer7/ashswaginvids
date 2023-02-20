def test():
  
  try:
    import json
      
    # Opening JSON file
    f = open('config.json')
      
    # returns JSON object as 
    # a dictionary
    data = json.load(f)

    import tweepy
    from random import choice
    from time import sleep

    consumer_key = data['consumer_key']
    consumer_secret = data['consumer_secret']
    access_token = data['access_token']
    access_token_secret = data['access_token_secret']
    bearer_token = data['bearer_token']

    delays=[86400000,43200000,21600000,10800000]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)

    tweets = ["Joining a server and trying to beat Minecraft with only Raw Beef" + "https://www.youtube.com/shorts/J3X3lBbukk0", "SECRET ZOMBIE APOCALYPSE LOL" + "https://www.youtube.com/watch?v=P_tvroB9zN8", "I took over an SMP where everyone has creative mode" + "https://www.youtube.com/shorts/c531rapbytc", "Giving up hope on a Youtuber Anarchy Server" + "https://www.youtube.com/shorts/ZnUPsMpFYLs", "How I Became God" + "https://www.youtube.com/watch?v=AVVQAU3lWZo", "Torturing Minecraft Youtubers" + "https://www.youtube.com/shorts/xULQOXAm0GQ", "I played fake Minecraft" + "https://www.youtube.com/shorts/IyXNsXwhMgg", "Why did a Viewer’s Mom invite me to this SMP Server?" + "https://www.youtube.com/watch?v=4F7URXhLNGc", "I beat minecraft using WHAT?! (i am lonely)" + "https://www.youtube.com/shorts/-0Yigp3UAMU", "I accidentally livestreamed on twitch…" + "https://www.youtube.com/shorts/8YjAu7gEbvc", "How I ruined this SMP with my sleep schedule" + "https://www.youtube.com/shorts/_fQjq_whLz8", "I Joined a Minecraft Deathswap SMP" + "https://www.youtube.com/shorts/wUf8baQeYyQ", "i'm in a TommyInnit video" + "https://www.youtube.com/shorts/FVuSaRqPVfc", "I reviewed sick viewer bases on my SMP" + "https://www.youtube.com/shorts/JVJQ38gmpWs", "I joined a viewer SMP and destroyed it's economy" + "https://www.youtube.com/shorts/vtrNi5uy-EQ", "Why I'm neutral on 1House SMP" + "https://www.youtube.com/shorts/QR9Vx7z9kwo", "I was invited to a cool Viewer SMP" + "https://www.youtube.com/shorts/pT-hqL5R91I", "my dogs turned vegan on 1House SMP" + "https://www.youtube.com/shorts/Ht9Ak8_ufVk", "I started my own SMP... big mistake" + "https://www.youtube.com/shorts/gtcfcwf3DTY", "I got dogs and lost on 1House SMP" + "https://www.youtube.com/shorts/xHPpGD58OVs", "I joined a cursed 1.17 Viewer SMP" + "https://www.youtube.com/shorts/CXQ55Xyvnwc", "I joined a Dream SMP CLONE and Escaped Prison" + "https://www.youtube.com/shorts/jBRBRZufxxo", "I got Creative Mode on an SMP and trolled a poor player's mother" + "https://www.youtube.com/shorts/mHWXupoIlWw", "I Joined a Youtuber ANARCHY SMP and did not have fun" + "https://www.youtube.com/shorts/y1GwhHSYjjw", "Making Feline enemies on the 1House SMP" + "https://www.youtube.com/shorts/NYCWOFzRJwE", "I got ambushed on a Youtuber Anarchy SMP" + "https://www.youtube.com/shorts/Dpx7imwEzsU", "Spreading bad opinions while rating a Viewer's SMP" + "https://www.youtube.com/shorts/H2nk3VrgH6c", "causing confusion on the 1house SMP" + "https://www.youtube.com/shorts/JF-hYf7Mm3Y", "Disrespecting graves on a Viewer's SMP" + "https://www.youtube.com/shorts/3BxBkMMu2bY", "I Joined a Viewer's SMP and secretly BEAT THE GAME" + "https://www.youtube.com/shorts/41bEaP6hShE", "I joined an SMP where 20 People HAVE to live in ONE HOUSE" + "https://www.youtube.com/shorts/G1oIUarqkgc", "How I got banned for destroying a viewer's SMP server" + "https://www.youtube.com/shorts/TaWftKc-0uA", "I went magma hunting on a viewer's SMP" + "https://www.youtube.com/shorts/9IzHEi3-i6Y", "How I got banned for ruining a viewer's SMP server..." + "https://www.youtube.com/shorts/pwvescagKSI", "How I raided a Capitalist Viewer SMP Server..." + "https://www.youtube.com/shorts/5PGOSdJNUqs", "the weird origin of my minecraft skin" + "https://www.youtube.com/shorts/ISuhvjb1Jmo", "How i stole potatoes from a viewer's SMP server" + "https://www.youtube.com/shorts/skznZjw2q2U", "how my internet connection RUINED a Viewer's SMP" + "https://www.youtube.com/shorts/Mi65pi5Pxpw", "I was bullied on my SMP" + "https://www.youtube.com/shorts/EAZDbiahRfQ", "I raided a Viewer's SMP and caused emotional damage to his pets" + "https://www.youtube.com/shorts/lI3lWxP2fXA", "how I made a religion on a Minecraft SMP Server..." + "https://www.youtube.com/shorts/8qWmvq9v3vQ", "How I obliterated a FANMADE Dream SMP Server..." + "https://www.youtube.com/shorts/VewadgjpUpM", "How I became the best Hypixel TNT Run player in the world..." + "https://www.youtube.com/shorts/iKy3W8zwHZs", "How I Raided a Viewer's SMP server and saved his Pets" + "https://www.youtube.com/shorts/CAd9pnYd8FU", "how I broke a Minecraft 2b2t CLONE anarchy SMP server..." + "https://www.youtube.com/shorts/tMGLmmxdEqo", "Technoblade's ENTIRE Dream SMP story in 1 MINUTE" + "https://www.youtube.com/shorts/pVUUdinK3wU", "EVERY Dream SMP character in ONE MINUTE" + "https://www.youtube.com/shorts/CUNUDzCBTLc", "10 REMOVED Minecraft Features in ONE MINUTE" + "https://www.youtube.com/shorts/YjS-Buugz14", "I got REVENGE on the Dream SMP CLONE..." + "https://www.youtube.com/shorts/aY3Hz-httG8", "Tommy's DEATH on the Dream SMP EXPLAINED in ONE MINUTE" + "https://www.youtube.com/shorts/CBnXI2CSCys", "technoblade's dream smp lore be like" + "https://www.youtube.com/shorts/rqLF4bz1sns", "The ENTIRE Dream SMP explained in 1 MINUTE" + "https://www.youtube.com/shorts/p7M7O9Xp_ME", "How BIG is the Dream SMP?" + "https://www.youtube.com/watch?v=q1tlPPz27d0", "Using Sun Tzu to Beat Minecraft" + "https://www.youtube.com/watch?v=vXb0Sz3N6u8", "How I ILLEGALLY Beat Minecraft On This Fan's SMP" + "https://www.youtube.com/watch?v=I3LnUoBNGrM", "I Found my 10 Year Old Minecraft Server" + "https://www.youtube.com/watch?v=o0axUeOf0do", "How I RUINED MrBeast's Charity Minecraft SMP" + "https://www.youtube.com/watch?v=-I-t_sRvgFE", "Why I Got Revived and Scammed This SMP Server" + "https://www.youtube.com/watch?v=y8PZYqVtvXI", "Challenging Myself to get good at Minecraft" + "https://www.youtube.com/watch?v=gRUgGWuGUcU", "How I Ruined The "Perfect" 1.18 Minecraft SMP Server" + "https://www.youtube.com/watch?v=hyyBf_3gDkw", "How I Ruined This Server with Communism" + "https://www.youtube.com/watch?v=2Vh68ZeGRnI", "This Button Puts You in a Random SMP" + "https://www.youtube.com/watch?v=CLLB2HgwMnY"]

    def tweet(): 
        # schedule the next call first
        api.update_status(choice(tweets))
        sleep(choice(delays))
        # then do your stuff

    tweet()
  except ValueError: 
    print("An error occurred. Restarting...")
    test()