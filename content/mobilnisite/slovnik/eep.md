---
slug: "eep"
url: "/mobilnisite/slovnik/eep/"
type: "slovnik"
title: "EEP – Ear Entrance Point"
date: 2025-01-01
abbr: "EEP"
fullName: "Ear Entrance Point"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/eep/"
summary: "Referenční bod při testování zvuku představující akustický vstup do zvukovodu. Je klíčový pro standardizaci měření kvality zvuku a hlasitosti pro 3GPP řečové kodeky a koncová zařízení, což zajišťuje k"
---

EEP je akustický referenční bod na vstupu do zvukovodu, používaný pro standardizaci měření kvality zvuku a hlasitosti pro 3GPP řečové kodeky a koncová zařízení.

## Popis

Bod vstupu do ucha (EEP) je standardizovaný anatomický referenční bod používaný ve specifikacích 3GPP pro testování audio výkonu. Je definován jako bod v prostoru umístěný na vstupu do zvukovodu. Tento bod slouží jako klíčová reference pro umístění umělých testovacích zařízení, jako jsou simulátory hlavy a trupu ([HATS](/mobilnisite/slovnik/hats/)) s ušními simulátory, během objektivních měření kvality přenosu zvuku, hlasitosti a frekvenční charakteristiky pro koncová zařízení, jako jsou mobilní telefony, sluchátka a hands-free systémy.

V testovací architektuře není EEP fyzickou součástí, ale konceptuálním orientačním bodem. Primárním fyzickým aparátem je standardizovaný ušní simulátor (podle definice [ITU-T](/mobilnisite/slovnik/itu-t/) P.57), což je konektor navržený tak, aby napodoboval akustickou impedanci a objem průměrného lidského zvukovodu. Tento ušní simulátor je umístěn v umělé hlavě nebo trupu. EEP je bod v prostoru na otvoru kanálu tohoto ušního simulátoru. Při testování je testované zařízení ([DUT](/mobilnisite/slovnik/dut/)), například sluchátko telefonu nebo reproduktor headsetu, pečlivě umístěno vůči tomuto EEP podle přesného geometrického zarovnání definovaného v testovacích standardech (např. poloha 'tvář' nebo 'dotyk').

Úlohou EEP je zajistit reprodukovatelnost. Audio charakteristiky, jako je hladina akustického tlaku (hlasitost), frekvenční charakteristika a zpětná vazba (sidetone), jsou vysoce citlivé na přesnou vzdálenost a úhel mezi zdrojem zvuku a uchem. Definováním pevného, jednoznačného referenčního bodu 3GPP zajišťuje, že různí výrobci a testovací laboratoře po celém světě zarovnávají svá DUT stejným způsobem. To umožňuje spravedlivá, srovnatelná a opakovatelná měření klíčových ukazatelů výkonu ([KPI](/mobilnisite/slovnik/kpi/)), jako je hodnocení vysílací hlasitosti (SLR), hodnocení přijímací hlasitosti ([RLR](/mobilnisite/slovnik/rlr/)) a celkové harmonické zkreslení (THD).

Měření probíhají generováním nebo zachycováním testovacích signálů prostřednictvím DUT, zatímco je toto zařízení akusticky spojeno s ušním simulátorem na úrovni EEP. Signál je analyzován měřicím zařízením připojeným k mikrofonu ušního simulátoru. Celý řetězec – od audio kodeku a reproduktoru DUT, přes vzduchovou mezeru k EEP, do ušního simulátoru a k analyzátoru – je kalibrován vůči tomuto referenčnímu bodu. Tato standardizace je zásadní pro ověření, že zařízení splňují minimální požadavky na kvalitu zvuku pro interoperabilitu sítě a uživatelský zážitek.

## K čemu slouží

EEP byl standardizován, aby vyřešil problém nekonzistentního a neopakovatelného testování zvuku pro telekomunikační koncová zařízení. Před takovými přesnými definicemi mohly různé testovací laboratoře umisťovat zařízení mírně odlišně vůči figurínám hlav nebo uší, což vedlo k významným odchylkám v měřené hlasitosti a frekvenční charakteristice. To ztěžovalo objektivní srovnání zařízení, vymáhání kvalitativních standardů a zaručení konzistentního uživatelského zážitku napříč průmyslem.

Historická motivace vychází z potřeby síťových operátorů a normalizačních orgánů definovat jasná kritéria vyhověl/nevyhověl pro typové schvalování koncových zařízení. S vývojem digitálních řečových kodeků (jako [AMR](/mobilnisite/slovnik/amr/), [EVS](/mobilnisite/slovnik/evs/)) se stalo kritickým přesné měření jejich výkonu v realistickém akustickém prostředí. EEP spolu s celým rámcem simulátoru hlavy a trupu poskytuje řízené, antropomorfní 'akustické rozhraní' potřebné pro převod elektrických signálů z kodeku na vnímaný akustický výkon.

Tento referenční bod řeší omezení jednoduššího elektrického loopback testování. Kvalita zvuku je nakonec vnímána lidským uchem, na které mají vliv akustika zařízení, geometrie ucha a umístění. Ukotvením testů k EEP vytváří 3GPP náhradu za skutečný lidský poslechový zážitek v laboratorním prostředí. Zajišťuje, že zařízení splňující standard poskytnou koncovým uživatelům dostatečnou a konzistentní hlasitost a věrnost zvuku, bez ohledu na to, kdo zařízení vyrobil nebo kde bylo testováno.

## Klíčové vlastnosti

- Standardizovaný anatomický referenční bod na vstupu do zvukovodu
- Základ pro reprodukovatelné umístění koncových zařízení během akustických testů
- Používá se s umělými simulátory hlavy a trupu (HATS) a ušními simulátory
- Klíčový pro měření hodnocení přijímací hlasitosti (RLR) a hodnocení vysílací hlasitosti (SLR)
- Umožňuje srovnatelná měření frekvenční charakteristiky a zkreslení napříč laboratořemi
- Definován ve spojení se specifickými testovacími polohami telefonu 'tvář' a 'dotyk'

## Definující specifikace

- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods

---

📖 **Anglický originál a plná specifikace:** [EEP na 3GPP Explorer](https://3gpp-explorer.com/glossary/eep/)
