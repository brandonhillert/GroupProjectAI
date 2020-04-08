CREATE TABLE "profile" (
	"id" varchar(255) NOT NULL,
	"recommendation_segment" varchar(45),
	"recommendations" varchar,
	"buids" varchar,
	CONSTRAINT "profile_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "session" (
	"id" varchar(255) NOT NULL,
	"has_sale" varchar(45),
	"prefences" varchar(45),
	"profile_id" varchar(255) NOT NULL,
	"buid" varchar(255),
	"segment" varchar(255),
	"It_order" varchar(255),
	CONSTRAINT "session_pk" PRIMARY KEY ("id")
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
	"discount" varchar(45),
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



CREATE TABLE "all_p" (
	"_id" varchar(255),
	"data" varchar(255),
	"price" varchar(255),
	"category" varchar(255),
	"sub_category" varchar(255),
	"sub_sub_category" varchar(255),
	"gender" varchar(255),
	"color" varchar(255),
	"discount" varchar(255),
	"brand" varchar(255)
) WITH (
  OIDS=FALSE
);



CREATE TABLE "all_pro" (
	"_id" varchar(255) NOT NULL,
	"buids" varchar(255),
	"recommendations" varchar(255),
	"viewed_before" varchar(255)
) WITH (
  OIDS=FALSE
);



CREATE TABLE "all_se" (
	"_id" varchar(255) NOT NULL,
	"buid" varchar(255),
	"has_sale" varchar(255),
	"segment" varchar(255),
	"preferences" varchar(255),
	"itorder" varchar(255)
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Recommendation_Table" (
	"id" varchar(255) NOT NULL,
	"product1" varchar(255),
	"product2" varchar(255),
	"product3" varchar(255),
	"product4" varchar(255),
	"product5" varchar(255),
	CONSTRAINT "Recommendation_Table_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);


ALTER TABLE "session" ADD CONSTRAINT "session_fk0" FOREIGN KEY ("profile_id") REFERENCES "profile"("id");

ALTER TABLE "product" ADD CONSTRAINT "product_fk0" FOREIGN KEY ("brand_idBrand") REFERENCES "brand"("idBrand");
ALTER TABLE "product" ADD CONSTRAINT "product_fk1" FOREIGN KEY ("gender_idgender") REFERENCES "gender"("idgender");
ALTER TABLE "product" ADD CONSTRAINT "product_fk2" FOREIGN KEY ("catergory_idcatergory") REFERENCES "category"("idcatergory");

ALTER TABLE "Recommendation_Table" ADD CONSTRAINT "Recommendation_Table_fk0" FOREIGN KEY ("id") REFERENCES "profile"("recommendations");

