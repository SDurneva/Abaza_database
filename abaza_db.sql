create table if not exists Example (
	id			integer primary key autoincrement not null,
	text 		          text,
	translation       text,
  obtaining_method  text,
  datetime          datetime,
  subject           text,
  comment           text,
  informantid       integer not null references Informant(id),
  interviewerid     integer not null references Interviewer(id)
);

create table if not exists Alternatives (
	example1id 		integer not null references Example(id),
  example2id    integer not null references Example(id)
);

create table if not exists Informant (
	id 			                 integer primary key autoincrement not null,
	full_name	               text,
	gender	                 text,
	year_of_birth	           datetime,
	birthplace	             text,
	education	               text,
	occupation	             text,
	native_language	         text,
	speaks_since_childhood   text,
	fathers_birthplace	     text,
	fathers_native_language  text,
	mothers_birthplace	     text,
	mothers_native_language	 text,
	mother_speaks_Abaza	     text,
	fam_lang_childh	         text,
	fam_lang_now	           text,
	speaks_Circaccian	       text,
	speaks_Circ_freq         text
);

create table if not exists Interviewer (
	id			      integer primary key autoincrement not null,
	full_name 		text,
	academic_stat	text,
	email		      text,
	university		text
);

create table if not exists Advisor (
	interviewerid			integer not null references Interviewer(id),
	advisorid		      integer not null references Interviewer(id)
);
