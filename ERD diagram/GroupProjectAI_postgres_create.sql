CREATE TABLE "profile" (
	"id" varchar(255) NOT NULL,
	"recommendation_segment" varchar(45),
	"recommendations" varchar(255),
	"buids" varchar(255),
	CONSTRAINT "profile_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "session" (
	"id" varchar(255) NOT NULL,
	"has_sale" varchar(45),
	"prefences" varchar(45),
	"profile_id" varchar(255),
	"buid" varchar(255),
	"segment" varchar(255),
	CONSTRAINT "session_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "preference_session" (
	"id" serial NOT NULL,
	"session_id" varchar(255) NOT NULL,
	"category_idcategory" integer NOT NULL,
	CONSTRAINT "preference_session_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "order_session" (
	"id" serial NOT NULL,
	"session_id" varchar(255) NOT NULL,
	"product_id" varchar(45) NOT NULL,
	CONSTRAINT "order_session_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "brand" (
	"idBrand" serial NOT NULL,
	"brandnaam" varchar(45),
	CONSTRAINT "brand_pk" PRIMARY KEY ("idBrand")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "product" (
	"id" varchar(45) NOT NULL,
	"selling_price" integer,
	"brand_idBrand" integer,
	"gender_idgender" integer,
	"herhaalaankoop" varchar(45),
	"catergory_idcatergory" integer,
	CONSTRAINT "product_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "gender" (
	"idgender" serial NOT NULL,
	"gendernaam" varchar(45),
	CONSTRAINT "gender_pk" PRIMARY KEY ("idgender")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "category" (
	"idcatergory" serial NOT NULL,
	"category" varchar(45),
	"sub_category" varchar(45),
	"sub_sub_category" varchar(45),
	CONSTRAINT "category_pk" PRIMARY KEY ("idcatergory")
) WITH (
  OIDS=FALSE
);



/*
ALTER TABLE "session" ADD CONSTRAINT "session_fk0" FOREIGN KEY ("profile_id") REFERENCES "profile"("id");

ALTER TABLE "preference_session" ADD CONSTRAINT "preference_session_fk0" FOREIGN KEY ("session_id") REFERENCES "session"("id");
ALTER TABLE "preference_session" ADD CONSTRAINT "preference_session_fk1" FOREIGN KEY ("category_idcategory") REFERENCES "category"("idcatergory");

ALTER TABLE "order_session" ADD CONSTRAINT "order_session_fk0" FOREIGN KEY ("session_id") REFERENCES "session"("id");
ALTER TABLE "order_session" ADD CONSTRAINT "order_session_fk1" FOREIGN KEY ("product_id") REFERENCES "product"("id");


ALTER TABLE "product" ADD CONSTRAINT "product_fk0" FOREIGN KEY ("brand_idBrand") REFERENCES "brand"("idBrand");
ALTER TABLE "product" ADD CONSTRAINT "product_fk1" FOREIGN KEY ("gender_idgender") REFERENCES "gender"("idgender");
ALTER TABLE "product" ADD CONSTRAINT "product_fk2" FOREIGN KEY ("catergory_idcatergory") REFERENCES "category"("idcatergory");
*/


