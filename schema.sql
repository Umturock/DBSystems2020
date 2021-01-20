drop table synergy;
drop table attributes;
drop table champion;
drop table account;

CREATE TABLE IF NOT EXISTS account (
    ID              VARCHAR(50) PRIMARY KEY,
    password        VARCHAR     ,
    email           VARCHAR(50) ,
    accounttitle    VARCHAR(50) ,
    accountlevel    INTEGER 
);
CREATE TABLE IF NOT EXISTS champion (
    ID      SERIAL     PRIMARY KEY,
    name    VARCHAR(30) ,
    rank    INTEGER     ,
    level   INTEGER     ,
    star    INTEGER     ,
    siglevel    INTEGER ,
    account VARCHAR(50) ,
    FOREIGN KEY (account) REFERENCES account(ID)
);
CREATE TABLE IF NOT EXISTS synergy (
    ID          SERIAL PRIMARY KEY,
    type        INTEGER ,
    rootchamp   INTEGER ,
    targetchamp INTEGER ,
    effect      text    ,
    FOREIGN KEY (rootchamp) REFERENCES champion(ID),
    FOREIGN KEY (targetchamp) REFERENCES champion(ID)
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
    block       INTEGER ,
    FOREIGN KEY (champID) REFERENCES champion(ID)
);