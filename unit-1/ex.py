/*
5. Write a PL/SQL block which displays gross salary of employees as per
user input EID. (Consider EMP table with EID, EName, Deptno,
Deptname Gender, Age, BasicSal) with appropriate data types.)
Gross_Salary: BASICSAL + (DA + HRA + Medical) – PF. Rules: HRA =
15% of basic, DA = 50% of basic, Medical = Rs. 500, PF = 10% of
basic.

*/


set serveroutput on;
set verify off;
set feedback off;

declare
    id number;
    basic number;
    hra number;
    da number;
    medical number := 500;
    pf number;
    gross number;
begin
    id := &employee_id;

    select basicsal
    into basic
    from emp
    where eid = id;

    hra := basic * 0.15;
    da := basic * 0.50;
    pf := basic * 0.10;

    gross := basic + da + hra + medical - pf;

    dbms_output.put_line('basic salary = ' || basic);
    dbms_output.put_line('da = ' || da);
    dbms_output.put_line('hra = ' || hra);
    dbms_output.put_line('medical = ' || medical);
    dbms_output.put_line('pf = ' || pf);
    dbms_output.put_line('gross salary = ' || gross);

exception
    when no_data_found then
        dbms_output.put_line('employee id not found');
end;
/

set serveroutput off;
set verify on;
set feedback on;
