--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.0

-- Started on 2024-06-03 23:34:27

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE IF EXISTS db_clientes;
--
-- TOC entry 4783 (class 1262 OID 17600)
-- Name: db_clientes; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE "db_clientes" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';

ALTER DATABASE db_clientes OWNER TO postgres;

--\connect db_clientes
\connect -reuse-previous=on "dbname='db_clientes'"

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 17601)
-- Name: clientes_temp; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.clientes_temp (
    id integer NOT NULL,
    cpf character varying(18),
    private integer,
    incompleto integer,
    data_da_ultima_compra date,
    ticket_medio character varying(18),
    ticket_da_ultima_compra character varying(18),
    loja_mais_frequente character varying(18),
    loja_da_ultima_compra character varying(18)
);


ALTER TABLE public.clientes_temp OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 17604)
-- Name: clientes_temp_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.clientes_temp ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.clientes_temp_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 4776 (class 0 OID 17601)
-- Dependencies: 215
-- Data for Name: clientes_temp; Type: TABLE DATA; Schema: public; Owner: postgres
--
--dados inseridos
--
-- TOC entry 4784 (class 0 OID 0)
-- Dependencies: 216
-- Name: clientes_temp_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

--SELECT pg_catalog.setval('public.clientes_temp_id_seq', 49998, true);
SELECT pg_catalog.setval('public.clientes_temp_id_seq', null, true);


-- Completed on 2024-06-03 23:34:28

--
-- PostgreSQL database dump complete
--

