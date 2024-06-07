-- CLASSIFICATIONS
CREATE INDEX classifications_name_index
ON classifications USING btree (name);

CREATE INDEX classifications_segmentName_index
ON classifications USING btree (segmentName);

-- VENUES
CREATE INDEX venues_name_index
ON venues USING btree (name);

CREATE INDEX venues_postalCode_index
ON venues USING btree (postalCode);

CREATE INDEX venues_zipCode_index
ON venues USING btree (city, state, country, address);

-- ATTRACTIONS
CREATE INDEX attractions_name_index
ON attractions USING btree (name);

-- EVENTS
CREATE INDEX events_name_index
ON events USING btree (name);

CREATE INDEX events_sale_period_index
ON events USING btree (startDateSale, endDateSale);

CREATE INDEX events_startDateEvent_index
ON events USING btree (startDateEvent);

CREATE INDEX events_price_range_index
ON events USING btree (minPrice, maxPrice);

-- MARKET
CREATE INDEX market_name_index
ON market USING btree (market);
