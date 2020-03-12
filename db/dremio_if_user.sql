--Execute via system user
ALTER USER hr ACCOUNT UNLOCK;
ALTER USER hr IDENTIFIED BY hr;


CREATE USER bigdata_interface IDENTIFIED BY bigdata_interface
  DEFAULT TABLESPACE users
  TEMPORARY TABLESPACE temp
  QUOTA UNLIMITED ON users;
GRANT CONNECT, RESOURCE TO bigdata_interface;
GRANT UNLIMITED TABLESPACE TO bigdata_interface;

CREATE ROLE bigdata_interface_role;
GRANT SELECT, UDAPTE, INSERT, DELETE ON HR.COUNTRIES TO bigdata_interface_role;
GRANT SELECT, UDAPTE, INSERT, DELETE ON HR.EMPLOYEES TO bigdata_interface_role;
GRANT SELECT, UDAPTE, INSERT, DELETE ON HR.DEPARTMENTS TO bigdata_interface_role;

--TODO: For loop for all relevant tables: add grant select to role

grant bigdata_interface_role to bigdata_interface;

