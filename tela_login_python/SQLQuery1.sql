select * from informacoesLogin
drop table informacoesLogin 
create table informacoesLogin(
usuario int identity(1,1) ,
nome varchar(50),
idade int,
senha varchar(10),
senhaCod varchar(10),
primary key(usuario)
)