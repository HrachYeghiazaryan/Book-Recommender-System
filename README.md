Before presentation update

In the end, we've changed our business problem for this moment. In the

beggining we thought of solving the problem that the user inputs a book

and finds other books similar to that, now we've changed the objective

a little bit and instead of taking a book as an input we take a text as an 

input and the algorithm finds the books that have description best matching

the input text.

In addition, we attach the link for our presentation: 

[Book Recommendation - Presentation](https://www.canva.com/design/DAFinm836II/qq9IYZwWNP7eP5u0h2NeHg/edit)

---

Milestone 4 update

1) The front-end and back-end engineers jointly deployed the dashboard.
2) The future plans are, if we will manage to do that during this course

update the search system so that it takes as input also books. Moreover,

we have ideas of integraton of chatGPT to generate descriptions for the

books. The updated system will work the way that it will take a book from

a much larger database, and suggest books like that from Zangak database.

From business point of view it will have a larger application scale.

---

Milestone 3 update

1) The front-end and back-end engineers jointly completed the implementation of the

dashboard. The storage for embeddings will be a directory where they will be saved, so

no additional work is needed for that step. The materials concerning dashboard can be

found in the directory dashboard. Additionally, we provide the link to figma:

[Figma](https://www.figma.com/file/dlQ5HRtSNXH7uoOOTzgPmv/Book-Recommendation?node-id=0-1&t=zrcmUyulWE04BKUb-0)

2) The data scientist and data analyst completed the codes for embedding extraction

from book description. The embedding extraction is complete, and the results are

available in the following google drive link:

[MA group project data - Google Drive](https://drive.google.com/drive/u/1/folders/1y6EMNzfI1V4WGgsLltSNStKR4yxrrCZN)

where zangak_embeddings must have been in data/embeddings.

A small note is that the example of translation results published during the milestone

have been replaced with full translated dataframe.

---

Milestone 2 update.

1) The front-end engineer completed the creation of the dashboard design. The design

can be found with the following path in github repo:

dashboard_design/design.pdf

Or alternatively it can be found by the following google drive link that is shared with

the instructor:  [diagrams.net](https://app.diagrams.net/#G1_A8RPBToDKyv-RBb4rSJMD06Td9Q8Xaq)

There are two options to go with, and we are inclined to go with option 2 (case 2 in the

diagram).

2) The data analyst and data scientist completed the codes for scraping the data from

zangak web page, cleaned the dataset and translated it. The source codes can be found

in directory src, and there are executable shell scripts written at the root directory for

convenience of use. An important note is that after each scraping a small manual work is

needed before running the second executable. The datasets are not typically pushed to

github, therefore, we provide a google drive link where:

zangak_scrape must have been in data/raw_scraped/

zangak_match must have been in data/book_text_matched/

zangak_translate must have been in data/translated/

The link: [MA group project data - Google Drive](https://drive.google.com/drive/u/1/folders/1y6EMNzfI1V4WGgsLltSNStKR4yxrrCZN)

IMPORTANT NOTE: Since the translation script is running long, the dataframe in

folder zangak_translate is just a sample to demonstrate what the result will look like.

The script is running on the whole dataset by the time of pushing current work to github,

and the sample folder will be replaced by the original one on google drive as the script

completes running.

---

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
