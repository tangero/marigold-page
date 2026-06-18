---
slug: "xmac"
url: "/mobilnisite/slovnik/xmac/"
type: "slovnik"
title: "XMAC – Expected Message Authentication Code"
date: 2025-01-01
abbr: "XMAC"
fullName: "Expected Message Authentication Code"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/xmac/"
summary: "XMAC je bezpečnostní parametr vypočítávaný USIM během procedury 3G Authentication and Key Agreement (AKA). Představuje očekávanou hodnotu kódu autentizace zprávy (MAC) přijatého od sítě. USIM porovná"
---

XMAC je očekávaná hodnota kódu autentizace zprávy (Message Authentication Code) vypočtená USIM během 3G AKA za účelem autentizace sítě porovnáním s přijatým MAC.

## Popis

Expected Message Authentication Code (XMAC) je klíčová součást bezpečnostní architektury 3GPP, konkrétně pro protokol 3G Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)) definovaný pro UMTS. Je lokálně vypočítán na modulu [USIM](/mobilnisite/slovnik/usim/) (User Services Identity Module) v zařízení uživatele. K výpočtu dochází, když USIM přijme autentizační výzvu od navštívené nebo obsluhující sítě, která obsahuje náhodné číslo ([RAND](/mobilnisite/slovnik/rand/)) a autentizační token ([AUTN](/mobilnisite/slovnik/autn/)).

XMAC je generován pomocí kryptografického algoritmu, typicky sady algoritmů MILENAGE založené na blokové šifře Rijndael ([AES](/mobilnisite/slovnik/aes/)). USIM použije svůj dlouhodobý tajný klíč (K), sdílený pouze s autentizačním centrem (AuC) domovské sítě, spolu s přijatým RAND a dalšími parametry z AUTN (konkrétně sekvenčním číslem [SQN](/mobilnisite/slovnik/sqn/)) jako vstupy do stejné funkce pro generování [MAC](/mobilnisite/slovnik/mac/) (f1), kterou použil AuC. Tento proces vytvoří hodnotu XMAC. Základní bezpečnostní operací je porovnání: USIM extrahuje přijatý MAC (součást AUTN) a porovná jej se svým lokálně vypočteným XMAC. Pokud se shodují, USIM tím získá důkaz, že autentizační výzva pochází od legitimní sítě, která zná sdílený tajný klíč K, čímž je síť autentizována vůči uživateli.

Tento mechanismus je základním kamenem vzájemné autentizace v 3G sítích. Zatímco síť autentizuje uživatele prostřednictvím kontroly [RES](/mobilnisite/slovnik/res/) (Response) a XRES (Expected Response), uživatel autentizuje síť prostřednictvím kontroly XMAC/MAC. Tato obousměrná verifikace je zásadní pro prevenci hrozeb, jako jsou útoky falešnou základnovou stanicí, kde protivník vydává falešnou síť za legitimní za účelem zachycení komunikace nebo sledování uživatelů. Výpočet a ověření XMAC se provádí výhradně v bezpečném prostředí USIM, čímž je chráněn tajný klíč K před vystavením hlavnímu operačnímu systému zařízení.

Specifikace upravující XMAC, především TS 31.900 (USIM Application Toolkit) a TS 35.934 (Security algorithms), podrobně popisují přesné vstupy, algoritmické kroky a integraci s bezpečnými zpracovatelskými schopnostmi USIM. TS 31.900 pokrývá příkazy a procedury pro provedení výpočtu USIM, zatímco TS 35.934 definuje standardizované příkladové algoritmy jako MILENAGE. Integrita tohoto procesu zajišťuje, že připojení uživatele je navázáno pouze s důvěryhodným síťovým prvkem, který byl autorizován jeho domovským operátorem.

## K čemu slouží

XMAC byl zaveden, aby splnil požadavek na vzájemnou autentizaci v sítích 3GPP, což je významné vylepšení bezpečnosti oproti systému 2G (GSM). V GSM autentizovala pouze síť mobilní stanici; mobilní stanice neautentizovala síť. Tato jednostranná autentizace vytvářela zranitelnost vůči útokům falešnou základnovou stanicí (IMSI catcher), kdy útočníci mohli nastavit zařízení napodobující skutečnou síť, přimět telefony k připojení a následně zachycovat hovory nebo provoz.

Hlavní problém, který XMAC řeší, je poskytnutí uživatelského zařízení (prostřednictvím USIM) prostředku k ověření legitimity sítě. Tím, že umožňuje USIM nezávisle vypočítat očekávanou hodnotu MAC a porovnat ji s hodnotou poskytnutou sítí, systém zajišťuje, že autentizační požadavek mohl být vygenerován pouze subjektem disponujícím sdíleným tajným klíčem (K). Tento klíč zná pouze skutečné autentizační centrum (AuC) domovského operátora a USIM. Tento mechanismus účinně uzavírá bezpečnostní mezeru přítomnou v 2G.

Jeho vytvoření bylo motivováno širšími principy návrhu bezpečnosti 3G stanovenými v 3GPP Release 99, které ukládaly použití silnějších kryptografických algoritmů a vzájemnou autentizaci. XMAC spolu se správou SQN pro ochranu před opakovaným přehráním tvoří uživatelskou stranu tohoto procesu vzájemné autentizace. Standardizace výpočetní metody (např. v sadě algoritmů MILENAGE) zajistila interoperabilitu mezi USIM od různých výrobců a AuC od různých síťových operátorů, čímž vytvořila globálně důvěryhodný bezpečnostní základ pro UMTS a pozdější generace, které převzaly rámec AKA.

## Klíčové vlastnosti

- Vypočítává se lokálně na USIM pomocí sdíleného tajného klíče K
- Klíčová součást vzájemné autentizace 3G (AKA)
- Používá standardizované kryptografické funkce (např. MILENAGE f1)
- Vstupy zahrnují RAND, SQN a tajný klíč K
- Porovnává se s MAC přijatým v AUTN od sítě
- Ověření probíhá v bezpečném prostředí pro provádění USIM

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [AUTN – Authentication Token](/mobilnisite/slovnik/autn/)
- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)
- [AUC – Authentication Centre](/mobilnisite/slovnik/auc/)

## Definující specifikace

- **TR 31.900** (Rel-19) — 3GPP TS 31.900: Security Interworking Guidance
- **TR 35.934** (Rel-19) — Tuak algorithm set for 3GPP auth & key gen

---

📖 **Anglický originál a plná specifikace:** [XMAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/xmac/)
