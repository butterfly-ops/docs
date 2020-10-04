# Introduction
Butterfly uses multi-layer database management. It's possible to use multiple databases at the same time. You can configure multiple databases and use it. Butterfly uses MySQL as the primary database.
All Butterfly related data is stored in MySQL but you can use the following database drivers: 

- [MySQL 5.6+](https://thebutterfly.io/docs/#/database-mysql)
- [ElasticSearch 7+](https://thebutterfly.io/docs/#/database-elastic-search)
- _MongoDB_
- _Redis_

When you check MySQL and other database implementations you will see that it's written to make developer comfortable whether you 
are using MySQL or ElasticSearch. We have built a system with same behaviours independent from which driver you use.

Why you should mess with Elastic Search complex JSON Queries if there is a better solution. You don't need anymore. Just give a shot to Butterfly 
implementations. 