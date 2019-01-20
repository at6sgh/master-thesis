
LIBNAME TMP00001 "C:\Agata\SASlibrary\magisterka";

/* -------------------------------------------------------------------
   Kod wygenerowany przez zadanie SAS-a

   Wygenerowany dnia: wtorek, 28 sierpnia 2018 o godz. 21:19:13
   Przez zadanie: Regresja logistyczna  (2)

   Dane wejściowe: C:\Agata\SASlibrary\magisterka\dane_usa_final.sas7bdat
   Serwer:  Local
   ------------------------------------------------------------------- */
ODS GRAPHICS ON;

%_eg_conditional_dropds(WORK.SORTTempTableSorted);
/* -------------------------------------------------------------------
   Sortowanie zbioru C:\Agata\SASlibrary\magisterka\dane_usa_final.sas7bdat
   ------------------------------------------------------------------- */

PROC SQL;
	CREATE VIEW WORK.SORTTempTableSorted AS
		SELECT T.price_quantile, T.reviews_per_month, T.distance, T.accommodates, T.bathrooms, T.bedrooms, T.review_scores_rating, T.room_type, T.host_is_superhost, T.instant_bookable, T.cancellation_policy, T.accommodation_type, T.free_parking
		     , T.elevator, T.fitness
	FROM TMP00001.dane_usa_final as T
;
QUIT;
TITLE;
TITLE1 "Rezultaty regresji logistycznej";
FOOTNOTE;
FOOTNOTE1 "Wygenerowane przez System SAS (&_SASSERVERNAME, &SYSSCPL) dnia %TRIM(%QSYSFUNC(DATE(), NLDATE20.)) o godz. %TRIM(%SYSFUNC(TIME(), NLTIMAP20.))";
PROC LOGISTIC DATA=WORK.SORTTempTableSorted
		PLOTS(ONLY)=ALL
	;
	CLASS room_type 	(PARAM=REF ref='Entire home/apt') host_is_superhost 	(PARAM=REF ref='f') instant_bookable 	(PARAM=REF ref='f') cancellation_policy 	(PARAM=REF) accommodation_type 	(PARAM=REF ref='House') free_parking 	(PARAM=REF ref='No') elevator 	(PARAM=REF ref='No') fitness 	(PARAM=REF ref='No');
	MODEL price_quantile (ref='low-cost')=reviews_per_month distance accommodates bathrooms bedrooms review_scores_rating room_type host_is_superhost instant_bookable cancellation_policy accommodation_type free_parking elevator fitness	bathrooms*room_type	/
		SELECTION=NONE
		SLE=0.05
		SLS=0.05
		INCLUDE=0
		RSQUARE
		LINK=GLOGIT
		CLPARM=WALD
		ALPHA=0.05;
	UNITS distance=5 accommodates=2;
	ODDSRATIO bathrooms;
	ODDSRATIO room_type;

	;
RUN;
QUIT;

/* -------------------------------------------------------------------
   Koniec kodu zadania
   ------------------------------------------------------------------- */
RUN; QUIT;
%_eg_conditional_dropds(WORK.SORTTempTableSorted);
TITLE; FOOTNOTE;
ODS GRAPHICS OFF;


