---
slug: "mecrp"
url: "/mobilnisite/slovnik/mecrp/"
type: "slovnik"
title: "MECRP – Manufacturer-defined Ear Cap Reference Point"
date: 2025-01-01
abbr: "MECRP"
fullName: "Manufacturer-defined Ear Cap Reference Point"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/mecrp/"
summary: "Referenční bod definovaný výrobci zařízení pro měření v oblasti ušního boltce při testování kompatibility se sluchadly. Určuje standardizované umístění na bezdrátovém zařízení pro akustická měření, čí"
---

MECRP je referenční bod definovaný výrobcem na bezdrátovém zařízení, který standardizuje umístění pro akustická měření, aby bylo zajištěno konzistentní testování kompatibility se sluchadly podle specifikací 3GPP.

## Popis

Manufacturer-defined Ear Cap Reference Point (MECRP) je technický koncept definovaný ve specifikacích 3GPP souvisejících s testováním kompatibility se sluchadly (HAC) pro bezdrátová zařízení. Nejde o síťový protokol nebo rozhraní, ale o fyzický referenční bod na mobilním telefonu nebo terminálu. MECRP je konkrétní bod v prostoru, vztažený ke geometrii zařízení, kde se provádějí akustická měření (konkrétně síla magnetického a elektrického pole) za účelem posouzení kompatibility zařízení se sluchadly. Tento bod má představovat typickou polohu mikrofonu sluchadla, když je zařízení přiloženo k uchu. Výrobci definují přesné souřadnice tohoto referenčního bodu pro každý model zařízení a musí být zdokumentován a konzistentně používán během testování shody.

Definice a použití MECRP jsou podrobně popsány v 3GPP TS 26.132 (která pokrývá akustickou testovací specifikaci pro hlasové a videohovorové terminály) a souvisejících dokumentech, jako je TS 26.801 (požadavky HAC). Proces zahrnuje, že výrobce specifikuje trojrozměrný souřadnicový systém vycházející z definovaného 'referenčního bodu' na zařízení (často mechanického prvku, jako je roh nebo konektor). Od tohoto bodu je MECRP definován jako bod umístěný v určité vzdálenosti, simulující polohu ucha a sluchadla. Během testování je specializovaná sonda (sonda magnetického pole nebo anténa elektrického pole) umístěna na tento MECRP, aby změřila rádiové (RF) emise ze zařízení v režimu hovoru i přenosu dat. Tato měření jsou porovnána s limity definovanými standardizačními orgány (jako je [FCC](/mobilnisite/slovnik/fcc/) v USA nebo podobné regulace jinde), aby se určilo, zda zařízení splňuje požadavky HAC.

Jeho role je klíčová pro standardizaci a regulatorní shodu. Existence referenčního bodu definovaného výrobcem, ale konzistentně aplikovaného, zajišťuje, že testování HAC je reprodukovatelné a srovnatelné mezi různými testovacími laboratořemi a pro různé modely zařízení. Bez standardizovaného referenčního bodu by se měření mohla výrazně lišit v závislosti na umístění sondy, což by vedlo k nekonzistentním výsledkům shody. MECRP tedy poskytuje klíčový spojovací článek mezi fyzickým designem zařízení a standardizovanou testovací metodologií, což zajišťuje, že bezdrátová zařízení jsou spravedlivě a přesně hodnocena z hlediska jejich potenciálu způsobit interference se sluchadly.

## K čemu slouží

MECRP byl vytvořen k vyřešení základního problému při testování kompatibility se sluchadly: kam umístit měřicí sondu na zařízení. Bezdrátová zařízení vyzařují RF energii, která se může induktivně vázat do sluchadel a způsobovat slyšitelné bzučení nebo interference. Aby toto bylo regulováno, vlády stanovují limity pro sílu magnetických a elektrických polí vyzařovaných zařízeními v blízkosti ucha. Tvary a velikosti zařízení se však enormně liší, což znemožňuje nařídit jediný pevný měřicí bod (jako '2 cm od sluchátka'), který by byl fyzicky smysluplný pro všechny návrhy. Koncept MECRP poskytuje flexibilní, ale standardizované řešení.

Historicky, před takovou standardizací, byly testovací metodologie nekonzistentní, což vedlo k nejasnostem pro výrobce i regulátory. Někteří mohli měřit ve středu sluchátka, jiní u mikrofonu, což vedlo k nesrovnatelným datům. Zavedení Manufacturer-defined Ear Cap Reference Point v 3GPP Release 16 (a přidružených standardech jako [ANSI](/mobilnisite/slovnik/ansi/) C63.19) poskytlo rámec. Uznává, že výrobce zná akustický design zařízení nejlépe – konkrétně, kde se nachází primární reproduktor (sluchátko) a kde má být ucho umístěno. Proto výrobce definuje referenční bod vzhledem k vlastní geometrii zařízení, čímž zajišťuje, že místo měření je akusticky relevantní pro daný konkrétní model.

Tento přístup řeší omezení univerzálního měřicího bodu. Umožňuje inovace v podobě faktorů zařízení (např. skládací telefony, velké obrazovky) při zachování důsledného a opakovatelného testovacího procesu. MECRP zajišťuje, že testování HAC přesně odráží reálné použití, kdy uživatel drží zařízení v přirozené poloze u ucha. Standardizací způsobu, jakým je tento bod definován a reportován, umožňuje globální regulatorní přijetí testovacích dat, což zjednodušuje certifikační proces pro výrobce zařízení prodávající produkty na více trzích s požadavky HAC.

## Klíčové vlastnosti

- Trojrozměrný prostorový bod definovaný výrobcem zařízení pro každý model
- Slouží jako standardní místo měření pro testy RF emisí HAC
- Vztažen k modelově specifickému souřadnicovému systému a fyzickému datumu
- Používá se pro měření magnetických (H-pole) i elektrických (E-pole) emisí
- Zajišťuje reprodukovatelnost testování mezi různými laboratořemi a zařízeními
- Zdokumentován v testovacích zprávách o shodě zařízení a regulatorních podkladech

## Definující specifikace

- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TS 26.801** (Rel-19) — Testing UEs with Non-Traditional Earpieces

---

📖 **Anglický originál a plná specifikace:** [MECRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/mecrp/)
