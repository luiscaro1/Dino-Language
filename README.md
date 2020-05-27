

*by Luis F Caro, Joshua Matos and Brandon Fung*

### Dino Programming Language

Dino is a simple and light-weight programming language focused on the English syntax. It uses real-life sentences to perform basic arithmetic and assignment operations. With all the upcoming technologies, we believe the industry has shied away from simplicity. We want to engage all audiences especially children and people with mental disabilities. Programming can be hard to grasp at first but it doesn’t have to be. Dino can be learned in an hour, we believe this empowers young developers and inspires them to tackle larger languages in the future. Dino doesn’t bring anything new to the industry, it makes the common case fast and allows younger generations to acquire exposure. Invest in the youth of today and they’ll be the pioneers of tomorrow.

### Get Started

Dino, in its simplicity, is based on English sentences that form a paragraph. Based on what type of sentences are formed, the program collects the data from the paragraph and stored in an internal object-oriented data structure. There are different types of sentences and these are expressions, definitions, questions and modifications.

## Sentence
  * **Expressions**
    Expressions represent mathematical values by adding, subtracting, multiplying and dividing.
        I.e. 2 times 3. or  2 plus 4.
  * **Definitions**
    Definitions have the ability to create objects that can store any type of information from values to list of values.
        I.e. Luis is a person.  or   Animals are pigs, cats, dogs.
  * **Questions**
  Questions are used to access any object’s information.
        I.e. What is the height of Luis? What are Animals? or  What is the length of Animals?
  * **Modifications**
  Modifications are sentences that can modify or even create an attribute for an object.
        I.e. The height of Luis is 176.  or  The model of Car is Fiesta.

## **Objects**
Objects in Dino can be thought of as a list with the first element pointing to its type. These objects store attributes with their respected values and can be accessed anytime using questions or modifications.

**Object visualization:**
	Some Object => [ ‘type’:Name , ‘attr1’:value1 , ‘attr2’:value2, … ]

* **Familiar grammar**
	Dino language can be very familiar if you know english since its sentences are made up by using 90% english words. By forming english sentences, Dino can be a good experience for kids who want to learn coding.
	**Example:** 
	[Dino] Math is 14 plsu 12 divided by 2. What is Math?
	Output:
	20

	(note: order of operations will follow PEMDAS automatically, no parenthesis needed)
