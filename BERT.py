body = '''
So if there’s anything we can say with confidence about Emil Cioran so far it’s that he was a defender of what he saw as
intellectual honesty at the highest level. He wasn’t the guy to be scared of bringing up some of the darkest recesses of
the human condition...he didn’t shy away from writing about personal failures and shortcomings...he even joked and laughed 
about this ridiculous plight of being a human being the entire way through his life and and he did all of this beginning 
from a place... where he took it as practically a self-evident fact...that there really isn’t ANY objective meaning to 
ANYTHING in the universe whatsoever.

We are born, and we are quickly smacked across the face with the cold, hard reality that we are a creature that seeks out 
meaning in the universe, and no matter how hard we look...no matter what method we try to utilize...no such meaning 
actually exists out there in the universe to be discovered. 

Now, maybe you’ll remember...the first episode we did on Cioran... I said that 95% of you probably wouldn’t agree with 
this depiction of reality. But no doubt 5% of you probably did. 5% of you out there are feeling pretty philosophically 
vindicated right now: Ayy it’s Cioran. Welcome to the club. Where you been all my meaningless life? 

But something that’s important to consider is that...knowing this audience...and the level you people CLEARLY think 
about things...it’s NOT JUST the 5%...dare I say almost everybody LISTENING to this...100% of you have considered at 
some point in your life this idea... that ultimately...isn’t it possible that nothing really matters at all...nothing 
really has ANY meaning...at least on the level of the universe.

We’ve all ENTERTAINED this worldview before. We’ve all no doubt at some point been faced with the question what if there 
IS no objective moral POINT to enduring the inherent suffering of existence? More than that...why DO anything...if nothing
ultimately MEANS anything, on the level of the universe? Why not sit around and just do nothing? Why be Sysiphus pushing 
the rock up the hill everyday... just to construct something that is ultimately going to be sucked into a black hole one day? See if your expectation was to ask these questions and get a text back from the universe with some clear, solid answers to them...then this is going to be a pretty uncomfortable place to sit and continue on with life. We know this is the case...and this has been Cioran’s entire point from the start: 

The history of human thought has been filled with these stories, religions, philosophical doctrines, gurus, self-help 
books...what we’ve referred to so far as sort of, optimism cults...stories that we delude ourselves with to get away 
from this uncomfortable reality that everything is meaningless. 

        '''
from summarizer import Summarizer, TransformerSummarizer
bert_model = Summarizer()
bert_summary = ''.join(bert_model(body, min_length=60))
print(bert_summary)

