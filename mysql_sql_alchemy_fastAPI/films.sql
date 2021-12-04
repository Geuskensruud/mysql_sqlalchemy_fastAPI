/*code van de sql query (mysql ivm die had ik nog op de pc staan)*/
/*Schema naam*/
USE sakila;
/*Creeren van de view*/
create or replace view films as
/*Select statement welke de informatie van de acteurs uit alle tabellen bundelt*/
select 
	distinct 
    film_.id                    as id
    ,film_.naamActeurs          as naamActeurs
    ,film_.titel                as titel
    ,film_.descriptie           as descriptie
    ,film_.LeeftijdRestrictie   as LeeftijdRestrictie
    ,film_.genre                as genre
    ,ceiling(amount.amount)     as AantalKeerBekeken
    ,film_.tijd                 as tijd
    ,film_.length               as minuten
    ,ceiling(film_.rating)      as rating
    ,language.name              as taal
from (
    select
	    film.film_id
	    ,row_number() OVER (ORDER BY film.title) id
	    ,group_concat(
		    concat(
			    concat(
				    upper(
					    Substr(actor.first_name, 1, 1)),
				    Lower(
					    Substr(actor.first_name, 2, LENGTH(actor.first_name))),
				    ' ',
				    upper(
					    Substr(actor.last_name, 1, 1)),
				    Lower(
					    Substr(actor.last_name, 2, LENGTH(actor.last_name)))))) 'naamActeurs'
        ,replace(film.title, ' ', '_') titel
        ,cast(film.description as char) descriptie
        ,case film.rating
            when 'PG' then '8 and older'
            when 'G' then 'No restrictions'
            when 'NC-17' then '17 and older'
            when  'PG-13' then '13 and older'
            when 'R' then 'Children Under 17 Require Accompanying Parent'
            else null
        end 'LeeftijdRestrictie'
        ,category.name genre
        ,film.rental_rate 'rating'
        ,concat(
		    floor(film.length/60),'h ',MOD(film.length,60),'m') tijd
        ,film.length
        ,film.language_id
    from actor actor
    inner join film_actor film_actor 
	    on actor.actor_id = film_actor.actor_id
    inner join film film
        on film_actor.film_id = film.film_id
    inner join film_category film_category
        on  film.film_id = film_category.film_id
    inner join category category
        on film_category.category_id = category.category_id
    group by  film.film_id , category.name
    order by film.title asc) as film_
    inner join (
        select 
            sum(amount) as amount
            ,film_id
        from inventory inventory
        inner join rental rental
            on inventory.inventory_id = rental.inventory_id
        inner join payment payment
            on rental.rental_id = payment.rental_id
        group by film_id
    ) As amount
        on  film_.film_id = amount.film_id
    inner join language language
	    on film_.language_id = language.language_id;

