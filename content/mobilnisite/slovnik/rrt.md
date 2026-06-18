---
slug: "rrt"
url: "/mobilnisite/slovnik/rrt/"
type: "slovnik"
title: "RRT – Rating Region Table"
date: 2025-01-01
abbr: "RRT"
fullName: "Rating Region Table"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rrt/"
summary: "Datová struktura definovaná v 3GPP pro službu multimediální telefonie (MTSI), která mapuje geografické regiony na konkrétní fakturační nebo tarifní politiky. Umožňuje dynamické, na polohu citlivé účto"
---

RRT je datová struktura 3GPP pro službu multimediální telefonie (Multimedia Telephony Service), která mapuje geografické regiony na konkrétní fakturační politiky, aby umožnila účtování citlivé na polohu.

## Popis

Rating Region Table (RRT) je koncept na aplikační vrstvě specifikovaný v rámci standardů 3GPP pro službu multimediální telefonie pro IMS ([MTSI](/mobilnisite/slovnik/mtsi/)), primárně dokumentovaný v TS 26.917. Funguje jako konfigurovatelná databáze nebo tabulka používaná aplikačním serverem, typicky Telephony Application Server ([TAS](/mobilnisite/slovnik/tas/)), k určení příslušné účtovací sazby nebo politiky pro komunikační relaci na základě geografické polohy zúčastněných uživatelů. Základní mechanismus spočívá v mapování identifikátoru 'Rating Region' na konkrétní soubor účtovacích pravidel. Rating Region je logická oblast, jako je země, skupina zemí, stát nebo specifická servisní oblast síťového operátora. Když je uskutečněn MTSI hovor nebo relace, obslužný síťový uzel (např. MTSI Application Server) může zjistit polohu volajícího a/nebo volaného účastníka, často odvozenou ze síťových informací o poloze nebo z předplatitelských dat.

Po určení příslušného geografického kontextu server konzultuje RRT. Vyhledání v tabulce poskytne konkrétní tarifní politiku použitelnou pro danou relaci. Tato politika definuje parametry, jako je tarif (cena za minutu, objem dat nebo událost), fakturační měna, případné variace sazeb podle denní doby nebo dne v týdnu a potenciálně i odpovědný účtovací systém (např. Online Charging System - [OCS](/mobilnisite/slovnik/ocs/) nebo Offline Charging System - [OFCS](/mobilnisite/slovnik/ofcs/)), který má být použit. RRT tedy funguje jako kritická překladová vrstva mezi fyzickou/síťovou polohou relace a komerční logikou řídící její cenu. Její implementace umožňuje jedné servisní platformě podporovat komplexní, více regionální komerční nasazení bez nutnosti pevně zakódované logiky pro každou možnou kombinaci poloh.

Z architektonického hlediska je RRT funkční komponentou v rámci servisní vrstvy, oddělenou od rozhraní pro účtování v jádrové síti, jako je Diameter Ro/Rf. Je provizována a spravována poskytovatelem služeb, často prostřednictvím operačních podpůrných systémů. Obsah tabulky je dynamický a může být aktualizován, aby odrážel nové tarifní plány, regulatorní změny v konkrétních regionech nebo propagační nabídky. Během nastavování relace MTSI [AS](/mobilnisite/slovnik/as/) používá výstup z RRT ke konstrukci příslušných účtovacích informací, které jsou následně předány účtovacím funkcím jádrové sítě prostřednictvím standardizovaných mechanismů. To umožňuje generovat přesné, na polohu citlivé účtovací události, což zajišťuje správné účtování předplatitelům podle toho, kde službu používají. RRT je klíčovým prvkem pro komerční služby Voice over LTE (VoLTE) a Video over LTE (ViLTE), který operátorům umožňuje bezproblémově implementovat diferencované ceny pro domácí, mezinárodní a roamingové scénáře.

## K čemu slouží

Rating Region Table (RRT) byla vytvořena, aby řešila komerční a provozní složitost účtování za IP-based služby multimediální telefonie, jako je VoLTE, v globalizovaném prostředí s podporou roamingu. Tradiční telefonie v přepojování okruhů měla relativně statické účtovací modely často vázané na předčíslí volaného čísla (např. kód země, směrové číslo). Nicméně u služeb založených na IMS se koncept polohy stává pružnějším – uživatel může být fyzicky v jedné zemi, ale registrován u své domácí sítě (roaming), a servisní logika je oddělena od podkladového přenosu. To vytvořilo výzvu: jak aplikovat správný tarif pro hovor, kde volající může být v roamingu, volaný může být v jiné zemi a služba je doručována přes paketové IP připojení.

RRT to řeší zavedením flexibilního, konfigurovatelného mapování mezi logickými geografickými regiony a účtovacími politikami. Jejím účelem je oddělit servisní logiku od komplexních, často aktualizovaných pravidel obchodu a regulace. Bez takové tabulky by aplikační servery potřebovaly vestavěnou, pevně zakódovanou logiku pro každou možnou dvojici poloh, což by činilo aktualizace tarifů těžkopádnými, náchylnými k chybám a pomalými na nasazení. RRT umožňuje operátorům centrálně definovat a upravovat tarifní regiony a s nimi spojené politiky, což umožňuje rychlou reakci na změny na trhu, nové roamingové dohody nebo regulatorní požadavky v konkrétních jurisdikcích.

Historicky bylo její zavedení v Release 14 jako součást rozšířených specifikací [MTSI](/mobilnisite/slovnik/mtsi/) motivováno rozsáhlým komerčním nasazením VoLTE/ViLTE. Operátoři potřebovali standardizovanou, robustní metodu pro implementaci sofistikovaných účtovacích schémat, která by dokázala rozlišovat mezi využitím domácí a navštívené sítě, aplikovat speciální sazby pro konkrétní regiony (jako 'home zone' nebo partnerské sítě) a podporovat komplexní modely vypořádání mezi operátory pro roaming. RRT poskytuje tuto nezbytnou abstraktní vrstvu. Dává poskytovatelům služeb možnost vytvářet konkurenceschopné a spravedlivé cenové modely, které odrážejí skutečnou cenu a hodnotu služby v různých kontextech, což je zásadní pro komerční úspěch telefonie založené na IMS jako náhrady za starší telefonii v přepojování okruhů.

## Klíčové vlastnosti

- Mapuje logické geografické regiony (Rating Regions) na konkrétní účtovací tarify a politiky
- Umožňuje dynamické, na polohu citlivé účtování za multimediální telefonii založenou na IMS (MTSI/VoLTE)
- Odděluje servisní logiku od pravidel komerčních tarifů pro snadnější aktualizace a správu
- Podporuje komplexní scénáře včetně roamingu, mezinárodních hovorů a regionálních propagačních akcí
- Integruje se s Online Charging System (OCS) a Offline Charging System (OFCS) jádrové sítě
- Konfigurovatelná a provizovatelná operačními podpůrnými systémy poskytovatele služeb

## Související pojmy

- [MTSI – Multimedia Telephony Services for IMS](/mobilnisite/slovnik/mtsi/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP

---

📖 **Anglický originál a plná specifikace:** [RRT na 3GPP Explorer](https://3gpp-explorer.com/glossary/rrt/)
