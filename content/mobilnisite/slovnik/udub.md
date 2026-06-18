---
slug: "udub"
url: "/mobilnisite/slovnik/udub/"
type: "slovnik"
title: "UDUB – User Determined User Busy"
date: 2025-01-01
abbr: "UDUB"
fullName: "User Determined User Busy"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/udub/"
summary: "Doplňková služba, která umožňuje volanému uživateli záměrně signalizovat síti stav obsazení, čímž zabrání příchozím hovorům. Umožňuje uživatelům ručně aktivovat stav obsazení, obvykle pomocí funkce na"
---

UDUB je doplňková služba, která umožňuje volanému uživateli ručně aktivovat pro síť stav obsazení, čímž zabrání příchozím hovorům a tónu volání zpět pro explicitní řízení hovorů a soukromí.

## Popis

User Determined User Busy (UDUB) je telekomunikační doplňková služba definovaná ve standardech 3GPP, která dává volané straně možnost záměrně signalizovat síti stav 'obsazení' pro příchozí hovory. Na rozdíl od stavu obsazení určeného sítí (který nastane, když je uživatel již v hovoru nebo má síťově ověřenou nedostupnost), je UDUB explicitně vyvolána uživatelem, často prostřednictvím konkrétní akce na mobilním koncovém zařízení, jako je stisknutí tlačítka 'obsazeno' nebo výběr možnosti 'odmítnout s obsazením' během upozornění na příchozí hovor. Při aktivaci způsobí služba, že terminál uživatele odpoví na pokus sítě o sestavení hovoru specifickým indikátorem, že uživatel je obsazen z vlastní volby. Síť, typicky obsluhující [MSC](/mobilnisite/slovnik/msc/) nebo funkce řízení relace hovoru ([CSCF](/mobilnisite/slovnik/cscf/)), to pak zpracuje jako stav obsazení a použije příslušné procedury pro obsluhu hovoru, které obvykle zahrnují ukončení pokusu o hovor a vrácení tónu obsazení nebo hlášení volající straně.

Architektonická implementace UDUB zahrnuje koordinaci mezi uživatelským zařízením (UE), obsluhujícím síťovým uzlem (např. MSC v okruhově spínaných doménách nebo CSCF v IMS) a potenciálně serverem domovského účastníka ([HSS](/mobilnisite/slovnik/hss/)), kde jsou uložena data o předplatném služby. Když dorazí příchozí hovor, síť odešle zprávu pro sestavení (jako SETUP v [CS](/mobilnisite/slovnik/cs/) nebo INVITE v IMS) volanému UE. Pokud se uživatel rozhodne vyvolat UDUB, UE hovor nezvedne, ale místo toho odešle síti specifickou zprávu o odmítnutí. V okruhově spínaných sítích to může být zpráva DISCONNECT nebo RELEASE COMPLETE s hodnotou příčiny indikující 'uživatel obsazen' (příčina č. 17). V IMS by UE odeslalo odpověď 486 Busy Here na INVITE. Síťový uzel tuto odpověď interpretuje, ověří, zda je uživatel přihlášen ke službě UDUB (v případě potřeby kontrolou dat účastníka), a poté provede uvolnění hovoru směrem k volajícímu s poskytnutím indikace obsazení.

Klíčovými komponentami služby UDUB jsou servisní logika v síťové ústředně nebo řadiči relace, signalizační protokoly mezi UE a sítí (jako [DTAP](/mobilnisite/slovnik/dtap/) v CS nebo [SIP](/mobilnisite/slovnik/sip/) v IMS) a profil účastníka, který může řídit, zda je služba aktivní. Úlohou UDUB v síti je poskytnout uživatelům přímý a jednoznačný mechanismus pro řízení příchozí komunikace, čímž se zvyšuje soukromí a správa hovorů. Liší se od pouhého nezvednutí hovoru (což může vést k vyzvánění bez odpovědi a případnému přesměrování) nebo použití přesměrování při obsazení, protože UDUB je okamžitý, uživatelem iniciovaný signál obsazení, který typicky vede k rychlejšímu ukončení hovoru a jasné indikaci obsazení pro volajícího. Tato služba je zvláště cenná ve scénářích, kdy se uživatelé chtějí vyhnout přerušením, aniž by museli vypínat zařízení nebo zapínat bezpodmínečné přesměrování, a nabízí tak střední cestu pro aktivní třídění hovorů.

## K čemu slouží

Doplňková služba UDUB byla vytvořena, aby uspokojila potřebu lepší uživatelské kontroly nad obsluhou příchozích hovorů v digitálních mobilních sítích. Před existencí takových funkcí měli uživatelé omezené možnosti při přijetí nežádoucího hovoru: mohli hovor zvednout a poté zavěsit, nechat vyzvánět do doby, než se aktivuje přesměrování při neodpovědi (pokud bylo nakonfigurováno), nebo vypnout telefon – všechny tyto možnosti byly společensky nepříjemné, zpožděné nebo příliš radikální. Existovala mezera v poskytování zdvořilé, okamžité a síťově asistované metody pro odmítnutí hovoru při současném jasném signalizování nedostupnosti volajícímu. UDUB tuto mezeru zaplňuje tím, že umožňuje uživateli ručně spustit stav 'obsazení', čímž dá volajícímu jasný tón obsazení nebo hlášení, což je společensky přijímaná indikace, že volaný není dostupný, aniž by se prozradilo, zda je stav obsazení skutečný nebo záměrný.

Motivace pro standardizaci UDUB v rámci 3GPP vycházela z vývoje doplňkových služeb v GSM a jejich pokračování v UMTS a IMS. Protože sítě nabízely pokročilejší funkce hovorů (jako čekání na hovor, přesměrování hovoru a explicitní přenos hovoru), stalo se poskytování jemně odstupňované kontroly nad přijímáním hovorů klíčovým diferenciátorem kvality služeb. UDUB řeší problém pasivního odmítání hovoru tím, že z něj činí aktivní, na službě založené rozhodnutí. Také spolupracuje s dalšími doplňkovými službami; například, pokud je aktivní přesměrování při obsazení, může vyvolání UDUB spustit přesměrování na hlasovou schránku v závislosti na nastavení předplatného. To vytváří ucelený uživatelský zážitek ze správy hovorů.

Historicky byla UDUB zavedena v 3GPP Rel-4, v souladu s vývojem vylepšení GSM Phase 2+ a jádra sítě UMTS. Její vytvoření bylo hnací silou poptávky operátorů a uživatelů po lepších funkcích řízení hovorů, zejména s rozšířením mobilních telefonů a touhou zvládat rostoucí objemy hovorů. Standardizací UDUB zajistilo 3GPP interoperabilitu napříč sítěmi a zařízeními, což uživatelům umožnilo spoléhat se na konzistentní chování bez ohledu na jejich polohu nebo model koncového zařízení. Služba řešila omezení dřívějších systémů, kde byly stavy obsazení určovány výhradně sítí, a dala tak uživatelům posílenou roli při správě jejich komunikační dostupnosti.

## Klíčové vlastnosti

- Uživatelem iniciovaný stav obsazení pro příchozí hovory
- Poskytuje volající straně jasnou indikaci obsazení (tón/hlášení)
- Typicky se vyvolává prostřednictvím uživatelského rozhraní koncového zařízení během upozornění na hovor
- Funguje jak v okruhově spínaných, tak v IMS relacích hovorů
- Spolupracuje s dalšími doplňkovými službami, jako je přesměrování hovoru
- Zvyšuje uživatelské soukromí a kontrolu nad správou hovorů

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 24.428** (Rel-7) — Common Basic Communication Procedures
- **TS 24.528** (Rel-8) — Common Basic Communication Procedures for IMS Services
- **TS 24.615** (Rel-19) — Communication Waiting (CW) Service Protocol
- **TS 24.628** (Rel-19) — Common Basic Communication Procedures in IMS

---

📖 **Anglický originál a plná specifikace:** [UDUB na 3GPP Explorer](https://3gpp-explorer.com/glossary/udub/)
