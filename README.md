Finding a book one will love reading can be difficult with so many options available.   
A recommendation system can make the process quicker and more effective. They can make   
reading more personalized and effective for users by introducing them to books they   
might not have otherwise come across. Our book recommender system is a form of   
recommender system where the user inputs a name of a book that he/she liked and   
the system provides books that are similar to the one that is in the input. This will   
help a user to see the suggested related books to the one the user wants to find.
Overall, our book recommendation system will help our users to save time, effort, and   
it will increase user satisfaction.

The general idea of our project is that first, we are going to scrape the descriptions   
of books from the Internet. As a source of our data, we decided to scrape data from   
Zangak’s webpage, where for each book there is a short description. After that we are   
going to obtain the NLP embeddings for each description. The method of obtaining the   
embeddings will be decided later, for now we have two ideas, the first one is that for   
each book we will obtain an embedding for the description text as a whole and the   
second idea is that for each book we will take embeddings of each of the words in the   
description and calculate their mean and consider it as the embedding of the   
description. Finally, when we have one vector for each book (the embeddings discussed 
above) we will make a dashboard where the user will input the book that he/she liked   
and then, the dashboard will take the embedding of the input book, calculate its dot   
product with the embeddings of all other books, and then the books for which the dot   
product will be the highest will be recommended.

