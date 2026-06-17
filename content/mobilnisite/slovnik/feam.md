---
slug: "feam"
url: "/mobilnisite/slovnik/feam/"
type: "slovnik"
title: "FEAM – Functional Entity Access Manager"
date: 2025-01-01
abbr: "FEAM"
fullName: "Functional Entity Access Manager"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/feam/"
summary: "Functional Entity Access Manager (FEAM) je bezpečnostní funkce v rámci IP Multimedia Subsystem (IMS), která spravuje řízení přístupu k aplikačním serverům a službám. Funguje jako bod vynucování politi"
---

FEAM je bezpečnostní funkce v rámci IP Multimedia Subsystem (IMS), která spravuje řízení přístupu k aplikačním serverům tím, že autorizuje žádosti o služby na základě uživatelských profilů a síťových politik.

## Popis

Functional Entity Access Manager (FEAM) je specializovaná bezpečnostní funkce definovaná v architektuře IMS dle 3GPP, specifikovaná primárně v TS 29.078. Funguje jako logická entita, často umístěná společně nebo integrovaná do Serving-Call Session Control Function (S-CSCF). Primární rolí FEAM je provádět řízení přístupu pro vyvolání služby v IMS síti. Když uživatel nebo aplikační server ([AS](/mobilnisite/slovnik/as/)) pokusí se vyvolat službu, je žádost zachycena a vyhodnocena FEAM. Ta provádí autorizační rozhodnutí na základě souboru pravidel a politik, které mohou zahrnovat uživatelský předplatitelský profil (načtený z [HSS](/mobilnisite/slovnik/hss/)), identitu žadatele, typ požadované služby a další parametry relace.

Operačně FEAM komunikuje s jádrem IMS přes rozhraní [ISC](/mobilnisite/slovnik/isc/) (IMS Service Control). Po přijetí SIP zprávy (jako je INVITE nebo MESSAGE) určené pro aplikační server může S-CSCF vyvolat logiku FEAM. FEAM vyhodnotí žádost vůči nastaveným politikám. Pokud je žádost autorizována, je předána cílovému AS. Pokud je zamítnuta, může FEAM způsobit, že S-CSCF žádost odmítne s příslušnou SIP chybovou odpovědí. Rozhodování FEAM může být založeno na statických politikách nastavených v síti nebo na dynamických politikách získaných z databáze politik. Hraje klíčovou roli ve scénářích zahrnujících AS třetích stran, zajišťuje, že pouze autorizované a důvěryhodné aplikace mohou komunikovat s jádrem IMS jménem uživatele.

Architektonicky FEAM posiluje bezpečnostní rámec IMS přidáním vrstvy autorizace na úrovni služby, čímž doplňuje autentizaci na síťové úrovni prováděnou CSCFs. Je součástí širšího rámce IMS Service Authorization. Přestože ne všechny IMS nasazení implementují samostatný FEAM uzel, jeho funkce jsou povinné a jsou implementovány v rámci logiky S-CSCF nebo vyhrazeného policy serveru. Jeho specifikace zajišťuje standardizovanou metodu pro řízení přístupu k IMS službám, což je zásadní pro prevenci podvodů, správu úrovní služeb a umožnění bezpečných otevřených servisních prostředí, kde operátoři mohou zpřístupnit síťové schopnosti externím partnerům.

## K čemu slouží

FEAM byl zaveden, aby řešil bezpečnostní a kontrolní výzvy vyplývající z otevřeného, na aplikace zaměřeného designu IP Multimedia Subsystem (IMS). IMS byl navržen tak, aby oddělil služby od základního přenosu, což umožňuje více aplikačním serverům (jak vlastněným operátorem, tak třetích stran) poskytovat služby. To vytvořilo kritickou potřebu robustního mechanismu pro řízení toho, které entity (uživatelé nebo [AS](/mobilnisite/slovnik/as/)) mohou vyvolat které služby a za jakých podmínek. Bez FEAM by S-CSCF slepě předával žádosti o služby, což by síť vystavovalo riziku neoprávněného přístupu ke službám, spamu a podvodům.

Jeho vytvoření bylo motivováno požadavkem na standardizovanou, na politikách založenou vrstvu řízení přístupu v rámci servisní roviny IMS. Předchozí přístupy často zabudovávaly autorizační logiku přímo do jednotlivých aplikačních serverů, což vedlo k fragmentaci a nekonzistentnímu zabezpečení. FEAM centralizuje tuto logiku v jádru sítě a poskytuje jednotný kontrolní bod. To řeší několik problémů: umožňuje operátorům vynucovat konzistentní obchodní a bezpečnostní politiky napříč všemi službami, umožňuje efektivní správu uživatelských servisních profilů z jediného místa ([HSS](/mobilnisite/slovnik/hss/)) a poskytuje bezpečnou bránu pro poskytovatele služeb třetích stran pro přístup k síťovým schopnostem, jak je definováno v rámci Open Service Access ([OSA](/mobilnisite/slovnik/osa/)) a Parlay dle 3GPP. Je klíčovým prvkem pro důvěryhodné a zpoplatnitelné poskytování multimediálních služeb.

## Klíčové vlastnosti

- Provádí autorizaci na úrovni služby pro žádosti o služby v IMS
- Funguje jako bod vynucování politik integrovaný s S-CSCF
- Rozhoduje na základě předplatitelských dat uživatele, typu služby a síťových politik
- Zachycuje signalizaci SIP na rozhraní ISC směrem k aplikačním serverům a od nich
- Chrání síťové zdroje a zabraňuje neoprávněnému vyvolání služeb
- Umožňuje bezpečný přístup aplikačních serverů třetích stran k IMS schopnostem

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification

---

📖 **Anglický originál a plná specifikace:** [FEAM na 3GPP Explorer](https://3gpp-explorer.com/glossary/feam/)
