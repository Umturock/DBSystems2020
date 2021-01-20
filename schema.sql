drop table synergy;
drop table champion;
drop table account;
drop table attributes;

CREATE TABLE IF NOT EXISTS champion (
    ID      SERIAL     PRIMARY KEY,
    name    VARCHAR(30) ,
    rank    INTEGER     ,
    level   INTEGER     ,
    star    INTEGER     ,
    siglevel    INTEGER ,
    account VARCHAR(50)
);
CREATE TABLE IF NOT EXISTS account (
    ID              VARCHAR(50) PRIMARY KEY,
    password        VARCHAR     ,
    email           VARCHAR(50) ,
    accounttitle    VARCHAR(50) ,
    accountlevel    INTEGER 
);
CREATE TABLE IF NOT EXISTS synergy (
    ID          SERIAL PRIMARY KEY,
    type        INTEGER ,
    rootchamp   INTEGER ,
    targetchamp INTEGER ,
    effect      text
);
CREATE TABLE IF NOT EXISTS attributes (
    champID     INTEGER ,
    rating      INTEGER ,
    health      INTEGER ,
    attack      INTEGER ,
    critrate    INTEGER ,
    critdmg     INTEGER ,
    armorpen    INTEGER ,
    blockpen    INTEGER ,
    critresist  INTEGER ,
    armor       INTEGER ,
    block       INTEGER 
);