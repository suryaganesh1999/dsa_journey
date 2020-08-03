def check_matching(words, pattern):
    for word in words:
        if len(word)!=len(pattern):
            continue
        p_w={}
        w_p={}
        for i in range(len(pattern)):
            w=word[i]
            p=pattern[i]
            if w in w_p:
                if p!=w_p[w]:
                    break
            else:
                w_p[w]=p

            if p in p_w:
                if w!=p_w[p]:
                    break
            else:
                p_w[p]=w
        else:
            print(word)
            

words = ["leet", "abcd", "loot", "geek",
			"cool", "for", "peer", "dear", "seed",
			"meet", "noon", "otto", "mess", "loss"]
pattern = "moom"
check_matching(words, pattern)
