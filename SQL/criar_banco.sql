--sqlacodegen --outfile mapeamento.py postgresql+psycopg2://postgres:1234@localhost:5432/ticketmaster

-- TABELAS --

CREATE TABLE classifications (
	id text PRIMARY KEY NOT NULL,
	name text NOT NULL,
	segmentid text NOT NULL,
	segmentName text NOT NULL	
);

CREATE TABLE venues (
	id text PRIMARY KEY NOT NULL,
	name text NOT NULL,
	url text,
	postalCode text NOT NULL,
	timezone text NOT NULL,
	city text NOT NULL,
	state text NOT NULL,
	country text NOT NULL,
	address text
);

CREATE TABLE attractions (
	id text PRIMARY KEY NOT NULL,
	name text NOT NULL,
	url text,
	classificationsid text,
    CONSTRAINT fk_classifications FOREIGN KEY (classificationsid) REFERENCES classifications(id)
);

CREATE TABLE events (
	id text PRIMARY KEY NOT NULL,
	name text NOT NULL,
	url text,
	StartDateSale date,
	EndDateSale date,
	StartDateEvent date,
	timezone text,
	minPrice float,
	maxPrice float,
	promoter text,
	venueid text,
    classificationsid text,
	CONSTRAINT fk_venue FOREIGN KEY (venueid) REFERENCES Venues(id),
    CONSTRAINT fk_classifications FOREIGN KEY (classificationsid) REFERENCES classifications(id)
);

CREATE TABLE event_attraction(
	id text PRIMARY KEY,
	eventid text,
	attractionid text,
	CONSTRAINT fk_event FOREIGN KEY (eventid) REFERENCES Events(id),
    CONSTRAINT fk_attraction FOREIGN KEY (attractionid) REFERENCES attractions(id)
);

CREATE TABLE venue_alias (
    alias text PRIMARY KEY,
	venueid text,
    CONSTRAINT fk_venue FOREIGN KEY (venueid) REFERENCES Venues(id)
);

CREATE TABLE market (
	id text PRIMARY KEY,
    market text,
	venueid text,
    CONSTRAINT fk_venue FOREIGN KEY (venueid) REFERENCES Venues(id)
);

CREATE TABLE venue_image (
    image text PRIMARY KEY,
	venueid text,
    CONSTRAINT fk_venue FOREIGN KEY (venueid) REFERENCES Venues(id)
);

CREATE TABLE event_image (
    image text PRIMARY KEY,
	eventid text,
    CONSTRAINT fk_event FOREIGN KEY (eventid) REFERENCES Events(id)
);

CREATE TABLE attraction_image (
    image text PRIMARY KEY,
	attractionid text,
    CONSTRAINT fk_attraction FOREIGN KEY (attractionid) REFERENCES attractions(id)
);