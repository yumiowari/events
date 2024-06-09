--sqlacodegen --outfile mapeamento.py postgresql+psycopg2://postgres:1234@localhost:5432/ticketmaster
-- TABELAS --
CREATE TABLE classifications (
	id varchar(20) PRIMARY KEY NOT NULL,
	name varchar(50) NOT NULL,
	segmentid varchar(20) NOT NULL,
	segmentName varchar(50) NOT NULL	
);

CREATE TABLE venues (
	id varchar(20) PRIMARY KEY NOT NULL,
	name varchar(50) NOT NULL,
	url text,
	postalCode int NOT NULL,
	timezone varchar(20) NOT NULL,
	city varchar(20) NOT NULL,
	state varchar(20) NOT NULL,
	country varchar(30) NOT NULL,
	address varchar(50)
);

CREATE TABLE attractions (
	id varchar(20) PRIMARY KEY NOT NULL,
	name varchar(50) NOT NULL,
	url text,
	classificationsid varchar(20),
    CONSTRAINT fk_classifications FOREIGN KEY (classificationsid) REFERENCES classifications(id)
);

CREATE TABLE events (
	id varchar(20) PRIMARY KEY NOT NULL,
	name varchar(50) NOT NULL,
	url text,
	StartDateSale date,
	EndDateSale date,
	StartDateEvent date,
	timezone varchar(20),
	minPrice float,
	maxPrice float,
	promoter varchar(20),
	venueid varchar(20),
    classificationsid varchar(20),
	CONSTRAINT fk_venue FOREIGN KEY (venueid) REFERENCES Venues(id),
    CONSTRAINT fk_classifications FOREIGN KEY (classificationsid) REFERENCES classifications(id)
);

CREATE TABLE event_attraction(
	id varchar(40) PRIMARY KEY,
	eventid varchar(20) NOT NULL,
	attractionid varchar(20) NOT NULL,
	CONSTRAINT fk_event FOREIGN KEY (eventid) REFERENCES Events(id),
    CONSTRAINT fk_attraction FOREIGN KEY (attractionid) REFERENCES attractions(id)
);

CREATE TABLE venue_alias (
    alias varchar(50) PRIMARY KEY,
	venueid varchar(20) NOT NULL,
    CONSTRAINT fk_venue FOREIGN KEY (venueid) REFERENCES Venues(id)
);

CREATE TABLE market (
	id varchar(70) PRIMARY KEY,
    market varchar(50) NOT NULL,
	venueid varchar(20) NOT NULL,
    CONSTRAINT fk_venue FOREIGN KEY (venueid) REFERENCES Venues(id)
);

CREATE TABLE venue_image (
    image text PRIMARY KEY,
	venueid varchar(20) NOT NULL,
    CONSTRAINT fk_venue FOREIGN KEY (venueid) REFERENCES Venues(id)
);

CREATE TABLE event_image (
    image text PRIMARY KEY,
	eventid varchar(20) NOT NULL,
    CONSTRAINT fk_event FOREIGN KEY (eventid) REFERENCES Events(id)
);

CREATE TABLE attraction_image (
    image text PRIMARY KEY,
	attractionid varchar(20) NOT NULL,
    CONSTRAINT fk_attraction FOREIGN KEY (attractionid) REFERENCES attractions(id)
);


SELECT * FROM Venues;
SELECT * FROM Events;
SELECT * FROM Classifications;
SELECT * FROM Attractions;