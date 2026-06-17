---
slug: "bdn"
url: "/mobilnisite/slovnik/bdn/"
type: "slovnik"
title: "BDN – Barred Dialling Number"
date: 2025-01-01
abbr: "BDN"
fullName: "Barred Dialling Number"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bdn/"
summary: "Barred Dialling Number (BDN) je služební funkce na úrovni účastníka v sítích 3GPP, která omezuje odchozí hovory na konkrétní telefonní čísla. Je spravována prostřednictvím aplikace USIM a vynucována m"
---

BDN je služební funkce na úrovni účastníka v sítích 3GPP, která omezuje odchozí hovory na konkrétní telefonní čísla, je spravována přes USIM a vynucována mobilním zařízením.

## Popis

Barred Dialling Number (BDN) je standardizovaná služební funkce v rámci specifikací 3GPP, konkrétně definovaná jako součást aplikační platformy USIM (Universal Subscriber Identity Module). Jejím hlavním účelem je umožnit zákaz (blokování) odchozích hlasových hovorů a potenciálně i dalších komunikačních pokusů, jako jsou SMS nebo datové relace, na předdefinovaný seznam telefonních čísel nebo číselných rozsahů. Seznam BDN je uložen jako vyhrazený soubor ([EF](/mobilnisite/slovnik/ef/)_BDN) na kartě USIM, což je zabezpečený, proti neoprávněné manipulaci chráněný prvek. Tento soubor obsahuje záznamy specifikující zakázaná čísla, která mohou být plná mezinárodní čísla (např. +441234567890) nebo částečná čísla využívající zástupné znaky pro blokování rozsahů čísel (např. blokování všech čísel prémiových tarifů začínajících konkrétní předvolbou). Vynucování zákazu je prováděno lokálně Mobile Equipment ([ME](/mobilnisite/slovnik/me/)), tj. telefonem nebo zařízením, nikoli síťovým jádrem. Když uživatel zahájí hovor, protokolový zásobník zařízení před pokračováním v signalizaci sestavení hovoru konzultuje seznam BDN uložený na USIM. Pokud volané číslo odpovídá záznamu v seznamu BDN, zařízení lokálně přeruší pokus o hovor a typicky uživatele informuje, že hovor je zakázán. Toto lokální vynucování je klíčovým architektonickým aspektem, protože nespotřebovává síťové prostředky pro hovor, který by byl nakonec zablokován, a poskytuje uživateli okamžitou zpětnou vazbu.

Správa seznamu BDN může probíhat několika mechanismy. Může být předem zřízena síťovým operátorem na USIM, často z obchodních nebo bezpečnostních důvodů (např. zákaz mezinárodního vytáčení na firemním telefonu). Případně ji může nakonfigurovat účastník prostřednictvím uživatelského rozhraní telefonu, pokud to operátor takovou uživatelskou kontrolu umožňuje. USIM Application Toolkit (USAT) poskytuje standardizované příkazy pro zabezpečenou interakci mezi zařízením a USIM za účelem čtení, aktualizace nebo ověření seznamu BDN. Provoz funkce je integrován s dalšími službami založenými na USIM a s logikou řízení hovorů zařízení. Funguje jako kontrola první linie předtím, než je pro odchozí hovor z mobilního zařízení navázáno jakékoli rádiové spojení.

Z pohledu sítě je BDN nástroj pro správu služeb zaměřený na účastníka. Zatímco síťové jádro ([MSC](/mobilnisite/slovnik/msc/)/VLR v okruhově spínaných doménách) si není vědomo kontroly BDN probíhající na zařízení, funkce přímo ovlivňuje uživatelský zážitek ze služby a fakturaci. Pomáhá předcházet neúmyslnému využití, jako jsou hovory na drahá čísla s prémiovým tarifem nebo mezinárodní čísla, což může vést k neočekávaně vysokému účtu. Pro podniky je to nástroj k vynucování telekomunikačních politik na zařízeních poskytovaných firmou. Specifikace BDN napříč dokumenty jako 3GPP TS 31.102 (charakteristiky USIM) a TS 31.121 (rozhraní UICC-terminál) zajišťuje interoperabilitu mezi USIM od různých výrobců a mobilními zařízeními, což z ní činí všeobecně podporovanou funkci v sítích 3GPP od 3G výše. Její role je doplňková k síťovým službám zákazu hovorů, jako je Barring of All Outgoing Calls ([BAOC](/mobilnisite/slovnik/baoc/)) nebo Barring of Outgoing International Calls ([BOIC](/mobilnisite/slovnik/boic/)), a nabízí podrobnější, na konkrétní čísla zaměřený řídicí mechanismus.

## K čemu slouží

Funkce Barred Dialling Number byla zavedena, aby řešila potřebu podrobné, na konkrétního účastníka zaměřené kontroly nad odchozími hovory v mobilních sítích. Před její standardizací byl zákaz hovorů primárně síťovou funkcí (jako [BAOC](/mobilnisite/slovnik/baoc/)) řízenou operátorem přes [HLR](/mobilnisite/slovnik/hlr/) nebo obsluhující [MSC](/mobilnisite/slovnik/msc/). Tyto síťové služby zákazu byly všeobecné, vztahovaly se na celé kategorie hovorů (např. všechny mezinárodní hovory) a pro účastníka je nebylo snadné měnit. Objevila se rostoucí poptávka, zejména od korporátních zákazníků a nákladově uvědomělých spotřebitelů, po možnosti blokovat hovory na konkrétní, známá drahá čísla (např. určité služby s prémiovým tarifem) nebo neoprávněná čísla, aniž by se zakazovaly všechny hovory určitého typu.

BDN to řeší přesunutím kontrolního bodu na USIM a telefon. Tato decentralizace umožňuje personalizovaný seznam zakázaných čísel, který je přenosný spolu s SIM kartou účastníka. Účel je dvojí: za prvé, poskytnout uživatelům nebo jejich správcům (např. firemní IT) přímou kontrolu nad oprávněními k hovorům, čímž se zvyšuje bezpečnost a správa nákladů; za druhé, snížit problémy se zákaznickým servisem a spory související s neoprávněnými hovory, protože zákaz je proaktivně vynucován samotným zařízením. Historicky vzrůst služeb prémiových SMS a hlasových služeb na počátku roku 2000, který někdy vedl k 'odběratelským pastem' nebo podvodným poplatkům, motivoval potřebu takových uživatelsky přístupných nástrojů zákazu.

Vytvoření BDN bylo motivováno rostoucí programovatelností a inteligencí SIM karty, která se vyvinula v USIM. Platforma USIM aplikací poskytla zabezpečené a standardizované prostředí pro hostování takové funkce. Uložením seznamu zakázaných čísel na USIM se stává nezávislým na telefonu; pokud uživatel změní telefon, jeho seznam zákazů zůstane neporušený. Tím se řeší omezení funkcí zákazu pouze na úrovni telefonu, které nebyly přenosné. Dále poskytuje standardizované rozhraní, které mohou používat všechny kompatibilní telefony, a zajišťuje tak konzistentní uživatelský zážitek napříč různými výrobci zařízení a síťovými operátory, což byl klíčový cíl snah 3GPP o interoperabilitu.

## Klíčové vlastnosti

- Ukládá seznam zakázaných telefonních čísel nebo číselních vzorů na USIM (soubor EF_BDN)
- Vynucováno lokálně Mobile Equipment před zahájením signalizace sestavení hovoru
- Podporuje zástupné znaky pro zákaz rozsahů čísel (např. konkrétní směrová čísla zemí nebo služeb)
- Spravovatelné přes uživatelské rozhraní telefonu (je-li povoleno) nebo přenosově síťovým operátorem
- Poskytuje přenosné řešení zákazu vázané na USIM, nikoli na konkrétní telefon
- Funguje nezávisle na síťových službách zákazu, ale doplňuje je

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification

---

📖 **Anglický originál a plná specifikace:** [BDN na 3GPP Explorer](https://3gpp-explorer.com/glossary/bdn/)
