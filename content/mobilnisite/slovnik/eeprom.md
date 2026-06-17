---
slug: "eeprom"
url: "/mobilnisite/slovnik/eeprom/"
type: "slovnik"
title: "EEPROM – Electronically Erasable Programmable Read-Only Memory"
date: 2025-01-01
abbr: "EEPROM"
fullName: "Electronically Erasable Programmable Read-Only Memory"
category: "Other"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/eeprom/"
summary: "Typ nevolatilní paměti používané v UE a síťových zařízeních k ukládání semitrvalých konfiguračních dat, firmwaru a bezpečnostních klíčů. Umožňuje uchování dat i po vypnutí napájení, ale lze je aktuali"
---

EEPROM (elektricky vymazatelná programovatelná paměť pouze pro čtení) je typ nevolatilní paměti používané v UE a síťových zařízeních k ukládání konfiguračních dat, firmwaru a bezpečnostních klíčů. Data jsou uchována i po vypnutí napájení, ale umožňuje elektronické aktualizace pro provisioning a správu softwaru.

## Popis

Elektricky vymazatelná programovatelná paměť pouze pro čtení (EEPROM) je základní technologie nevolatilní paměti odkazovaná v 3GPP specifikacích pro ukládání kritických semitrvalých dat v uživatelském zařízení (UE) a prvcích síťové infrastruktury. Na rozdíl od volatilní paměti RAM si EEPROM uchovává uložené informace i po odstranění elektrického napájení. Na rozdíl od tradiční paměti ROM nebo PROM umožňuje data vymazat a přeprogramovat elektricky, přímo v obvodu, bez nutnosti fyzického odstranění. Díky tomu je ideální pro ukládání parametrů, které musí přetrvávat mezi cykly napájení, ale mohou občas vyžadovat aktualizaci.

V rámci architektury UE je EEPROM často vestavěna v integrovaných obvodech nebo existuje jako diskrétní komponenta. S hlavním procesorem zařízení nebo základním pásmovým modemem komunikuje prostřednictvím sériových komunikačních sběrnic jako I2C nebo SPI. V kontextu 3GPP se EEPROM používá pro ukládání širokého spektra nezbytných dat. To zahrnuje specifické konfigurační parametry zařízení kalibrované během výroby, preference výběru sítě, bezpečnostní data jako kryptografické klíče nebo certifikáty (např. pro autentizaci) a firmware pro periferní řadiče. Může také uchovávat perzistentní signalizační parametry [NAS](/mobilnisite/slovnik/nas/) nebo informace o schopnostech zařízení.

Provozní role EEPROM je zaměřena na trvalost a řízené aktualizace. Při startu nebo inicializaci software UE čte konfigurační data z EEPROM pro nastavení rádiových jednotek, zprovoznění protokolových zásobníků a vytvoření počátečních bezpečnostních kontextů. Například [IMEI](/mobilnisite/slovnik/imei/) (International Mobile Equipment Identity) může být uloženo v proti zápisu chráněné oblasti EEPROM. Během provozu může UE zapisovat aktualizovaná data do EEPROM, jako je nový seznam preferovaných PLMN, aktualizované informace o třídě řízení přístupu nebo změněná uživatelská nastavení. Proces zápisu probíhá po blocích nebo bajtech a je pomalejší než přístup do RAM, proto se používá uvážlivě pro data, která musí přežít restart.

Z pohledu sítě a standardů mohou 3GPP specifikace (jako TS 35.909 o bezpečnostních algoritmech) předpokládat nebo doporučovat použití zabezpečené EEPROM odolné proti neoprávněné manipulaci pro ukládání citlivého materiálu. Tím je zajištěno, že kritická autentizační data nejsou ztracena a nemohou být snadno extrahována nebo modifikována neautorizovanými stranami. Přeprogramovatelnost EEPROM je také klíčová pro správu zařízení přes vzduch ([OTA](/mobilnisite/slovnik/ota/)), což operátorům umožňuje vzdáleně aktualizovat firmware zařízení nebo konfigurační parametry zápisem nových dat do EEPROM pro trvalý účinek.

## K čemu slouží

Technologie EEPROM byla přijata k řešení potřeby trvalé, avšak aktualizovatelné paměti v mobilních zařízeních a síťových prvcích. Raná mobilní zařízení používala maskovou ROM nebo jednorázově programovatelnou PROM pro firmware, což znemožňovalo aktualizace v terénu, nebo pro konfiguraci RAM se zálohovací baterií, což s sebou neslo riziko ztráty dat. EEPROM poskytla nezbytný střední přístup: trvalost dat bez napájení a možnost aktualizace v terénu elektronicky.

Historický kontext v telekomunikacích představuje přechod k softwarově definovaným a konfigurovatelným zařízením. S vývojem mobilních standardů od 2G po 5G enormně vzrostl objem kalibračních dat specifických pro zařízení, síťových parametrů a bezpečnostních přihlašovacích údajů. Pevně zakódovaná data se stala nepraktickými. EEPROM umožnila výrobcům kalibrovat každé zařízení po výrobě, ukládat jedinečné identity ([IMEI](/mobilnisite/slovnik/imei/)) a později síťovým operátorům vzdáleně zřizovat zařízení. Stala se základním kamenem flexibilního, spravovatelného spotřebitelského hardwaru.

Tato technologie řeší významná omezení předchozích přístupů. Odstraňuje potřebu fyzické výměny paměťových čipů pro aktualizace (jako u [EPROM](/mobilnisite/slovnik/eprom/) vyžadujících pro vymazání UV světlo). Také poskytuje vyšší spolehlivost a nižší spotřebu energie ve srovnání s SRAM se zálohovací baterií. Z bezpečnostního hlediska lze implementovat vyhrazené zabezpečené oblasti EEPROM s hardwarovou ochranou, čímž se chrání citlivé klíče před softwarovými útoky. Její použití umožňuje kritické funkce 3GPP jako autentizaci zařízení, bezpečné ukládání dat aplikace USIM a aktualizace firmwaru pro opravy chyb a vylepšení funkcí během životního cyklu zařízení.

## Klíčové vlastnosti

- Nevolatilní uchování dat bez nutnosti napájení
- Elektricky vymazatelná a přeprogramovatelná přímo v obvodu (na úrovni bajtu nebo bloku)
- Pomalejší rychlost zápisu, ale rychlé čtení ve srovnání s volatilní pamětí
- Používá se pro ukládání konfigurace zařízení, kalibračních dat a bezpečnostních klíčů
- Umožňuje aktualizace přes vzduch (OTA) pro firmware a parametry
- Často zahrnuje hardwarové mechanizmy ochrany proti zápisu pro bezpečnostně kritické oblasti

## Související pojmy

- [IMEI – International Mobile Station Equipment Identities](/mobilnisite/slovnik/imei/)

## Definující specifikace

- **TR 35.909** (Rel-19) — 3GPP MILENAGE Algorithm Design Report

---

📖 **Anglický originál a plná specifikace:** [EEPROM na 3GPP Explorer](https://3gpp-explorer.com/glossary/eeprom/)
