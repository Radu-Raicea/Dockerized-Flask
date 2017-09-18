-- -----------------------------------------------------------------------
-- This file is run when the postgres container is first created. It
-- creates 3 databases, one for each configuration.
-- -----------------------------------------------------------------------

CREATE DATABASE db_dev;
CREATE DATABASE db_prod;
CREATE DATABASE db_test;